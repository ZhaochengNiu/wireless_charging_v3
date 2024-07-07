import pickle
import logging
import math
import numpy as np

from Decision import Decision
from MobileDevice import MobileDevice
from Edge import Edge
from Config import Config
from Task import Task
from algorithm import local_algorithm, nearest_bs_algorithm, random_algorithm, proposed_algorithm, proposed_algorithm_v2,binary_match_game
from trans_rate import get_upload_gain, get_d2d_gain, get_upload_rate, get_d2d_rate

# 只考虑任务执行时间的版本

logging.basicConfig(level=logging.ERROR)

config = Config()
devices = []
edges = []


task_in_each_slot = [[0 for _ in range(config.total_number_of_devices)] for _ in range(config.times)]
x_location_in_each_slot = [[0 for _ in range(config.total_number_of_devices)] for _ in range(config.times)]
y_location_in_each_slot = [[0 for _ in range(config.total_number_of_devices)] for _ in range(config.times)]
number_of_tasks_in_each_slot = [0 for _ in range(config.times)]
io_in_each_slot = []
ave_queue_length_in_each_slot = []
ave_execute_latency_in_each_slot = []
energy_consumption_in_each_slot = []
energy_harvest_in_each_slot = []
latency_cost_in_each_slot = []
energy_cost_in_each_slot = []
total_cost_in_each_slot = []
local_ratio_in_each_slot = [0.0 for _ in range(config.times)]
edge_ratio_in_each_slot = [0.0 for _ in range(config.times)]
d2d_ratio_in_each_slot = [0.0 for _ in range(config.times)]


def init_edge_device():
    # 初始化边缘和设备
    global devices
    global edges
    global x_location_in_each_slot
    global y_location_in_each_slot

    if config.cache is True:
        devices_cache_file = open(config.devices_cache_file_path, 'rb')
        devices = pickle.load(devices_cache_file)
        edges_cache_file = open(config.edges_cache_file_path, 'rb')
        edges = pickle.load(edges_cache_file)
        x_location_cache_file = open(config.x_location_cache_file_path, 'rb')
        x_location_in_each_slot = pickle.load(x_location_cache_file)
        y_location_cache_file = open(config.y_location_cache_file_path, 'rb')
        y_location_in_each_slot = pickle.load(y_location_cache_file)
    else:
        for i in range(0, config.total_number_of_edges):
            frequency = config.edge_cpu_frequency
            ncp_type = 'EDGE'
            nid = i
            edge = Edge(nid=nid, frequency=frequency, ncp_type=ncp_type, x=config.edge_locations[i][0],
                        y=config.edge_locations[i][1], coverage_radius=config.coverage_radius,
                        total_number_of_devices=config.total_number_of_devices)
            edges.append(edge)

        for i in range(0, config.total_number_of_active_devices):
            frequency = config.activate_device_cpu_frequency
            ncp_type = 'ACT DEV'
            nid = i
            device = MobileDevice(nid=nid, init_energy=config.max_energy_queue_length,
                                  max_energy_queue_length=config.max_energy_queue_length, frequency=frequency,
                                  ncp_type=ncp_type, move_distance= config.MOVE_DISTANCE,
                                  total_number_of_edges=config.total_number_of_edges,
                                  min_x_location=config.MIN_X_LOCATION, max_x_location=config.MAX_X_LOCATION,
                                  min_y_location=config.MIN_Y_LOCATION, max_y_location=config.MAX_Y_LOCATION,
                                  generating_tasks_probability_of_device=config.generating_tasks_probability_of_active_device)
            device.init_position()
            device.init_velocity_direction()
            device.get_the_distance(total_number_of_edges=config.total_number_of_edges, edges=edges)
            devices.append(device)
            x_location_in_each_slot[0][i] = device.x
            y_location_in_each_slot[0][i] = device.y
        for i in range(config.total_number_of_active_devices, config.total_number_of_devices):
            frequency = config.passive_device_cpu_frequency
            ncp_type = 'PAS DEV'
            nid = i
            device = MobileDevice(nid=nid, init_energy=config.max_energy_queue_length,
                                  max_energy_queue_length=config.max_energy_queue_length, frequency=frequency,
                                  ncp_type=ncp_type, move_distance= config.MOVE_DISTANCE,
                                  total_number_of_edges=config.total_number_of_edges,
                                  min_x_location=config.MIN_X_LOCATION, max_x_location=config.MAX_X_LOCATION,
                                  min_y_location=config.MIN_Y_LOCATION, max_y_location=config.MAX_Y_LOCATION,
                                  generating_tasks_probability_of_device=config.generating_tasks_probability_of_active_device)
            device.init_position()
            device.init_velocity_direction()
            device.get_the_distance(total_number_of_edges=config.total_number_of_edges, edges=edges)
            devices.append(device)
            x_location_in_each_slot[0][i] = device.x
            y_location_in_each_slot[0][i] = device.y

    # 保存到文件中
        devices_cache_file = open(config.devices_cache_file_path, 'wb')
        pickle.dump(devices, devices_cache_file)
        edges_cache_file = open(config.edges_cache_file_path, 'wb')
        pickle.dump(edges, edges_cache_file)


# 模拟负载
def mock_load():
    # 模拟负载
    global task_in_each_slot
    global number_of_tasks_in_each_slot

    if config.cache is True:
        task_cache_file = open(config.task_cache_file_path, 'rb')
        task_in_each_slot = pickle.load(task_cache_file)
        number_of_tasks_cache_file = open(config.number_of_tasks_cache_file_path, 'rb')
        number_of_tasks_in_each_slot = pickle.load(number_of_tasks_cache_file)
    else:
        for time_slot in range(0, config.times):
            for i in range(0, config.total_number_of_devices):
                whether_generate_task = np.random.uniform(0, 1)
                if whether_generate_task < devices[i].generating_tasks_probability_of_device:
                    number_of_tasks_in_each_slot[time_slot] = number_of_tasks_in_each_slot[time_slot] + 1
                    data_size = np.random.uniform(config.task_size[0], config.task_size[1])
                    cpu_frequency_demand = config.task_cpu_frequency_demand * data_size
                    task = Task(data_size=data_size, cpu_frequency_demand=cpu_frequency_demand)
                    task_in_each_slot[time_slot][i] = task
                else:
                    pass
        task_cache_file = open(config.task_cache_file_path, 'wb')
        pickle.dump(task_in_each_slot, task_cache_file)
        number_of_tasks_cache_file = open(config.number_of_tasks_cache_file_path, 'wb')
        pickle.dump(number_of_tasks_in_each_slot, number_of_tasks_cache_file)


def edge_compute(edge):
    # 边缘计算
    slot_computing_data_size = config.time_slot_length * edge.frequency
    task_queue_length = edge.task_queue_length()
    if slot_computing_data_size <= task_queue_length:
        edge.task_dequeue(cpu_frequency_demand=slot_computing_data_size)
        edge_computing_size = slot_computing_data_size
    elif slot_computing_data_size > task_queue_length:
        edge.task_dequeue(cpu_frequency_demand=slot_computing_data_size)
        edge_computing_size = task_queue_length
    else:
        print('error_135')
    return edge_computing_size


def device_compute(device):
    # 设备计算
    slot_computing_data_size = config.time_slot_length * device.frequency
    task_queue_length = device.task_queue_length()
    if slot_computing_data_size <= task_queue_length:
        device.task_dequeue(cpu_frequency_demand=slot_computing_data_size)
        local_computing_size = slot_computing_data_size
    elif slot_computing_data_size > task_queue_length:
        device.task_dequeue(cpu_frequency_demand=slot_computing_data_size)
        local_computing_size = task_queue_length
    else:
        print('error_150')
    return local_computing_size


def make_decision(time_slot):
    # 决策
    global task_in_each_slot
    global local_ratio_in_each_slot
    global edge_ratio_in_each_slot
    global d2d_ratio_in_each_slot

    decisions = Decision()
    if config.algorithm == 'local_algorithm':
        decisions = local_algorithm(decisions=decisions, config=config, time_slot=time_slot,
                                    task_in_each_slot=task_in_each_slot)
    elif config.algorithm == 'nearest_algorithm':
        decisions = nearest_bs_algorithm(decisions=decisions, config=config, devices=devices, edges=edges,time_slot=time_slot,
                                         task_in_each_slot=task_in_each_slot)
    elif config.algorithm == 'random_algorithm':
        decisions = random_algorithm(decisions=decisions, config=config, devices=devices, edges=edges,
                                     time_slot=time_slot, task_in_each_slot=task_in_each_slot)
    elif config.algorithm == 'match_algorithm':
        decisions = binary_match_game(decisions=decisions, config=config, devices=devices, edges=edges, time_slot=time_slot,
                                       task_in_each_slot=task_in_each_slot)
    elif config.algorithm == 'proposed_algorithm':
        decisions = proposed_algorithm(decisions=decisions, config=config, devices=devices, edges=edges, time_slot=time_slot,
                                       task_in_each_slot=task_in_each_slot)
    elif config.algorithm == 'proposed_algorithm_v2':
        decisions = proposed_algorithm_v2(decisions=decisions, config=config, devices=devices, edges=edges, time_slot=time_slot,
                                       task_in_each_slot=task_in_each_slot)
    else:
        pass
    if config.algorithm == 'proposed_algorithm':
        for i in range(0, config.total_number_of_devices):
            if decisions.execute_mode[i] == 'local':
                local_ratio_in_each_slot[time_slot] = local_ratio_in_each_slot[time_slot] + 1
            elif decisions.execute_mode[i] == 'edge':
                edge_ratio_in_each_slot[time_slot] = edge_ratio_in_each_slot[time_slot] + 1
            elif decisions.execute_mode[i] == 'device':
                d2d_ratio_in_each_slot[time_slot] = d2d_ratio_in_each_slot[time_slot] + 1
    return decisions


def execute_decision(device, edges, time_slot, decisions):
    # 执行决策
    global task_in_each_slot
    global io_in_each_slot
    if decisions.execute_mode[device.id] != 'null':
        task = task_in_each_slot[time_slot][device.id]
        data_size = task_in_each_slot[time_slot][device.id].data_size
        cpu_frequency_demand = task_in_each_slot[time_slot][device.id].cpu_frequency_demand
        # 获取权重 要在耗能之前
        latency_weight, energy_weight = device.get_weight()
        if decisions.execute_mode[device.id] == 'local' and decisions.execute_destination[device.id] == -1:
            # print('local')
            # 本地计算时间
            device.task_enqueue(cpu_frequency_demand=cpu_frequency_demand)
            queue_length = device.task_queue_length()
            local_execute_latency = queue_length / device.frequency
            latency_cost = local_execute_latency
            # print('latency_cost', latency_cost)
            # 本地计算能耗
            local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(device.frequency, 3)
            local_computing_latency = cpu_frequency_demand / device.frequency
            energy_consumption = local_computing_latency * local_computing_power
            # print('energy_consumption', energy_consumption)
            # 能量出队
            energy_queue_length = device.energy_queue_length()
            if energy_queue_length < energy_consumption:
                device.energy_consumption(energy_cost=energy_consumption)
                print('energy exhaustion')
            elif energy_queue_length >= energy_consumption:
                device.energy_consumption(energy_cost=energy_consumption)
            else:
                print('error_224')
            # 收集能量
            min_distance = 4000
            destination = -1
            for j in range(0, len(device.distance_BS)):
                distance = device.distance_BS[j]
                if distance < min_distance:
                    min_distance = distance
                    destination = j
            if device.locate_BS[destination] == 1:
                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * config.time_slot_length
                # print('energy_harvest', energy_harvest)
            else:
                energy_harvest = 0
            # 能量入队
            device.energy_harvest(energy_harvest)
            # 打印当前能量
            # print('energy queue length', device.energy_queue_length())
            # 能量效用
            energy_cost = energy_consumption - energy_harvest
            # print(energy_cost)
            # 总效用
            # cost = latency_weight * latency_cost + energy_weight * energy_cost
            # scale
            cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost

        elif decisions.execute_mode[device.id] == 'edge':
            # print('edge')
            execute_edge_id = decisions.execute_destination[device.id]
            local_computing_portion = decisions.local_computing_portion[device.id]
            execute_edge = edges[execute_edge_id]
            # 计算卸载数据大小
            offload_computing_portion = (1 - local_computing_portion)
            # print('offload_computing_portion', offload_computing_portion)
            if offload_computing_portion > 0:
                offload_data_size = data_size * offload_computing_portion
                # 计算传输速率
                interference = 0
                for i in range(0, config.total_number_of_devices):
                    if i != device.id and decisions.execute_mode[i] == 'edge' and decisions.execute_destination[i] == execute_edge_id:
                        gain = get_upload_gain(device=devices[i], edge=execute_edge)
                        interference += gain
                upload_rate = get_upload_rate(device=device, edge=execute_edge, interference=interference)
                # print('upload_rate', upload_rate/8388608)
                # 传输时间
                edge_transmit_latency = offload_data_size / upload_rate
                edge_transmit_latency = round(edge_transmit_latency, 6)
                # print('edge_transmit_latency=', edge_transmit_latency)
                if edge_transmit_latency >= config.time_slot_length:
                    edge_transmit_latency = config.time_slot_length
                print('real_edge_transmit_latency=', edge_transmit_latency)
                # 传输能耗
                trans_energy_consumption = edge_transmit_latency * device.offload_trans_power
            elif offload_computing_portion == 0:
                # 传输时间
                edge_transmit_latency = 0
                # 传输能耗
                trans_energy_consumption = 0
            else:
                print('error_282')
            # 收集能量
            min_distance = 4000
            destination = -1
            for j in range(0, len(device.distance_BS)):
                distance = device.distance_BS[j]
                if distance < min_distance:
                    min_distance = distance
                    destination = j
            if device.locate_BS[destination] == 1:
                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
                print('energy harvest slot length =', energy_harvest_slot_length)
                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                # print('energy harvest ', energy_harvest)
            else:
                energy_harvest = 0
            # 本地计算时间
            if local_computing_portion > 0:
                if edge_transmit_latency == config.time_slot_length:
                    edge_transmit_data_size = upload_rate * config.time_slot_length
                    local_computing_data_size = data_size - edge_transmit_data_size
                    local_computing_cpu_demand = local_computing_data_size * config.task_cpu_frequency_demand
                else:
                    local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                device.task_enqueue(cpu_frequency_demand=local_computing_cpu_demand)
                # 队列长度
                queue_length = device.task_queue_length()
                # 本地计算时间
                local_execute_latency = queue_length / device.frequency
                # 本地计算能耗
                local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(device.frequency, 3)
                local_computing_latency = local_computing_cpu_demand / device.frequency
                local_computing_energy_consumption = local_computing_latency * local_computing_power
            elif local_computing_portion == 0:
                local_computing_cpu_demand = 0
                local_execute_latency = 0
                local_computing_energy_consumption = 0
            else:
                print('error_321')
            # 能量消耗
            energy_consumption = local_computing_energy_consumption + trans_energy_consumption
            # print('energy_consumption', energy_consumption)
            # 能量出队
            energy_queue_length = device.energy_queue_length()
            if energy_queue_length < energy_consumption:
                device.energy_consumption(energy_consumption)
                print('energy exhaustion')
            elif energy_queue_length >= energy_consumption:
                device.energy_consumption(energy_consumption)
            else:
                print('error_333')
            # 能量入队
            device.energy_harvest(energy_harvest)
            # 打印能量
            # print('energy queue length', device.energy_queue_length())
            # 能量效用
            energy_cost = energy_consumption - energy_harvest
            # print('energy_cost', energy_cost)
            # 边缘计算执行时间
            if offload_computing_portion > 0:
                offload_computing_cpu_demand = cpu_frequency_demand - local_computing_cpu_demand
                execute_edge.task_enqueue(cpu_frequency_demand=offload_computing_cpu_demand)
                edge_queue_length = execute_edge.task_queue_length()
                edge_compute_task_latency = edge_queue_length / execute_edge.frequency
            elif offload_computing_portion == 0:
                edge_compute_task_latency = 0
            else:
                print('error_350')
            edge_execute_latency = edge_transmit_latency + edge_compute_task_latency
            # 延迟效用
            # print('local_execute_latency', local_execute_latency)
            # print('edge_execute_latency', edge_execute_latency)
            latency_cost = max(local_execute_latency, edge_execute_latency)
            # print('latency_cost', latency_cost)
            # 总效用
            # cost = latency_weight * latency_cost + energy_weight * energy_cost
            # scale
            cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost

        elif decisions.execute_mode[device.id] == 'device':
            # print('device')
            execute_device_id = decisions.execute_destination[device.id]
            local_computing_portion = decisions.local_computing_portion[device.id]
            execute_device = devices[execute_device_id]
            # 计算卸载数据大小
            offload_computing_portion = (1 - local_computing_portion)
            if offload_computing_portion > 0:
                offload_data_size = data_size * offload_computing_portion
                # 计算传输速率
                interference = 0
                for i in range(0, config.total_number_of_devices):
                    if i != device.id and decisions.execute_mode[i] == 'device' and decisions.execute_destination[i] == execute_device_id:
                        gain = get_d2d_gain(device1=devices[i], device2=devices[execute_device_id])
                        interference += gain
                d2d_rate = get_d2d_rate(device1=device, device2=execute_device, interference=interference)
                # print('d2d_rate', d2d_rate/8388608)
                # 传输时间
                d2d_transmit_latency = offload_data_size / d2d_rate
                d2d_transmit_latency = round(d2d_transmit_latency, 6)
                if d2d_transmit_latency >= config.time_slot_length:
                    d2d_transmit_latency = config.time_slot_length
                print('d2d_transmit_latency', d2d_transmit_latency)
                # 传输能耗
                trans_energy_consumption = d2d_transmit_latency * device.d2d_trans_power
                # d2d 计算能耗
                trans_data_size = d2d_transmit_latency * d2d_rate
                trans_computing_cpu_demand = trans_data_size * config.task_cpu_frequency_demand
                trans_computing_power = config.SWITCHED_CAPACITANCE * math.pow(execute_device.frequency, 3)
                trans_computing_latency = trans_computing_cpu_demand / execute_device.frequency
                trans_computing_energy_consumption = trans_computing_latency * trans_computing_power
                # 总能耗
                total_trans_energy_consumption = trans_energy_consumption + trans_computing_energy_consumption
            elif offload_computing_portion == 0:
                # 传输时间
                d2d_transmit_latency = 0
                # 传输能耗
                trans_energy_consumption = 0
                # d2d 计算能耗
                trans_computing_energy_consumption = 0
                # 总能耗
                total_trans_energy_consumption = 0
            else:
                print('error_403')
            # 收集能量
            min_distance = 4000
            destination = -1
            for j in range(0, len(device.distance_BS)):
                distance = device.distance_BS[j]
                if distance < min_distance:
                    min_distance = distance
                    destination = j
            if device.locate_BS[destination] == 1:
                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
                # print('energy_harvest_slot_length', energy_harvest_slot_length)
                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                print('energy_harvest', energy_harvest)
            else:
                energy_harvest = 0
            # 本地计算时间
            if local_computing_portion > 0:
                if d2d_transmit_latency == config.time_slot_length:
                    d2d_transmit_data_size = d2d_rate * config.time_slot_length
                    local_computing_data_size = data_size - d2d_transmit_data_size
                    local_computing_cpu_demand = local_computing_data_size * config.task_cpu_frequency_demand
                else:
                    local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                device.task_enqueue(cpu_frequency_demand=local_computing_cpu_demand)
                # 队列长度
                queue_length = device.task_queue_length()
                # 本地计算时间
                local_execute_latency = queue_length / device.frequency
                # 本地计算能耗
                local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(device.frequency, 3)
                local_computing_latency = local_computing_cpu_demand / device.frequency
                local_computing_energy_consumption = local_computing_latency * local_computing_power
            elif local_computing_portion == 0:
                local_computing_cpu_demand = 0
                local_execute_latency = 0
                local_computing_energy_consumption = 0
            else:
                print('error_442')
            # 能量消耗
            energy_consumption = local_computing_energy_consumption + total_trans_energy_consumption
            # print('energy_consumption', energy_consumption)
            # 能量出队
            energy_queue_length = device.energy_queue_length()
            if energy_queue_length < energy_consumption:
                device.energy_consumption(energy_consumption)
                print('energy exhaustion')
            elif energy_queue_length >= energy_consumption:
                device.energy_consumption(energy_consumption)
            else:
                print('error_451')
            # 能量入队
            device.energy_harvest(energy_harvest)
            # 打印能量
            # print('energy queue length', device.energy_queue_length())
            # 能量效用
            energy_cost = energy_consumption - energy_harvest
            # print('energy_cost', energy_cost)
            # 边缘计算执行时间
            if offload_computing_portion > 0:
                offload_computing_cpu_demand = cpu_frequency_demand - local_computing_cpu_demand
                execute_device.task_enqueue(cpu_frequency_demand=offload_computing_cpu_demand)
                d2d_queue_length = execute_device.task_queue_length()
                d2d_compute_task_latency = d2d_queue_length / execute_device.frequency
            elif offload_computing_portion == 0:
                d2d_compute_task_latency = 0
            else:
                print('error_471')
            d2d_execute_latency = d2d_transmit_latency + d2d_compute_task_latency
            # 延迟效用
            # print('local_execute_latency', local_execute_latency)
            # print('d2d_execute_latency', d2d_execute_latency)
            latency_cost = max(local_execute_latency, d2d_execute_latency)
            # print('latency_cost', latency_cost)
            # 总效用
            # cost = latency_weight * latency_cost + energy_weight * energy_cost
            # scale
            cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
        # logging.info("<Time-%s> --> <NCP-%s> ｜ 执行后Q: %s  执行成本:%s", time_slot, device.id, device.queue, total_cost)
        else:
            print('error_482')
    elif decisions.execute_mode[device.id] == 'null':
        latency_cost = 0
        # 收集能量
        min_distance = 4000
        destination = -1
        for j in range(0, len(device.distance_BS)):
            distance = device.distance_BS[j]
            if distance < min_distance:
                min_distance = distance
                destination = j
        if device.locate_BS[destination] == 1:
            energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
            energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * config.time_slot_length
        else:
            energy_harvest = 0
        device.energy_harvest(energy_harvest)
        energy_cost = 0
        energy_consumption = 0
        cost = 0
    else:
        print("error_503")
    return latency_cost, energy_cost, energy_consumption, energy_harvest, cost


def execute_decision_v2(device, edges, time_slot, decisions):
    # 执行决策
    global task_in_each_slot
    global io_in_each_slot
    if decisions.execute_mode[device.id] != 'null':
        task = task_in_each_slot[time_slot][device.id]
        data_size = task_in_each_slot[time_slot][device.id].data_size
        cpu_frequency_demand = task_in_each_slot[time_slot][device.id].cpu_frequency_demand
        # 获取权重 要在耗能之前
        latency_weight, energy_weight = device.get_weight()
        if decisions.execute_mode[device.id] == 'local' and decisions.execute_destination[device.id] == -1:
            # print('local')
            queue_length_last_slot = device.task_queue_length() / config.task_cpu_frequency_demand
            queue_length_last_slot = queue_length_last_slot / 8388608
            # 本地计算时间
            device.task_enqueue(cpu_frequency_demand=cpu_frequency_demand)
            queue_length = device.task_queue_length()
            local_execute_latency = queue_length / device.frequency
            latency_utility = local_execute_latency
            # print('latency_utility', latency_utility)
            # 本地计算能耗
            local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(device.frequency, 3)
            local_computing_latency = cpu_frequency_demand / device.frequency
            energy_cost = local_computing_latency * local_computing_power
            # print('energy_cost', energy_cost)
            # 能量出队
            energy_queue_length = device.energy_queue_length()
            if energy_queue_length < energy_cost:
                device.energy_consumption(energy_cost=energy_cost)
                print('energy exhaustion')
            elif energy_queue_length >= energy_cost:
                device.energy_consumption(energy_cost=energy_cost)
            else:
                print('error')
            # 收集能量
            min_distance = 4000
            destination = -1
            for j in range(0, len(device.distance_BS)):
                distance = device.distance_BS[j]
                if distance < min_distance:
                    min_distance = distance
                    destination = j
            if device.locate_BS[destination] == 1:
                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * config.time_slot_length
                # print('energy_harvest', energy_harvest)
            else:
                energy_harvest = 0
            # 能量入队
            device.energy_harvest(energy_harvest)
            # 打印当前能量
            # print('energy queue length', device.energy_queue_length())
            # 能量效用
            energy_utility = energy_cost - energy_harvest
            # print(energy_utility)
            # 总效用
            utility = latency_weight * latency_utility + energy_weight * energy_utility
            print('local: utility', utility)
            # 计算lyapunov
            cpu_frequency_demand_offload = 0
            for j in range(0, config.total_number_of_devices):
                if j != device.id and decisions.execute_mode[j] == 'device' and decisions.execute_destination[j] == device.id:
                    cpu_frequency_demand_lya = task_in_each_slot[time_slot][j].cpu_frequency_demand
                    local_computing_portion = decisions.local_computing_portion[j]
                    offload_computing_portion = (1 - local_computing_portion)
                    cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
            cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand
            cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
            cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
            lya = pow(cpu_frequency_demand_offload, 2) + 2 * queue_length_last_slot * cpu_frequency_demand_offload
            print('local: lya', lya)
        elif decisions.execute_mode[device.id] == 'edge':
            # print('edge')
            queue_length_last_slot = device.task_queue_length() / config.task_cpu_frequency_demand
            queue_length_last_slot = queue_length_last_slot / 8388608
            execute_edge_id = decisions.execute_destination[device.id]
            local_computing_portion = decisions.local_computing_portion[device.id]
            execute_edge = edges[execute_edge_id]
            # 计算卸载数据大小
            offload_computing_portion = (1 - local_computing_portion)
            # print('offload_computing_portion', offload_computing_portion)
            if offload_computing_portion > 0:
                offload_data_size = data_size * offload_computing_portion
                # 计算传输速率
                interference = 0
                for i in range(0, config.total_number_of_devices):
                    if i != device.id and decisions.execute_mode[i] == 'edge' and decisions.execute_destination[i] == execute_edge_id:
                        gain = get_upload_gain(device=devices[i], edge=execute_edge)
                        interference += gain
                upload_rate = get_upload_rate(device=device, edge=execute_edge, interference=interference)
                # print('upload_rate', upload_rate/8388608)
                # 传输时间
                edge_transmit_latency = offload_data_size / upload_rate
                edge_transmit_latency = round(edge_transmit_latency, 6)
                # print('edge_transmit_latency=', edge_transmit_latency)
                if edge_transmit_latency >= config.time_slot_length:
                    edge_transmit_latency = config.time_slot_length
                print('real_edge_transmit_latency=', edge_transmit_latency)
                # 传输能耗
                trans_energy_cost = edge_transmit_latency * device.offload_trans_power
            elif offload_computing_portion == 0:
                # 传输时间
                edge_transmit_latency = 0
                # 传输能耗
                trans_energy_cost = 0
            else:
                print('error')
            # 收集能量
            min_distance = 4000
            destination = -1
            for j in range(0, len(device.distance_BS)):
                distance = device.distance_BS[j]
                if distance < min_distance:
                    min_distance = distance
                    destination = j
            if device.locate_BS[destination] == 1:
                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
                print('energy harvest slot length =', energy_harvest_slot_length)
                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                # print('energy harvest ', energy_harvest)
            else:
                energy_harvest = 0
            # 本地计算时间
            if local_computing_portion > 0:
                if edge_transmit_latency == config.time_slot_length:
                    edge_transmit_data_size = upload_rate * config.time_slot_length
                    local_computing_data_size = data_size - edge_transmit_data_size
                    local_computing_cpu_demand = local_computing_data_size * config.task_cpu_frequency_demand
                else:
                    local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                device.task_enqueue(cpu_frequency_demand=local_computing_cpu_demand)
                # 队列长度
                queue_length = device.task_queue_length()
                # 本地计算时间
                local_execute_latency = queue_length / device.frequency
                # 本地计算能耗
                local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(device.frequency, 3)
                local_computing_latency = local_computing_cpu_demand / device.frequency
                local_computing_energy_cost = local_computing_latency * local_computing_power
            elif local_computing_portion == 0:
                local_computing_cpu_demand = 0
                local_execute_latency = 0
                local_computing_energy_cost = 0
            else:
                print('error')
            # 能量消耗
            energy_cost = local_computing_energy_cost + trans_energy_cost
            # print('energy_cost', energy_cost)
            # 能量出队
            energy_queue_length = device.energy_queue_length()
            if energy_queue_length < energy_cost:
                device.energy_consumption(energy_cost)
                print('energy exhaustion')
            elif energy_queue_length >= energy_cost:
                device.energy_consumption(energy_cost)
            else:
                print('error')
            # 能量入队
            device.energy_harvest(energy_harvest)
            # 打印能量
            # print('energy queue length', device.energy_queue_length())
            # 能量效用
            energy_utility = energy_cost - energy_harvest
            # print('energy_utility', energy_utility)
            # 边缘计算执行时间
            if offload_computing_portion > 0:
                offload_computing_cpu_demand = cpu_frequency_demand - local_computing_cpu_demand
                execute_edge.task_enqueue(cpu_frequency_demand=offload_computing_cpu_demand)
                edge_queue_length = execute_edge.task_queue_length()
                edge_compute_task_latency = edge_queue_length / execute_edge.frequency
            elif offload_computing_portion == 0:
                edge_compute_task_latency = 0
            else:
                print('error')
            edge_execute_latency = edge_transmit_latency + edge_compute_task_latency
            # 延迟效用
            # print('local_execute_latency', local_execute_latency)
            # print('edge_execute_latency', edge_execute_latency)
            latency_utility = max(local_execute_latency, edge_execute_latency)
            # print('latency_utility', latency_utility)
            # 总效用
            utility = latency_weight * latency_utility + energy_weight * energy_utility
            print('edge: utility', utility)
            # 计算lyapunov
            cpu_frequency_demand_offload = 0
            for j in range(0, config.total_number_of_devices):
                if j != device.id and decisions.execute_mode[j] == 'device' and decisions.execute_destination[j] == device.id:
                    cpu_frequency_demand_lya = task_in_each_slot[time_slot][j].cpu_frequency_demand
                    local_computing_portion = decisions.local_computing_portion[j]
                    offload_computing_portion = (1 - local_computing_portion)
                    cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
            cpu_frequency_demand_offload = cpu_frequency_demand_offload + local_computing_cpu_demand
            cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
            cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
            lya = pow(cpu_frequency_demand_offload, 2) + 2 * queue_length_last_slot * cpu_frequency_demand_offload
            print('edge: lya', lya)
        elif decisions.execute_mode[device.id] == 'device':
            # print('device')
            queue_length_last_slot = device.task_queue_length() / config.task_cpu_frequency_demand
            queue_length_last_slot = queue_length_last_slot / 8388608
            execute_device_id = decisions.execute_destination[device.id]
            local_computing_portion = decisions.local_computing_portion[device.id]
            execute_device = devices[execute_device_id]
            # 计算卸载数据大小
            offload_computing_portion = (1 - local_computing_portion)
            if offload_computing_portion > 0:
                offload_data_size = data_size * offload_computing_portion
                # 计算传输速率
                interference = 0
                for i in range(0, config.total_number_of_devices):
                    if i != device.id and decisions.execute_mode[i] == 'device' and decisions.execute_destination[i] == execute_device_id:
                        gain = get_d2d_gain(device1=devices[i], device2=devices[execute_device_id])
                        interference += gain
                d2d_rate = get_d2d_rate(device1=device, device2=execute_device, interference=interference)
                # print('d2d_rate', d2d_rate/8388608)
                # 传输时间
                d2d_transmit_latency = offload_data_size / d2d_rate
                d2d_transmit_latency = round(d2d_transmit_latency, 6)
                if d2d_transmit_latency >= config.time_slot_length:
                    d2d_transmit_latency = config.time_slot_length
                print('d2d_transmit_latency', d2d_transmit_latency)
                # 传输能耗
                trans_energy_cost = d2d_transmit_latency * device.d2d_trans_power
            elif offload_computing_portion == 0:
                # 传输时间
                d2d_transmit_latency = 0
                # 传输能耗
                trans_energy_cost = 0
            else:
                print('error')
            # 收集能量
            min_distance = 4000
            destination = -1
            for j in range(0, len(device.distance_BS)):
                distance = device.distance_BS[j]
                if distance < min_distance:
                    min_distance = distance
                    destination = j
            if device.locate_BS[destination] == 1:
                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
                # print('energy_harvest_slot_length', energy_harvest_slot_length)
                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                print('energy_harvest', energy_harvest)
            else:
                energy_harvest = 0
            # 本地计算时间
            if local_computing_portion > 0:
                if d2d_transmit_latency == config.time_slot_length:
                    d2d_transmit_data_size = d2d_rate * config.time_slot_length
                    local_computing_data_size = data_size - d2d_transmit_data_size
                    local_computing_cpu_demand = local_computing_data_size * config.task_cpu_frequency_demand
                else:
                    local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                device.task_enqueue(cpu_frequency_demand=local_computing_cpu_demand)
                # 队列长度
                queue_length = device.task_queue_length()
                # 本地计算时间
                local_execute_latency = queue_length / device.frequency
                # 本地计算能耗
                local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(device.frequency, 3)
                local_computing_latency = local_computing_cpu_demand / device.frequency
                local_computing_energy_cost = local_computing_latency * local_computing_power
            elif local_computing_portion == 0:
                local_computing_cpu_demand = 0
                local_execute_latency = 0
                local_computing_energy_cost = 0
            else:
                print('error')
            # 能量消耗
            energy_cost = local_computing_energy_cost + trans_energy_cost
            # print('energy_cost', energy_cost)
            # 能量出队
            energy_queue_length = device.energy_queue_length()
            if energy_queue_length < energy_cost:
                device.energy_consumption(energy_cost)
                print('energy exhaustion')
            elif energy_queue_length >= energy_cost:
                device.energy_consumption(energy_cost)
            else:
                print('error')
            # 能量入队
            device.energy_harvest(energy_harvest)
            # 打印能量
            # print('energy queue length', device.energy_queue_length())
            # 能量效用
            energy_utility = energy_cost - energy_harvest
            # print('energy_utility', energy_utility)
            # 边缘计算执行时间
            if offload_computing_portion > 0:
                offload_computing_cpu_demand = cpu_frequency_demand - local_computing_cpu_demand
                execute_device.task_enqueue(cpu_frequency_demand=offload_computing_cpu_demand)
                d2d_queue_length = execute_device.task_queue_length()
                d2d_compute_task_latency = d2d_queue_length / execute_device.frequency
            elif offload_computing_portion == 0:
                d2d_compute_task_latency = 0
            else:
                print('error')
            d2d_execute_latency = d2d_transmit_latency + d2d_compute_task_latency
            # 延迟效用
            # print('local_execute_latency', local_execute_latency)
            # print('d2d_execute_latency', d2d_execute_latency)
            latency_utility = max(local_execute_latency, d2d_execute_latency)
            # print('latency_utility', latency_utility)
            # 总效用
            utility = latency_weight * latency_utility + energy_weight * energy_utility
            print('d2d: utility', utility)
            # 计算lyapunov
            cpu_frequency_demand_offload = 0
            for j in range(0, config.total_number_of_devices):
                if j != device.id and decisions.execute_mode[j] == 'device' and decisions.execute_destination[j] == device.id:
                    cpu_frequency_demand_lya = task_in_each_slot[time_slot][j].cpu_frequency_demand
                    local_computing_portion = decisions.local_computing_portion[j]
                    offload_computing_portion = (1 - local_computing_portion)
                    cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
            cpu_frequency_demand_offload = cpu_frequency_demand_offload + local_computing_cpu_demand
            cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
            cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
            lya = pow(cpu_frequency_demand_offload, 2) + 2 * queue_length_last_slot * cpu_frequency_demand_offload
            print('d2d: lya', lya)
        # logging.info("<Time-%s> --> <NCP-%s> ｜ 执行后Q: %s  执行成本:%s", time_slot, device.id, device.queue, total_cost)
        else:
            print('error')
    elif decisions.execute_mode[device.id] == 'null':
        latency_utility = 0
        # 收集能量
        min_distance = 4000
        destination = -1
        for j in range(0, len(device.distance_BS)):
            distance = device.distance_BS[j]
            if distance < min_distance:
                min_distance = distance
                destination = j
        if device.locate_BS[destination] == 1:
            energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
            energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * config.time_slot_length
        else:
            energy_harvest = 0
        device.energy_harvest(energy_harvest)
        energy_utility = 0
        energy_cost = 0
        utility = 0
    else:
        print("error")
    return latency_utility, energy_utility, energy_cost, energy_harvest, utility


def update_system(timeslot, devices, edges):
    global x_location_in_each_slot
    global y_location_in_each_slot

    # 更新系统
    # global uav_trans_rates
    for i in range(0, config.total_number_of_devices):
        if config.cache is True:
            devices[i].x = x_location_in_each_slot[timeslot][i]
            devices[i].y = y_location_in_each_slot[timeslot][i]
        else:
            devices[i].move()
            x_location_in_each_slot[timeslot][i] = devices[i].x
            y_location_in_each_slot[timeslot][i] = devices[i].y
    for i in range(0, config.total_number_of_devices):
        devices[i].get_the_distance(total_number_of_edges=config.total_number_of_edges, edges=edges)
        for j in range(0, config.total_number_of_edges):
            if edges[j].coverage_radius >= devices[i].distance_BS[j]:
                devices[i].locate_BS[j] = 1
                edges[j].coverage_mobile_device[i] = 1
            else:
                devices[i].locate_BS[j] = 0
                edges[j].coverage_mobile_device[i] = 0


def do_simulation():
    # 系统仿真
    global devices
    global edges
    global io_in_each_slot
    global ave_queue_length_in_each_slot
    global ave_execute_latency_in_each_slot
    global energy_consumption_in_each_slot
    global energy_harvest_in_each_slot
    global number_of_tasks_in_each_slot
    global latency_cost_in_each_slot
    global energy_cost_in_each_slot
    global total_cost_in_each_slot

    for time_slot in range(0, config.times):
        logging.error("%s / %s", time_slot, config.times)
        update_system(time_slot=time_slot, devices=devices, edges=edges)
        decisions = make_decision(time_slot=time_slot)
        device_compute_size = 0
        edge_compute_size = 0
        if time_slot > 0:
            for i in range(0, config.total_number_of_devices):
                device_compute_size += device_compute(device=devices[i])
            for i in range(0, config.total_number_of_edges):
                edge_compute_size = edge_compute_size + edge_compute(edge=edges[i])
        io = device_compute_size + edge_compute_size
        io_in_each_slot.append(io)
        total_latency_cost = 0
        total_energy_cost = 0
        total_energy_consumption = 0
        total_energy_harvest = 0
        total_cost = 0
        for j in range(0, config.total_number_of_devices):
            if config.algorithm != 'proposed_algorithm_v2':
                latency_cost, energy_cost, energy_consumption, energy_harvest, cost = execute_decision(device=devices[j], edges=edges, time_slot=time_slot, decisions=decisions)
            else:
                latency_cost, energy_cost, energy_consumption, energy_harvest, cost = execute_decision_v2(device=devices[j], edges=edges, time_slot=time_slot, decisions=decisions)
            total_latency_cost += latency_cost
            total_energy_cost += energy_cost
            total_energy_consumption += energy_consumption
            total_energy_harvest += energy_harvest
            total_cost += cost
        latency_cost_in_each_slot.append(total_latency_cost)
        ave_execute_latency = total_latency_cost / number_of_tasks_in_each_slot[time_slot]
        ave_execute_latency_in_each_slot.append(ave_execute_latency)
        energy_cost_in_each_slot.append(total_energy_cost)
        energy_consumption_in_each_slot.append(total_energy_consumption)
        energy_harvest_in_each_slot.append(total_energy_harvest)
        total_cost_in_each_slot.append(total_cost)
        sum_queue_length = 0
        for i in range(0, config.total_number_of_devices):
            sum_queue_length += devices[i].task_queue_length()
        # for i in range(0, config.total_number_of_edges):
        #     sum_queue_length += edges[i].task_queue_length()
        # ave_queue_length = sum_queue_length / (config.total_number_of_devices + config.total_number_of_edges)
        ave_queue_length = sum_queue_length / config.total_number_of_devices
        ave_queue_length_in_each_slot.append(ave_queue_length)


def print_result():
    # 输出结果
    global number_of_tasks_in_each_slot
    global io_in_each_slot
    global ave_queue_length_in_each_slot
    global ave_execute_latency_in_each_slot
    global latency_cost_in_each_slot
    global energy_cost_in_each_slot
    global energy_consumption_in_each_slot
    global total_cost_in_each_slot
    global local_ratio_in_each_slot
    global edge_ratio_in_each_slot
    global d2d_ratio_in_each_slot
    global x_location_in_each_slot
    global y_location_in_each_slot

    # path = config.res_cache_path + str(config.local_algorithm)
    # file = open(path, 'w+')
    # for item in queue_len_of_each_slot:
    #     file.write(str(item) + " ")
    # file.close()
    # 输出配置
    # logging.error(config.__dict__)  # 打印init里面的所有配置
    # 输出总成本
    # logging.error("传输总成本：%s", sum(trans_cost_in_each_slot))
    # logging.error("总成本：%s", sum(total_cost_in_each_slot))

    if config.algorithm == 'proposed_algorithm':
        for i in range(0, config.times):
            local_ratio_in_each_slot[i] = local_ratio_in_each_slot[i] / number_of_tasks_in_each_slot[i]
            edge_ratio_in_each_slot[i] = edge_ratio_in_each_slot[i] / number_of_tasks_in_each_slot[i]
            d2d_ratio_in_each_slot[i] = d2d_ratio_in_each_slot[i] / number_of_tasks_in_each_slot[i]

        local_ratio_in_each_slot_file_path = config.local_ratio_in_each_slot_file_path
        file = open(local_ratio_in_each_slot_file_path, 'w+')
        for item in local_ratio_in_each_slot:
            file.write(str(item) + " ")
        file.close()

        edge_ratio_in_each_slot_file_path = config.edge_ratio_in_each_slot_file_path
        file = open(edge_ratio_in_each_slot_file_path, 'w+')
        for item in edge_ratio_in_each_slot:
            file.write(str(item) + " ")
        file.close()

        d2d_ratio_in_each_slot_file_path = config.d2d_ratio_in_each_slot_file_path
        file = open(d2d_ratio_in_each_slot_file_path, 'w+')
        for item in d2d_ratio_in_each_slot:
            file.write(str(item) + " ")
        file.close()

    if config.cache is False:
        # 保存到文件中
        x_location_in_each_slot_file = open(config.x_location_in_each_slot_file_path, 'wb')
        pickle.dump(x_location_in_each_slot, x_location_in_each_slot_file)

        # 保存到文件中
        y_location_in_each_slot_file = open(config.y_location_in_each_slot_file_path, 'wb')
        pickle.dump(y_location_in_each_slot, y_location_in_each_slot_file)

    # to do
    # ave_queue_length_in_each_slot_path = config.local_ave_queue_length_in_each_slot_file_path
    # ave_queue_length_in_each_slot_path = config.nearest_ave_queue_length_in_each_slot_file_path
    # ave_queue_length_in_each_slot_path = config.random_ave_queue_length_in_each_slot_file_path
    # ave_queue_length_in_each_slot_path = config.match_ave_queue_length_in_each_slot_file_path
    ave_queue_length_in_each_slot_path = config.proposed_ave_queue_length_in_each_slot_file_path
    file = open(ave_queue_length_in_each_slot_path, 'w+')
    for item in ave_queue_length_in_each_slot:
        file.write(str(item) + " ")
    file.close()

    # to do
    # ave_execute_latency_in_each_slot_file_path = config.local_ave_execute_latency_in_each_slot_file_path
    # ave_execute_latency_in_each_slot_file_path = config.nearest_ave_execute_latency_in_each_slot_file_path
    # ave_execute_latency_in_each_slot_file_path = config.random_ave_execute_latency_in_each_slot_file_path
    # ave_execute_latency_in_each_slot_file_path = config.match_ave_execute_latency_in_each_slot_file_path
    ave_execute_latency_in_each_slot_file_path = config.proposed_ave_execute_latency_in_each_slot_file_path
    file = open(ave_execute_latency_in_each_slot_file_path, 'w+')
    for item in ave_execute_latency_in_each_slot:
        file.write(str(item) + " ")
    file.close()

    # to do
    # energy_consumption_in_each_slot_file_path = config.local_energy_consumption_in_each_slot_file_path
    # energy_consumption_in_each_slot_file_path = config.nearest_energy_consumption_in_each_slot_file_path
    # energy_consumption_in_each_slot_file_path = config.random_energy_consumption_in_each_slot_file_path
    # energy_consumption_in_each_slot_file_path = config.match_energy_consumption_in_each_slot_file_path
    energy_consumption_in_each_slot_file_path = config.proposed_energy_consumption_in_each_slot_file_path
    file = open(energy_consumption_in_each_slot_file_path, 'w+')
    for item in energy_consumption_in_each_slot:
        file.write(str(item) + " ")
    file.close()

    # to do
    # energy_harvest_in_each_slot_file_path = config.local_energy_harvest_in_each_slot_file_path
    # energy_harvest_in_each_slot_file_path = config.nearest_energy_harvest_in_each_slot_file_path
    # energy_harvest_in_each_slot_file_path = config.random_energy_harvest_in_each_slot_file_path
    # energy_harvest_in_each_slot_file_path = config.match_energy_harvest_in_each_slot_file_path
    energy_harvest_in_each_slot_file_path = config.proposed_energy_harvest_in_each_slot_file_path
    file = open(energy_harvest_in_each_slot_file_path, 'w+')
    for item in energy_harvest_in_each_slot:
        file.write(str(item) + " ")
    file.close()

    # to do
    # energy_cost_in_each_slot_file_path = config.local_energy_cost_in_each_slot_file_path
    # energy_cost_in_each_slot_file_path = config.nearest_energy_cost_in_each_slot_file_path
    # energy_cost_in_each_slot_file_path = config.random_energy_cost_in_each_slot_file_path
    # energy_cost_in_each_slot_file_path = config.match_energy_cost_in_each_slot_file_path
    energy_cost_in_each_slot_file_path = config.proposed_energy_cost_in_each_slot_file_path
    file = open(energy_cost_in_each_slot_file_path, 'w+')
    for item in energy_cost_in_each_slot:
        file.write(str(item) + " ")
    file.close()

    # to do
    # latency_cost_in_each_slot_file_path = config.local_latency_cost_in_each_slot_file_path
    # latency_cost_in_each_slot_file_path = config.nearest_latency_cost_in_each_slot_file_path
    # latency_cost_in_each_slot_file_path = config.random_latency_cost_in_each_slot_file_path
    # latency_cost_in_each_slot_file_path = config.match_latency_cost_in_each_slot_file_path
    latency_cost_in_each_slot_file_path = config.proposed_latency_cost_in_each_slot_file_path
    file = open(latency_cost_in_each_slot_file_path, 'w+')
    for item in latency_cost_in_each_slot:
        file.write(str(item) + " ")
    file.close()

    # to do
    # total_cost_in_each_slot_file_path = config.local_total_cost_in_each_slot_file_path
    # total_cost_in_each_slot_file_path = config.nearest_total_cost_in_each_slot_file_path
    # total_cost_in_each_slot_file_path = config.random_total_cost_in_each_slot_file_path
    # total_cost_in_each_slot_file_path = config.match_total_cost_in_each_slot_file_path
    total_cost_in_each_slot_file_path = config.proposed_total_cost_in_each_slot_file_path
    file = open(total_cost_in_each_slot_file_path, 'w+')
    for item in total_cost_in_each_slot:
        file.write(str(item) + " ")
    file.close()

    # to do
    # io_in_each_slot_file_path = config.local_io_in_each_slot_file_path
    # io_in_each_slot_file_path = config.nearest_io_in_each_slot_file_path
    # io_in_each_slot_file_path = config.random_io_in_each_slot_file_path
    # io_in_each_slot_file_path = config.match_io_in_each_slot_file_path
    io_in_each_slot_file_path = config.proposed_io_in_each_slot_file_path
    file = open(io_in_each_slot_file_path, 'w+')
    for item in io_in_each_slot:
        file.write(str(item) + " ")
    file.close()

    # 保存任务
    # if config.is_task_cache is False:
    #     task_cache_file = open(config.task_cache_file_path, 'wb')
    #     pickle.dump(task_in_each_slot, task_cache_file)


def start():
    init_edge_device()
    mock_load()
    do_simulation()
    print_result()


if __name__ == '__main__':
    start()

