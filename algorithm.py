import random
import matplotlib.pyplot as plt
import numpy
import math
from copy import deepcopy
from trans_rate import get_upload_rate, get_d2d_rate


def local_algorithm(decisions, config, time_slot, task_in_each_slot):
    for device_id in range(0, config.total_number_of_devices):
        if task_in_each_slot[time_slot][device_id] != 0:
            decisions.execute_mode.append('local')
            decisions.execute_destination.append(-1)
            decisions.local_computing_portion.append(1)
        elif task_in_each_slot[time_slot][device_id] == 0:
            decisions.execute_mode.append('null')
            decisions.execute_destination.append(-2)
            decisions.local_computing_portion.append(-1)
        else:
            print("error")
    return decisions


def nearest_bs_algorithm(decisions, config, devices, edges,time_slot, task_in_each_slot):
    for device_id in range(0, config.total_number_of_devices):
        if task_in_each_slot[time_slot][device_id] != 0:
            # 找最近的基站
            min_distance = 4000
            destination = -1
            for edge_id in range(0, config.total_number_of_edges):
                distance = devices[device_id].distance_BS[edge_id]
                if distance < min_distance:
                    min_distance = distance
                    destination = edge_id
            # 在基站的覆盖范围内
            if devices[device_id].locate_BS[destination] == 1:
                decisions.execute_mode.append('edge')
                decisions.execute_destination.append(destination)
            elif devices[device_id].locate_BS[destination] == 0:
                decisions.execute_mode.append('local')
                decisions.execute_destination.append(-1)
            else:
                print("error")
        elif task_in_each_slot[time_slot][device_id] == 0:
            decisions.execute_mode.append('null')
            decisions.execute_destination.append(-2)
        else:
            print("error")
    for device_id in range(0, config.total_number_of_devices):
        if decisions.execute_mode[device_id] == 'null':
            decisions.local_computing_portion.append(-1)
        elif decisions.execute_mode[device_id] == 'local':
            decisions.local_computing_portion.append(1)
        elif decisions.execute_mode[device_id] == 'edge':
            # 最大限度的卸载任务
            execute_destination = decisions.execute_destination[device_id]
            interference = 1
            for infer_device_id in range(0, config.total_number_of_devices):
                if infer_device_id != device_id and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_destination:
                    interference += 1
            upload_rate = get_upload_rate(device=devices[device_id], edge=edges[execute_destination], interference=interference)
            slot_upload_data_size = upload_rate * config.time_slot_length
            data_size = task_in_each_slot[time_slot][device_id].data_size
            upload_date_size_up_limit = min(slot_upload_data_size, data_size)
            offload_computing_portion = upload_date_size_up_limit / data_size
            local_computing_portion = 1.0 - offload_computing_portion
            # print('local_computing_portion=',local_computing_portion)
            decisions.local_computing_portion.append(local_computing_portion)
        else:
            print('error')
    return decisions


def random_algorithm(decisions, config, devices, edges, time_slot, task_in_each_slot):
    for device_id in range(0, config.total_number_of_devices):
        if task_in_each_slot[time_slot][device_id] != 0:
            rand = numpy.random.randint(1, 4)
            if rand == 1:
                decisions.execute_mode.append('local')
                decisions.execute_destination.append(-1)
            elif rand == 2:
                min_distance = 4000
                destination = -1
                for edge_id in range(0, config.total_number_of_edges):
                    distance = devices[device_id].distance_BS[edge_id]
                    if distance < min_distance:
                        min_distance = distance
                        destination = edge_id
                if devices[device_id].locate_BS[destination] == 1:
                    decisions.execute_mode.append('edge')
                    decisions.execute_destination.append(destination)
                elif devices[device_id].locate_BS[destination] == 0:
                    decisions.execute_mode.append('local')
                    decisions.execute_destination.append(-1)
                else:
                    pass
            elif rand == 3:
                choices = [0 for _ in range(0, config.total_number_of_devices)]
                for edge_id in range(0, config.total_number_of_edges):
                    if devices[device_id].locate_BS[edge_id] == 1:
                        for co_device_id in range(0, config.total_number_of_devices):
                            if edges[edge_id].coverage_mobile_device[co_device_id] == 1:
                                choices[co_device_id] = 1
                choices_number = 0
                for count_id in range(0, config.total_number_of_devices):
                    if choices[count_id] == 1:
                        choices_number = choices_number + 1
                if choices_number == 0:
                    # 不会走
                    decisions.execute_mode.append('local')
                    decisions.execute_destination.append(-1)
                elif choices_number > 0:
                    lucky_number = numpy.random.randint(1, choices_number + 1)
                    for co_device_id in range(0, config.total_number_of_devices):
                        if choices[co_device_id] == 1:
                            lucky_number = lucky_number - 1
                            if lucky_number == 0:
                                if device_id == co_device_id:
                                    decisions.execute_mode.append('local')
                                    decisions.execute_destination.append(-1)
                                elif device_id != co_device_id:
                                    decisions.execute_mode.append('device')
                                    decisions.execute_destination.append(co_device_id)
                                else:
                                    print('error')
                else:
                    print('error')
            else:
                print('error')
        elif task_in_each_slot[time_slot][device_id] == 0:
            decisions.execute_mode.append('null')
            decisions.execute_destination.append(-2)
        else:
            print("error")
    for device_id in range(0, config.total_number_of_devices):
        if decisions.execute_mode[device_id] == 'null':
            decisions.local_computing_portion.append(-1)
        elif decisions.execute_mode[device_id] == 'local':
            decisions.local_computing_portion.append(1)
        elif decisions.execute_mode[device_id] == 'edge':
            execute_destination = decisions.execute_destination[device_id]
            interference = 1
            for infer_device_id in range(0, config.total_number_of_devices):
                if infer_device_id != device_id and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_destination:
                    interference += 1
            upload_rate = get_upload_rate(device=devices[device_id], edge=edges[execute_destination], interference=interference)
            slot_upload_data_size = upload_rate * config.time_slot_length
            data_size = task_in_each_slot[time_slot][device_id].data_size
            upload_data_size_up_limit = min(slot_upload_data_size, data_size)
            offload_computing_portion_up_limit = upload_data_size_up_limit / data_size
            offload_computing_portion = random.uniform(0, offload_computing_portion_up_limit)
            local_computing_portion = 1.0 - offload_computing_portion
            # print('local_computing_portion=',local_computing_portion)
            decisions.local_computing_portion.append(local_computing_portion)
        elif decisions.execute_mode[device_id] == 'device':
            execute_destination = decisions.execute_destination[device_id]
            interference = 1
            for infer_device_id in range(0, config.total_number_of_devices):
                if infer_device_id != device_id and decisions.execute_mode[infer_device_id] == 'device' and decisions.execute_destination[infer_device_id] == execute_destination:
                    interference += 1
            d2d_rate = get_d2d_rate(device1=devices[device_id], device2=devices[execute_destination], interference=interference)
            slot_d2d_data_size = d2d_rate * config.time_slot_length
            data_size = task_in_each_slot[time_slot][device_id].data_size
            d2d_data_size_up_limit = min(slot_d2d_data_size, data_size)
            d2d_computing_portion_up_limit = d2d_data_size_up_limit / data_size
            offload_computing_portion = random.uniform(0, d2d_computing_portion_up_limit)
            local_computing_portion = 1.0 - offload_computing_portion
            # print('local_computing_portion=',local_computing_portion)
            decisions.local_computing_portion.append(local_computing_portion)
    return decisions


def binary_match_game(decisions, config, devices, edges, time_slot, task_in_each_slot):
    for device_id in range(config.total_number_of_devices):
        if task_in_each_slot[time_slot][device_id] != 0:
            # 遍历所有可以选择的决策，选择最优的决策。
            cost_flag = 10000000
            execute_mode = ''
            execute_destination = -2
            task = task_in_each_slot[time_slot][device_id]
            # 1. 本地计算决策
            # 本地计算大小
            local_compute_size = devices[device_id].task_queue_length() + task.cpu_frequency_demand
            # 本地执行延迟
            local_execute_latency = local_compute_size / devices[device_id].frequency
            local_latency_cost = local_execute_latency
            # 本地计算延迟
            local_computing_latency = task.cpu_frequency_demand / devices[device_id].frequency
            # 本地计算功率
            local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices[device_id].frequency, 3)
            # 本地计算能耗
            local_energy_consumption = local_computing_power * local_computing_latency
            # 收集能量
            min_distance = 4000
            destination = -1
            for har_edge_id in range(0, len(devices[device_id].distance_BS)):
                distance = devices[device_id].distance_BS[har_edge_id]
                if distance < min_distance:
                    min_distance = distance
                    destination = har_edge_id
            if devices[device_id].locate_BS[destination] == 1:
                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * config.time_slot_length
            else:
                energy_harvest = 0
            # 能量效用
            local_energy_cost = local_energy_consumption - energy_harvest
            # 获取权重
            latency_weight, energy_weight = devices[device_id].get_weight()
            # 本地计算总效用
            # total_local_cost = latency_weight * local_latency_cost + energy_weight * local_energy_cost
            # scale
            total_local_cost = latency_weight * local_latency_cost + 30 * energy_weight * local_energy_cost
            # 更新 flag
            if total_local_cost <= cost_flag:
                cost_flag = total_local_cost
                execute_mode = 'local'
                execute_destination = -1
            # 2. 边缘计算决策
            edges_execute_latency = [float("inf") for _ in range(config.total_number_of_edges)]
            edges_transmit_consumption = [0 for _ in range(config.total_number_of_edges)]
            for edge_id in range(0, config.total_number_of_edges):
                if devices[device_id].locate_BS[edge_id] == 1:
                    # 计算传输速率
                    interference = 1
                    upload_rate = get_upload_rate(devices[device_id], edges[edge_id], interference)
                    # 计算传输时间
                    edge_transmit_latency = task.data_size / upload_rate
                    # 计算传输能耗
                    edge_transmit_consumption = edge_transmit_latency * devices[device_id].offload_trans_power
                    edges_transmit_consumption[edge_id] = edge_transmit_consumption
                    # 收集能量
                    min_distance = 4000
                    destination = -1
                    for har_edge_id in range(0, len(devices[device_id].distance_BS)):
                        distance = devices[device_id].distance_BS[har_edge_id]
                        if distance < min_distance:
                            min_distance = distance
                            destination = har_edge_id
                    if devices[device_id].locate_BS[destination] == 1:
                        energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                        if edge_transmit_latency < config.time_slot_length:
                            energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
                        else:
                            energy_harvest_slot_length = 0
                        energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                    else:
                        energy_harvest = 0
                    # 边缘计算能量效用
                    edge_energy_cost = edge_transmit_consumption - energy_harvest
                    # 边缘计算数据大小
                    edge_compute_size = task.cpu_frequency_demand
                    # 边缘计算时间
                    edge_compute_latency = edge_compute_size / edges[edge_id].frequency
                    # 边缘执行延迟
                    edge_execute_latency = edge_transmit_latency + edge_compute_latency
                    edges_execute_latency[edge_id] = edge_execute_latency
                    edge_latency_cost = edge_execute_latency
                    # 获取权重
                    latency_weight, energy_weight = devices[device_id].get_weight()
                    # 边缘总效用
                    # total_edge_cost = energy_weight * edge_energy_cost + latency_weight * edge_latency_cost
                    # scale
                    total_edge_cost = 30 * energy_weight * edge_energy_cost + latency_weight * edge_latency_cost
                    # 更新 flag
                    if total_edge_cost <= cost_flag:
                        cost_flag = total_edge_cost
                        execute_mode = 'edge'
                        execute_destination = edge_id
            # 3. d2d计算决策
            d2ds_execute_latency = [float("inf") for _ in range(config.total_number_of_devices)]
            d2ds_transmit_consumption = [0 for _ in range(config.total_number_of_devices)]
            # 首先计算可以选择的决策
            choices = [0 for _ in range(0, config.total_number_of_devices)]
            for edge_id in range(0, config.total_number_of_edges):
                if devices[device_id].locate_BS[edge_id] == 1:
                    for co_device_id in range(0, config.total_number_of_devices):
                        if edges[edge_id].coverage_mobile_device[co_device_id] == 1:
                            choices[co_device_id] = 1
            for co_device_id in range(0, config.total_number_of_devices):
                # 如果设备 j 是一个可以选择的执行节点
                if choices[co_device_id] == 1 and co_device_id != device_id:
                    # 计算干扰
                    interference = 1
                    # 计算 d2d 传输速率
                    d2d_rate = get_d2d_rate(devices[device_id], devices[co_device_id], interference)
                    # 计算 d2d 传输延迟
                    d2d_transmit_latency = task.data_size / d2d_rate
                    # 传输能量消耗
                    d2d_trans_energy_consumption = d2d_transmit_latency * devices[device_id].d2d_trans_power
                    d2ds_transmit_consumption[co_device_id] = d2d_trans_energy_consumption
                    d2d_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices[co_device_id].frequency, 3)
                    d2d_computing_latency = task.cpu_frequency_demand / devices[co_device_id].frequency
                    d2d_computing_energy_consumption = d2d_computing_latency * d2d_computing_power
                    d2d_energy_consumption = d2d_trans_energy_consumption + d2d_computing_energy_consumption
                    # 收集能量
                    min_distance = 4000
                    destination = -1
                    for har_edge_id in range(0, len(devices[device_id].distance_BS)):
                        distance = devices[device_id].distance_BS[har_edge_id]
                        if distance < min_distance:
                            min_distance = distance
                            destination = har_edge_id
                    if devices[device_id].locate_BS[destination] == 1:
                        energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                        if config.time_slot_length > d2d_transmit_latency:
                            energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
                        else:
                            energy_harvest_slot_length = 0
                        energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                    else:
                        energy_harvest = 0
                    # d2d 能量效用
                    d2d_energy_cost = d2d_energy_consumption - energy_harvest
                    # d2d 计算大小
                    d2d_compute_size = devices[co_device_id].task_queue_length() + task.cpu_frequency_demand
                    # d2d 计算时间
                    d2d_compute_latency = d2d_compute_size / devices[co_device_id].frequency
                    # d2d 执行延迟
                    d2d_execute_latency = d2d_transmit_latency + d2d_compute_latency
                    d2ds_execute_latency[co_device_id] = d2d_execute_latency
                    d2d_latency_cost = d2d_execute_latency
                    # 获取权重
                    latency_weight, energy_weight = devices[device_id].get_weight()
                    # d2d 总效用
                    # total_d2d_cost = energy_weight * d2d_energy_cost + latency_weight * d2d_latency_cost
                    # scale
                    total_d2d_cost = 30 * energy_weight * d2d_energy_cost + latency_weight * d2d_latency_cost
                    # 更新 flag
                    if total_d2d_cost <= cost_flag:
                        cost_flag = total_d2d_cost
                        execute_mode = 'device'
                        execute_destination = co_device_id
                elif choices[co_device_id] == 1 and co_device_id == device_id:
                    pass
                elif choices[co_device_id] == 0:
                    pass
                else:
                    print('error_334')
            decisions.execute_mode.append(execute_mode)
            decisions.execute_destination.append(execute_destination)
        elif task_in_each_slot[time_slot][device_id] == 0:
            decisions.execute_mode.append('null')
            decisions.execute_destination.append(-2)
        else:
            print('error_341')
    for device_id in range(0, config.total_number_of_devices):
        if decisions.execute_mode[device_id] == 'null':
            decisions.local_computing_portion.append(-1)
        elif decisions.execute_mode[device_id] == 'local':
            decisions.local_computing_portion.append(1)
        elif decisions.execute_mode[device_id] == 'edge':
            execute_destination = decisions.execute_destination[device_id]
            interference = 1
            for infer_device_id in range(0, config.total_number_of_devices):
                if infer_device_id != device_id and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_destination:
                    interference += 1
            upload_rate = get_upload_rate(device=devices[device_id], edge=edges[execute_destination], interference=interference)
            slot_upload_data_size = upload_rate * config.time_slot_length
            data_size = task_in_each_slot[time_slot][device_id].data_size
            upload_data_size_up_limit = min(slot_upload_data_size, data_size)
            offload_computing_portion_up_limit = upload_data_size_up_limit / data_size
            local_computing_portion = 1.0 - offload_computing_portion_up_limit
            # print('local_computing_portion=',local_computing_portion)
            decisions.local_computing_portion.append(local_computing_portion)
        elif decisions.execute_mode[device_id] == 'device':
            execute_destination = decisions.execute_destination[device_id]
            interference = 1
            for infer_device_id in range(0, config.total_number_of_devices):
                if infer_device_id != device_id and decisions.execute_mode[infer_device_id] == 'device' and decisions.execute_destination[infer_device_id] == execute_destination:
                    interference += 1
            d2d_rate = get_d2d_rate(device1=devices[device_id], device2=devices[execute_destination], interference=interference)
            slot_d2d_data_size = d2d_rate * config.time_slot_length
            data_size = task_in_each_slot[time_slot][device_id].data_size
            d2d_data_size_up_limit = min(slot_d2d_data_size, data_size)
            d2d_computing_portion_up_limit = d2d_data_size_up_limit / data_size
            local_computing_portion = 1.0 - d2d_computing_portion_up_limit
            # print('local_computing_portion=',local_computing_portion)
            decisions.local_computing_portion.append(local_computing_portion)
    return decisions


def dot_game(decisions, config, devices, edges, time_slot, task_in_each_slot):
    for device_id in range(0, config.total_number_of_devices):
        if task_in_each_slot[time_slot][device_id] != 0:
            rand = numpy.random.randint(1, 3)
            if rand == 1:
                decisions.execute_mode.append('local')
                decisions.execute_destination.append(-1)
            elif rand == 2:
                min_distance = 4000
                destination = -1
                for edge_id in range(0, config.total_number_of_edges):
                    distance = devices[device_id].distance_BS[edge_id]
                    if distance < min_distance:
                        min_distance = distance
                        destination = edge_id
                if devices[device_id].locate_BS[destination] == 1:
                    decisions.execute_mode.append('edge')
                    decisions.execute_destination.append(destination)
                elif devices[device_id].locate_BS[destination] == 0:
                    decisions.execute_mode.append('local')
                    decisions.execute_destination.append(-1)
                else:
                    print('error')
            else:
                print('error')
        elif task_in_each_slot[time_slot][device_id] == 0:
            decisions.execute_mode.append('null')
            decisions.execute_destination.append(-2)
        else:
            print("error")
    for device_id in range(0, config.total_number_of_devices):
        if decisions.execute_mode[device_id] == 'null':
            decisions.local_computing_portion.append(-1)
        elif decisions.execute_mode[device_id] == 'local':
            decisions.local_computing_portion.append(1)
        elif decisions.execute_mode[device_id] == 'edge':
            execute_destination = decisions.execute_destination[device_id]
            interference = 1
            for infer_device_id in range(0, config.total_number_of_devices):
                if infer_device_id != device_id and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_destination:
                    interference += 1
            upload_rate = get_upload_rate(device=devices[device_id], edge=edges[execute_destination], interference=interference)
            slot_upload_data_size = upload_rate * config.time_slot_length
            data_size = task_in_each_slot[time_slot][device_id].data_size
            upload_data_size_up_limit = min(slot_upload_data_size, data_size)
            offload_computing_portion_up_limit = upload_data_size_up_limit / data_size
            offload_computing_portion = offload_computing_portion_up_limit
            local_computing_portion = 1.0 - offload_computing_portion
            # print('local_computing_portion=',local_computing_portion)
            decisions.local_computing_portion.append(local_computing_portion)
    flag = 0
    for _ in range(0, config.iterations_number_of_game_theory):
        # 随机选择一个移动设备更新其决策
        lucky_user = numpy.random.randint(0, config.total_number_of_devices)
        while decisions.execute_mode[lucky_user] == 'null':
            lucky_user = numpy.random.randint(0, config.total_number_of_devices)
        if decisions.execute_mode[lucky_user] != 'null':
            # 除选择的移动设备外其他移动设备执行决策
            devices_temp = deepcopy(devices)
            edges_temp = deepcopy(edges)
            for previous_device_id in range(0, lucky_user):
                if previous_device_id != lucky_user:
                    if decisions.execute_mode[previous_device_id] == 'local':
                        cpu_frequency_demand = task_in_each_slot[time_slot][previous_device_id].cpu_frequency_demand
                        devices_temp[previous_device_id].task_enqueue(cpu_frequency_demand)
                    elif decisions.execute_mode[previous_device_id] == 'edge':
                        execute_destination = decisions.execute_destination[previous_device_id]
                        data_size = task_in_each_slot[time_slot][previous_device_id].data_size
                        local_computing_portion = decisions.local_computing_portion[previous_device_id]
                        edge_computing_portion = 1 - local_computing_portion
                        offload_data_size = data_size * edge_computing_portion
                        # 计算传输速率
                        interference = 1
                        for infer_device_id in range(0, config.total_number_of_devices):
                            if infer_device_id != previous_device_id and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_destination:
                                interference += 1
                        upload_rate = get_upload_rate(device=devices_temp[previous_device_id], edge=edges_temp[execute_destination],
                                                      interference=interference)
                        # 传输时间
                        edge_transmit_latency = offload_data_size / upload_rate
                        edge_transmit_latency = round(edge_transmit_latency, 6)
                        # 修正边缘传输延迟
                        if edge_transmit_latency >= config.time_slot_length:
                            edge_transmit_latency = config.time_slot_length
                        edge_transmit_data_size = edge_transmit_latency * upload_rate
                        local_computing_data_size = data_size - edge_transmit_data_size
                        # 修正本地计算比例
                        if edge_transmit_latency == config.time_slot_length:
                            decisions.local_computing_portion[previous_device_id] = local_computing_data_size / data_size
                        local_computing_cpu_frequency_demand = local_computing_data_size * config.task_cpu_frequency_demand
                        devices_temp[previous_device_id].task_enqueue(local_computing_cpu_frequency_demand)
                else:
                    print('error')
            # 遍历所有可以选择的决策，选择最优的决策。
            cost_flag = 10000000
            iteration_execute_mode = ''
            iteration_execute_destination = -2
            iteration_local_computing_portion = -1
            task = task_in_each_slot[time_slot][lucky_user]
            # 1. 本地计算决策
            # 本地计算大小
            local_compute_size = devices_temp[lucky_user].task_queue_length() + task.cpu_frequency_demand
            # 本地执行延迟
            local_execute_latency = local_compute_size / devices_temp[lucky_user].frequency
            local_latency_cost = local_execute_latency
            # 本地计算延迟
            local_computing_latency = task.cpu_frequency_demand / devices_temp[lucky_user].frequency
            # 本地计算功率
            local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
            # 本地计算能耗
            local_energy_consumption = local_computing_power * local_computing_latency
            # 收集能量
            min_distance = 4000
            destination = -1
            for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                if distance < min_distance:
                    min_distance = distance
                    destination = har_edge_id
            if devices_temp[lucky_user].locate_BS[destination] == 1:
                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
            else:
                energy_harvest = 0
            # 能量效用
            local_energy_cost = local_energy_consumption - energy_harvest
            # 获取权重
            latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
            # 本地计算总效用
            # total_local_cost = latency_weight * local_latency_cost + energy_weight * local_energy_cost
            # scale
            total_local_cost = latency_weight * local_latency_cost + 30 * energy_weight * local_energy_cost
            # 更新 flag
            if total_local_cost <= cost_flag:
                cost_flag = total_local_cost
                iteration_execute_mode = 'local'
                iteration_execute_destination = -1
                iteration_local_computing_portion = 1
            # 2. 边缘计算决策
            edges_execute_latency = [float("inf") for _ in range(config.total_number_of_edges)]
            edges_transmit_consumption = [0 for _ in range(config.total_number_of_edges)]
            for edge_id in range(0, config.total_number_of_edges):
                if devices_temp[lucky_user].locate_BS[edge_id] == 1:
                    # 计算传输速率
                    interference = 1
                    for infer_device_id in range(0, config.total_number_of_devices):
                        if infer_device_id != lucky_user and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == edge_id:
                            interference += 1
                    upload_rate = get_upload_rate(device=devices_temp[lucky_user], edge=edges_temp[edge_id], interference=interference)
                    slot_upload_data_size = upload_rate * config.time_slot_length
                    data_size = task_in_each_slot[time_slot][lucky_user].data_size
                    upload_data_size_up_limit = min(slot_upload_data_size, data_size)
                    offload_computing_portion_up_limit = upload_data_size_up_limit / data_size
                    offload_computing_portion = offload_computing_portion_up_limit
                    local_computing_portion = 1.0 - offload_computing_portion
                    if offload_computing_portion > 0:
                        offload_data_size = data_size * offload_computing_portion
                        edge_transmit_latency = offload_data_size / upload_rate
                        edge_transmit_latency = round(edge_transmit_latency, 6)
                        # print('edge_transmit_latency=', edge_transmit_latency)
                        if edge_transmit_latency >= config.time_slot_length:
                            edge_transmit_latency = config.time_slot_length
                        # print('real_edge_transmit_latency=', edge_transmit_latency)
                        # 传输能耗
                        trans_energy_consumption = edge_transmit_latency * devices_temp[lucky_user].offload_trans_power
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
                    for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                        distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                        if distance < min_distance:
                            min_distance = distance
                            destination = har_edge_id
                    if devices_temp[lucky_user].locate_BS[destination] == 1:
                        energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                        energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
                        print('energy harvest slot length =', energy_harvest_slot_length)
                        energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
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
                            local_computing_cpu_demand = task.cpu_frequency_demand * local_computing_portion
                        # 队列长度
                        queue_length = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
                        # 本地计算时间
                        local_execute_latency = queue_length / devices_temp[lucky_user].frequency
                        # 本地计算能耗
                        local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                        local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
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
                    # 能量效用
                    energy_cost = energy_consumption - energy_harvest
                    # 边缘计算执行时间
                    if offload_computing_portion > 0:
                        offload_computing_cpu_demand = task.cpu_frequency_demand - local_computing_cpu_demand
                        interference_number = 1
                        for infer_device_id in range(0, config.total_number_of_devices):
                            if infer_device_id != lucky_user and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == edge_id:
                                interference_number += 1
                        actual_frequency = edges_temp[edge_id].frequency / interference_number
                        edge_compute_task_latency = offload_computing_cpu_demand / actual_frequency
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
                    total_edge_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                    if total_edge_cost <= cost_flag:
                        cost_flag = total_edge_cost
                        iteration_execute_mode = 'edge'
                        iteration_execute_destination = edge_id
                        iteration_local_computing_portion = local_computing_portion
            if decisions.execute_mode[lucky_user] == iteration_execute_mode and decisions.execute_destination[lucky_user] == iteration_execute_destination:
                flag = flag + 1
            else:
                flag = 0
            if flag >= 50:
                break
            decisions.execute_mode[lucky_user] = iteration_execute_mode
            decisions.execute_destination[lucky_user] = iteration_execute_destination
            decisions.local_computing_portion[lucky_user] = iteration_local_computing_portion
        elif decisions.execute_mode[lucky_user] == 'null':
            pass
        else:
            print('error6')
    return decisions


def proposed_algorithm(decisions, config, devices, edges, time_slot, task_in_each_slot):
    decisions = random_algorithm(decisions, config, devices, edges, time_slot, task_in_each_slot)
    for _ in range(0, config.iterations_number_of_game_theory):
        lucky_user = numpy.random.randint(0, config.total_number_of_devices)
        # 选出生成任务的幸运用户
        while decisions.execute_mode[lucky_user] == 'null':
            lucky_user = numpy.random.randint(0, config.total_number_of_devices)
        if decisions.execute_mode[lucky_user] != 'null':
            devices_temp = deepcopy(devices)
            edges_temp = deepcopy(edges)
            for previous_device_id in range(0, lucky_user):
                if decisions.execute_mode[previous_device_id] == 'local':
                    cpu_frequency_demand = task_in_each_slot[time_slot][previous_device_id].cpu_frequency_demand
                    devices_temp[previous_device_id].task_enqueue(cpu_frequency_demand)
                elif decisions.execute_mode[previous_device_id] == 'edge':
                    execute_destination = decisions.execute_destination[previous_device_id]
                    data_size = task_in_each_slot[time_slot][previous_device_id].data_size
                    local_computing_portion = decisions.local_computing_portion[previous_device_id]
                    edge_computing_portion = 1 - local_computing_portion
                    offload_data_size = data_size * edge_computing_portion
                    # 计算传输速率
                    interference = 1
                    for infer_device_id in range(0, config.total_number_of_devices):
                        if infer_device_id != previous_device_id and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_destination:
                            interference += 1
                    upload_rate = get_upload_rate(device=devices_temp[previous_device_id], edge=edges_temp[execute_destination], interference=interference)
                    # 传输时间
                    edge_transmit_latency = offload_data_size / upload_rate
                    edge_transmit_latency = round(edge_transmit_latency, 6)
                    # 修正边缘传输延迟
                    if edge_transmit_latency >= config.time_slot_length:
                        edge_transmit_latency = config.time_slot_length
                    edge_transmit_data_size = edge_transmit_latency * upload_rate
                    local_computing_data_size = data_size - edge_transmit_data_size
                    # 修正本地计算比例
                    if edge_transmit_latency == config.time_slot_length:
                        decisions.local_computing_portion[previous_device_id] = local_computing_data_size / data_size
                    local_computing_cpu_frequency_demand = local_computing_data_size * config.task_cpu_frequency_demand
                    devices_temp[previous_device_id].task_enqueue(local_computing_cpu_frequency_demand)
                elif decisions.execute_mode[previous_device_id] == 'device':
                    execute_destination = decisions.execute_destination[previous_device_id]
                    data_size = task_in_each_slot[time_slot][previous_device_id].data_size
                    local_computing_portion = decisions.local_computing_portion[previous_device_id]
                    d2d_computing_portion = 1 - local_computing_portion
                    d2d_data_size = data_size * d2d_computing_portion
                    # 计算传输速率
                    interference = 1
                    for infer_device_id in range(0, config.total_number_of_devices):
                        if infer_device_id != previous_device_id and decisions.execute_mode[infer_device_id] == 'device' and decisions.execute_destination[infer_device_id] == execute_destination:
                            interference += 1
                    d2d_rate = get_d2d_rate(device1=devices_temp[previous_device_id], device2=devices_temp[execute_destination], interference=interference)
                    # 传输时间
                    d2d_transmit_latency = d2d_data_size / d2d_rate
                    d2d_transmit_latency = round(d2d_transmit_latency, 6)
                    if d2d_transmit_latency >= config.time_slot_length:
                        d2d_transmit_latency = config.time_slot_length
                    d2d_transmit_data_size = d2d_transmit_latency * d2d_rate
                    d2d_transmit_cpu_frequency_demand = d2d_transmit_data_size * config.task_cpu_frequency_demand
                    devices_temp[execute_destination].task_enqueue(d2d_transmit_cpu_frequency_demand)
                    local_computing_data_size = data_size - d2d_transmit_data_size
                    if d2d_transmit_latency == config.time_slot_length:
                        decisions.local_computing_portion[previous_device_id] = local_computing_data_size / data_size
                    local_computing_cpu_frequency_demand = local_computing_data_size * config.task_cpu_frequency_demand
                    devices_temp[previous_device_id].task_enqueue(local_computing_cpu_frequency_demand)
            task = task_in_each_slot[time_slot][lucky_user]
            data_size = task_in_each_slot[time_slot][lucky_user].data_size
            cpu_frequency_demand = task_in_each_slot[time_slot][lucky_user].cpu_frequency_demand
            # 计算上一轮的效用
            last_total_cost = 0
            if decisions.execute_mode[lucky_user] == 'local':
                local_computing_size = devices_temp[lucky_user].task_queue_length() + cpu_frequency_demand
                local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                latency_cost = local_execute_latency
                # 本地计算能耗
                local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                local_computing_latency = cpu_frequency_demand / devices_temp[lucky_user].frequency
                energy_consumption = local_computing_latency * local_computing_power
                # 收集能量
                min_distance = 4000
                destination = -1
                for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                    distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                    if distance < min_distance:
                        min_distance = distance
                        destination = har_edge_id
                if devices_temp[lucky_user].locate_BS[destination] == 1:
                    energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                    energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
                else:
                    energy_harvest = 0
                # 能量效用
                energy_cost = energy_consumption - energy_harvest
                # 获取权重
                latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                # 总效用
                # total_local_cost = latency_weight * latency_cost + energy_weight * energy_cost
                # scale
                total_local_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                last_total_cost = total_local_cost
            elif decisions.execute_mode[lucky_user] == 'edge':
                execute_edge_id = decisions.execute_destination[lucky_user]
                local_computing_portion = decisions.local_computing_portion[lucky_user]
                execute_edge = edges_temp[execute_edge_id]
                # 计算卸载数据大小
                offload_computing_portion = (1 - local_computing_portion)
                # print('offload_computing_portion', offload_computing_portion)
                if offload_computing_portion > 0:
                    offload_data_size = data_size * offload_computing_portion
                    # 计算传输速率
                    interference = 1
                    for infer_device_id in range(0, config.total_number_of_devices):
                        if infer_device_id != lucky_user and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_edge_id:
                            interference += 1
                    upload_rate = get_upload_rate(device=devices_temp[lucky_user], edge=execute_edge, interference=interference)
                    # 传输时间
                    edge_transmit_latency = offload_data_size / upload_rate
                    edge_transmit_latency = round(edge_transmit_latency, 6)
                    if edge_transmit_latency >= config.time_slot_length:
                        edge_transmit_latency = config.time_slot_length
                    # 传输能耗
                    trans_energy_consumption = edge_transmit_latency * devices_temp[lucky_user].offload_trans_power
                elif offload_computing_portion == 0:
                    # 传输时间
                    edge_transmit_latency = 0
                    # 传输能耗
                    trans_energy_consumption = 0
                else:
                    print('error')
                # 收集能量
                min_distance = 4000
                destination = -1
                for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                    distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                    if distance < min_distance:
                        min_distance = distance
                        destination = har_edge_id
                if devices_temp[lucky_user].locate_BS[destination] == 1:
                    energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                    energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
                    # print('energy harvest slot length =', energy_harvest_slot_length)
                    energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                    # print('energy harvest ', energy_harvest)
                else:
                    energy_harvest = 0
                # 本地计算时间
                if local_computing_portion > 0:
                    if edge_transmit_latency == config.time_slot_length:
                        edge_transmit_data_size = upload_rate * config.time_slot_length
                        local_computing_data_size = data_size - edge_transmit_data_size
                        decisions.local_computing_portion[lucky_user] = local_computing_data_size / data_size
                        local_computing_cpu_demand = local_computing_data_size * config.task_cpu_frequency_demand
                    else:
                        local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                    local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
                    # 本地计算时间
                    local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                    # 本地计算能耗
                    local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                    local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
                    local_computing_energy_consumption = local_computing_latency * local_computing_power
                elif local_computing_portion == 0:
                    local_computing_cpu_demand = 0
                    local_execute_latency = 0
                    local_computing_energy_consumption = 0
                else:
                    print('error')
                # 能量消耗
                energy_consumption = local_computing_energy_consumption + trans_energy_consumption
                # 能量效用
                energy_cost = energy_consumption - energy_harvest
                # print(energy_cost)
                # 边缘计算执行时间
                if offload_computing_portion > 0:
                    offload_computing_cpu_demand = cpu_frequency_demand - local_computing_cpu_demand
                    interference_number = 1
                    for infer_device_id in range(0, config.total_number_of_devices):
                        if infer_device_id != lucky_user and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_edge_id:
                            interference_number += 1
                    actual_frequency = edges_temp[execute_edge_id].frequency / interference_number
                    edge_computing_task_latency = offload_computing_cpu_demand / actual_frequency
                elif offload_computing_portion == 0:
                    edge_computing_task_latency = 0
                else:
                    print('error')
                edge_execute_latency = edge_transmit_latency + edge_computing_task_latency
                # 延迟效用
                latency_cost = max(local_execute_latency, edge_execute_latency)
                # print('energy queue', devices_temp[lucky_user].energy_queue)
                # 获取权重
                latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                # 总效用
                # total_edge_cost = latency_weight * latency_cost + energy_weight * energy_cost
                # scale
                total_edge_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                last_total_cost = total_edge_cost
            elif decisions.execute_mode[lucky_user] == 'device':
                execute_device_id = decisions.execute_destination[lucky_user]
                local_computing_portion = decisions.local_computing_portion[lucky_user]
                execute_device = devices_temp[execute_device_id]
                # 计算卸载数据大小
                offload_computing_portion = (1 - local_computing_portion)
                if offload_computing_portion > 0:
                    offload_data_size = data_size * offload_computing_portion
                    # 计算传输速率
                    interference = 1
                    for infer_device_id in range(0, config.total_number_of_devices):
                        if infer_device_id != lucky_user and decisions.execute_mode[infer_device_id] == 'device' and decisions.execute_destination[infer_device_id] == execute_device_id:
                            interference += 1
                    d2d_rate = get_d2d_rate(device1=devices_temp[lucky_user], device2=execute_device, interference=interference)
                    # 传输时间
                    d2d_transmit_latency = offload_data_size / d2d_rate
                    d2d_transmit_latency = round(d2d_transmit_latency, 6)
                    if d2d_transmit_latency >= config.time_slot_length:
                        d2d_transmit_latency = config.time_slot_length
                    # 传输能耗
                    trans_energy_consumption = d2d_transmit_latency * devices_temp[lucky_user].d2d_trans_power
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
                    print('error')
                # 收集能量
                min_distance = 4000
                destination = -1
                for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                    distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                    if distance < min_distance:
                        min_distance = distance
                        destination = har_edge_id
                if devices_temp[lucky_user].locate_BS[destination] == 1:
                    energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                    energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
                    energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                else:
                    energy_harvest = 0
                # 本地计算时间
                if local_computing_portion > 0:
                    if d2d_transmit_latency == config.time_slot_length:
                        d2d_transmit_data_size = d2d_rate * config.time_slot_length
                        local_computing_data_size = data_size - d2d_transmit_data_size
                        decisions.local_computing_portion[lucky_user] = local_computing_data_size / data_size
                        local_computing_cpu_demand = local_computing_data_size * config.task_cpu_frequency_demand
                    else:
                        local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                    local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
                    # 本地计算时间
                    local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                    # 本地计算能耗
                    local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                    local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
                    local_computing_energy_consumption = local_computing_latency * local_computing_power
                elif local_computing_portion == 0:
                    local_computing_cpu_demand = 0
                    local_execute_latency = 0
                    local_computing_energy_consumption = 0
                else:
                    print('error')
                # 能量消耗
                energy_consumption = local_computing_energy_consumption + total_trans_energy_consumption
                # 能量效用
                energy_cost = energy_consumption - energy_harvest
                # 边缘计算执行时间
                if offload_computing_portion > 0:
                    offload_computing_cpu_demand = cpu_frequency_demand - local_computing_cpu_demand
                    d2d_queue_length = execute_device.task_queue_length() + offload_computing_cpu_demand
                    d2d_compute_task_latency = d2d_queue_length / execute_device.frequency
                elif offload_computing_portion == 0:
                    d2d_compute_task_latency = 0
                else:
                    print('error')
                d2d_execute_latency = d2d_transmit_latency + d2d_compute_task_latency
                # 延迟效用
                latency_cost = max(local_execute_latency, d2d_execute_latency)
                # 获取权重
                latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                # 总效用
                # total_d2d_cost = latency_weight * latency_cost + energy_weight * energy_cost
                # scale
                total_d2d_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                last_total_cost = total_d2d_cost
            # this interation
            rand = numpy.random.randint(1, 4)
            if rand == 1:
                local_computing_size = devices_temp[lucky_user].task_queue_length() + cpu_frequency_demand
                local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                latency_cost = local_execute_latency
                # 本地计算能耗
                local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                local_computing_latency = cpu_frequency_demand / devices_temp[lucky_user].frequency
                energy_consumption = local_computing_latency * local_computing_power
                # 收集能量
                min_distance = 4000
                destination = -1
                for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                    distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                    if distance < min_distance:
                        min_distance = distance
                        destination = har_edge_id
                if devices_temp[lucky_user].locate_BS[destination] == 1:
                    energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                    energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
                    # print('energy_harvest', energy_harvest)
                else:
                    energy_harvest = 0
                # 能量效用
                energy_cost = energy_consumption - energy_harvest
                # 获取权重
                latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                # 总效用
                # total_local_cost = latency_weight * latency_cost + energy_weight * energy_cost
                # scale
                total_local_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                this_total_cost = total_local_cost
                if this_total_cost <= last_total_cost:
                    decisions.execute_mode[lucky_user] = 'local'
                    decisions.execute_destination[lucky_user] = -1
                    decisions.local_computing_portion[lucky_user] = 1
            elif rand == 2:
                # 随机选动作
                choices_number = 0
                for edge_id in range(0, config.total_number_of_edges):
                    if devices_temp[lucky_user].locate_BS[edge_id] == 1:
                        choices_number = choices_number + 1
                if choices_number == 0:
                    execute_mode = 'local'
                    execute_destination = -1
                elif choices_number > 0:
                    lucky_number = numpy.random.randint(1, choices_number + 1)
                    for edge_id in range(0, config.total_number_of_edges):
                        if devices_temp[lucky_user].locate_BS[edge_id] == 1:
                            lucky_number = lucky_number - 1
                            if lucky_number == 0:
                                execute_mode = 'edge'
                                execute_destination = edge_id
                # 计算效用
                if execute_mode == 'local':
                    local_computing_size = devices_temp[lucky_user].task_queue_length() + cpu_frequency_demand
                    local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                    latency_cost = local_execute_latency
                    # 本地计算能耗
                    local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency,3)
                    local_computing_latency = cpu_frequency_demand / devices_temp[lucky_user].frequency
                    energy_consumption = local_computing_latency * local_computing_power
                    # 收集能量
                    min_distance = 4000
                    destination = -1
                    for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                        distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                        if distance < min_distance:
                            min_distance = distance
                            destination = har_edge_id
                    if devices_temp[lucky_user].locate_BS[destination] == 1:
                        energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                        energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
                        # print('energy_harvest', energy_harvest)
                    else:
                        energy_harvest = 0
                    # 能量效用
                    energy_cost = energy_consumption - energy_harvest
                    # 获取权重
                    latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                    # 总效用
                    # total_local_cost = latency_weight * latency_cost + energy_weight * energy_cost
                    # scale
                    total_local_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                    this_total_cost = total_local_cost
                    if this_total_cost <= last_total_cost:
                        decisions.execute_mode[lucky_user] = 'local'
                        decisions.execute_destination[lucky_user] = -1
                        decisions.local_computing_portion[lucky_user] = 1
                elif execute_mode == 'edge':
                    execute_edge_id = execute_destination
                    execute_edge = edges_temp[execute_edge_id]
                    interference = 1
                    for infer_device_id in range(0, config.total_number_of_devices):
                        if infer_device_id != lucky_user and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_edge_id:
                            interference += 1
                    upload_rate = get_upload_rate(device=devices_temp[lucky_user], edge=execute_edge, interference=interference)
                    slot_upload_data_size = upload_rate * config.time_slot_length
                    slot_upload_data_size = round(slot_upload_data_size, 6)
                    offload_data_size_up_limit = min(slot_upload_data_size, data_size)
                    offload_computing_portion_up_limit = offload_data_size_up_limit / data_size
                    offload_computing_portion_up_limit = round(offload_computing_portion_up_limit, 6)
                    X = numpy.random.uniform(low=0, high=offload_computing_portion_up_limit, size=config.pop_size)
                    X[0] = 0
                    X[1] = offload_computing_portion_up_limit
                    Y = [0 for _ in range(len(X))]
                    for x in range(len(X)):
                        offload_computing_portion = X[x]
                        if offload_computing_portion > 0:
                            offload_data_size = data_size * offload_computing_portion
                            # 传输时间
                            edge_transmit_latency = offload_data_size / upload_rate
                            edge_transmit_latency = round(edge_transmit_latency, 6)
                            # print('edge_transmit_latency', edge_transmit_latency)
                            # 传输能耗
                            trans_energy_consumption = edge_transmit_latency * devices_temp[lucky_user].offload_trans_power
                        elif offload_computing_portion == 0:
                            # 传输时间
                            edge_transmit_latency = 0
                            # 传输能耗
                            trans_energy_consumption = 0
                        else:
                            print('error')
                        # 收集能量
                        min_distance = 4000
                        destination = -1
                        for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                            distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                            if distance < min_distance:
                                min_distance = distance
                                destination = har_edge_id
                        if devices_temp[lucky_user].locate_BS[destination] == 1:
                            energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                            energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
                            # print('energy harvest slot length =', energy_harvest_slot_length)
                            energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                            # print('energy harvest =', energy_harvest)
                        else:
                            energy_harvest = 0
                        # 本地计算时间
                        local_computing_portion = 1 - offload_computing_portion
                        if local_computing_portion > 0:
                            local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                            local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
                            # 本地计算时间
                            local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                            # 本地计算能耗
                            local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                            local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
                            local_computing_energy_consumption = local_computing_latency * local_computing_power
                        elif local_computing_portion == 0:
                            local_execute_latency = 0
                            local_computing_energy_consumption = 0
                        else:
                            print('error')
                        # 能量消耗
                        energy_consumption = local_computing_energy_consumption + trans_energy_consumption
                        # 能量效用
                        energy_cost = energy_consumption - energy_harvest
                        # print(energy_cost)
                        # 边缘计算执行时间
                        if offload_computing_portion > 0:
                            offload_computing_cpu_demand = cpu_frequency_demand * offload_computing_portion
                            interference_number = 1
                            for infer_device_id in range(0, config.total_number_of_devices):
                                if infer_device_id != lucky_user and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_edge_id:
                                    interference_number += 1
                            actual_frequency = edges_temp[execute_edge_id].frequency / interference_number
                            edge_computing_task_latency = offload_computing_cpu_demand / actual_frequency
                        elif offload_computing_portion == 0:
                            edge_computing_task_latency = 0
                        else:
                            print('error')
                        edge_execute_latency = edge_transmit_latency + edge_computing_task_latency
                        # 延迟效用
                        latency_cost = max(local_execute_latency, edge_execute_latency)
                        # 获取权重
                        latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                        # 总效用
                        # total_edge_cost = latency_weight * latency_cost + energy_weight * energy_cost
                        # scale
                        total_edge_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                        #
                        Y[x] = total_edge_cost
                    pbest_x = X.copy()  # personal best location of every particle in history
                    # self.pbest_x = self.X 表示地址传递,改变 X 值 pbest_x 也会变化
                    pbest_y = [numpy.inf for _ in range(config.pop_size)]  # best image of every particle in history
                    # self.gbest_x = self.pbest_x.mean(axis=0).reshape(1, -1)  # global best location for all particles
                    gbest_x = pbest_x.mean(axis=0)
                    gbest_y = numpy.inf  # global best y for all particles
                    gbest_y_hist = []  # gbest_y of every iteration
                    for this_iter in range(config.max_iter):
                        # # update
                        # r1 = config.a - this_iter * (config.a / config.max_iter)
                        # 抛物线函数
                        iter_period = this_iter / config.max_iter
                        inter_rest_phase = 1 - iter_period
                        square = pow(inter_rest_phase, 2)
                        r1 = config.a * square
                        for pop in range(config.pop_size):
                            r2 = 2 * math.pi * random.uniform(0.0, 1.0)
                            r3 = 2 * random.uniform(0.0, 1.0)
                            r4 = random.uniform(0.0, 1.0)
                            if r4 < 0.5:
                                X[pop] = X[pop] + (r1 * math.sin(r2) * abs(r3 * gbest_x - X[pop]))
                            else:
                                X[pop] = X[pop] + (r1 * math.cos(r2) * abs(r3 * gbest_x - X[pop]))
                        X = numpy.clip(a=X, a_min=0, a_max=offload_computing_portion_up_limit)
                        for x in range(len(X)):
                            offload_computing_portion = X[x]
                            if offload_computing_portion > 0:
                                offload_data_size = data_size * offload_computing_portion
                                # 传输时间
                                edge_transmit_latency = offload_data_size / upload_rate
                                edge_transmit_latency = round(edge_transmit_latency, 6)
                                # print('edge_transmit_latency', edge_transmit_latency)
                                # 传输能耗
                                trans_energy_consumption = edge_transmit_latency * devices_temp[lucky_user].offload_trans_power
                            elif offload_computing_portion == 0:
                                # 传输时间
                                edge_transmit_latency = 0
                                # 传输能耗
                                trans_energy_consumption = 0
                            else:
                                print('error')
                            # 收集能量
                            min_distance = 4000
                            destination = -1
                            for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                                distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                                if distance < min_distance:
                                    min_distance = distance
                                    destination = har_edge_id
                            if devices_temp[lucky_user].locate_BS[destination] == 1:
                                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                                energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
                                # print('energy harvest slot length =', energy_harvest_slot_length)
                                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                                # print('energy harvest ', energy_harvest)
                            else:
                                energy_harvest = 0
                            # 本地计算时间
                            local_computing_portion = 1 - offload_computing_portion
                            if local_computing_portion > 0:
                                local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                                local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
                                # 本地计算时间
                                local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                                # 本地计算能耗
                                local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                                local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
                                local_computing_energy_consumption = local_computing_latency * local_computing_power
                            elif local_computing_portion == 0:
                                local_execute_latency = 0
                                local_computing_energy_consumption = 0
                            else:
                                print('error')
                            # 能量消耗
                            energy_consumption = local_computing_energy_consumption + trans_energy_consumption
                            # 能量效用
                            energy_cost = energy_consumption - energy_harvest
                            # print(energy_cost)
                            # 边缘计算执行时间
                            if offload_computing_portion > 0:
                                offload_computing_cpu_demand = cpu_frequency_demand * offload_computing_portion
                                interference_number = 1
                                for infer_device_id in range(0, config.total_number_of_devices):
                                    if infer_device_id != lucky_user and decisions.execute_mode[infer_device_id] == 'edge' and decisions.execute_destination[infer_device_id] == execute_edge_id:
                                        interference_number += 1
                                actual_frequency = edges_temp[execute_edge_id].frequency / interference_number
                                edge_computing_task_latency = offload_computing_cpu_demand / actual_frequency
                            elif offload_computing_portion == 0:
                                edge_computing_task_latency = 0
                            else:
                                print('error')
                            edge_execute_latency = edge_transmit_latency + edge_computing_task_latency
                            # 延迟效用
                            latency_cost = max(local_execute_latency, edge_execute_latency)
                            # 获取权重
                            latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                            # 总效用
                            # total_edge_cost = latency_weight * latency_cost + energy_weight * energy_cost
                            # scale
                            total_edge_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                            #
                            Y[x] = total_edge_cost
                        # update_pbest
                        for y in range(len(Y)):
                            if pbest_y[y] > Y[y]:
                                pbest_x[y] = X[y].copy()
                                pbest_y[y] = Y[y].copy()
                        # update_gbest
                        idx_min = pbest_y.index(min(pbest_y))
                        if gbest_y > pbest_y[idx_min]:
                            gbest_x = pbest_x[idx_min].copy()  # copy很重要！
                            gbest_y = pbest_y[idx_min]
                        gbest_y_hist.append(gbest_y)
                    this_total_cost = gbest_y
                    # plt.plot(gbest_y_hist)
                    # plt.show()
                    if this_total_cost <= last_total_cost:
                        decisions.execute_mode[lucky_user] = 'edge'
                        decisions.execute_destination[lucky_user] = execute_edge_id
                        decisions.local_computing_portion[lucky_user] = 1-gbest_x
            elif rand == 3:
                choices = [0 for m in range(0, config.total_number_of_devices)]
                for edge_id in range(0, config.total_number_of_edges):
                    if devices_temp[lucky_user].locate_BS[edge_id] == 1:
                        for co_device_id in range(0, config.total_number_of_devices):
                            if edges_temp[edge_id].coverage_mobile_device[co_device_id] == 1:
                                choices[co_device_id] = 1
                choices_number = 0
                for device_id in range(0, config.total_number_of_devices):
                    if choices[device_id] == 1:
                        choices_number = choices_number + 1
                if choices_number == 0:
                    # 不会走
                    execute_mode = 'local'
                    execute_destination = -1
                elif choices_number > 0:
                    lucky_number = numpy.random.randint(1, choices_number + 1)
                    for device_id in range(0, config.total_number_of_devices):
                        if choices[device_id] == 1:
                            lucky_number = lucky_number - 1
                            if lucky_number == 0:
                                if lucky_user == device_id:
                                    execute_mode = 'local'
                                    execute_destination = -1
                                elif lucky_user != device_id:
                                    execute_mode = 'device'
                                    execute_destination = device_id
                                else:
                                    print('error')
                else:
                    print('error')
                # 计算效用
                if execute_mode == 'local':
                    local_computing_size = devices_temp[lucky_user].task_queue_length() + cpu_frequency_demand
                    local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                    latency_cost = local_execute_latency
                    # 本地计算能耗
                    local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency,3)
                    local_computing_latency = cpu_frequency_demand / devices_temp[lucky_user].frequency
                    energy_consumption = local_computing_latency * local_computing_power
                    # 收集能量
                    min_distance = 4000
                    destination = -1
                    for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                        distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                        if distance < min_distance:
                            min_distance = distance
                            destination = har_edge_id
                    if devices_temp[lucky_user].locate_BS[destination] == 1:
                        energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                        energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
                        # print('energy_harvest', energy_harvest)
                    else:
                        energy_harvest = 0
                    # 能量效用
                    energy_cost = energy_consumption - energy_harvest
                    # 获取权重
                    latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                    # 总效用
                    # total_local_cost = latency_weight * latency_cost + energy_weight * energy_cost
                    # scale
                    total_local_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                    this_total_cost = total_local_cost
                    if this_total_cost <= last_total_cost:
                        decisions.execute_mode[lucky_user] = 'local'
                        decisions.execute_destination[lucky_user] = -1
                        decisions.local_computing_portion[lucky_user] = 1
                elif execute_mode == 'device':
                    execute_device_id = execute_destination
                    execute_device = devices_temp[execute_device_id]
                    interference = 1
                    for j in range(0, config.total_number_of_devices):
                        if j != lucky_user and decisions.execute_mode[j] == 'device' and decisions.execute_destination[j] == execute_device_id:
                            interference += 1
                    d2d_rate = get_d2d_rate(device1=devices_temp[lucky_user], device2=execute_device, interference=interference)
                    slot_d2d_data_size = d2d_rate * config.time_slot_length
                    d2d_data_size_up_limit = min(slot_d2d_data_size, data_size)
                    d2d_computing_portion_up_limit = d2d_data_size_up_limit / data_size
                    X = numpy.random.uniform(low=0, high=d2d_computing_portion_up_limit, size=config.pop_size)
                    X[0] = 0
                    X[1] = d2d_computing_portion_up_limit
                    Y = [0 for _ in range(len(X))]
                    for x in range(len(X)):
                        d2d_computing_portion = X[x]
                        if d2d_computing_portion > 0:
                            d2d_data_size = data_size * d2d_computing_portion
                            # 传输时间
                            d2d_transmit_latency = d2d_data_size / d2d_rate
                            d2d_transmit_latency = round(d2d_transmit_latency, 6)
                            # print('d2d_transmit_latency', d2d_transmit_latency)
                            # 传输能耗
                            d2d_trans_energy_consumption = d2d_transmit_latency * devices_temp[lucky_user].d2d_trans_power
                            # 计算能耗
                            d2d_computing_cpu_demand = d2d_data_size * config.task_cpu_frequency_demand
                            d2d_computing_power = config.SWITCHED_CAPACITANCE * math.pow(execute_device.frequency, 3)
                            d2d_computing_latency = d2d_computing_cpu_demand / execute_device.frequency
                            d2d_computing_energy_consumption = d2d_computing_latency * d2d_computing_power
                            # 总能耗
                            total_d2d_energy_consumption = d2d_trans_energy_consumption + d2d_computing_energy_consumption
                        elif d2d_computing_portion == 0:
                            # 传输时间
                            d2d_transmit_latency = 0
                            # 传输能耗
                            d2d_trans_energy_consumption = 0
                            # 计算能耗
                            d2d_computing_energy_consumption = 0
                            # 总能耗
                            total_d2d_energy_consumption = 0
                        else:
                            print('error')
                        # 收集能量
                        min_distance = 4000
                        destination = -1
                        for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                            distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                            if distance < min_distance:
                                min_distance = distance
                                destination = har_edge_id
                        if devices_temp[lucky_user].locate_BS[destination] == 1:
                            energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                            energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
                            # print('energy harvest slot length =', energy_harvest_slot_length)
                            energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                            # print('energy harvest ', energy_harvest)
                        else:
                            energy_harvest = 0
                        # 本地计算时间
                        local_computing_portion = 1 - d2d_computing_portion
                        if local_computing_portion > 0:
                            local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                            local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
                            # 本地计算时间
                            local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                            # 本地计算能耗
                            local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                            local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
                            local_computing_energy_consumption = local_computing_latency * local_computing_power
                        elif local_computing_portion == 0:
                            local_execute_latency = 0
                            local_computing_energy_consumption = 0
                        else:
                            print('error')
                        # 能量消耗
                        energy_consumption = local_computing_energy_consumption + total_d2d_energy_consumption
                        # 能量效用
                        energy_cost = energy_consumption - energy_harvest
                        # print(energy_cost)
                        # 边缘计算执行时间
                        if d2d_computing_portion > 0:
                            d2d_cpu_frequency_demand = cpu_frequency_demand * d2d_computing_portion
                            device_queue_length = execute_device.task_queue_length() + d2d_cpu_frequency_demand
                            d2d_computing_task_latency = device_queue_length / execute_device.frequency
                        elif d2d_computing_portion == 0:
                            d2d_computing_task_latency = 0
                        else:
                            print('error')
                        d2d_execute_latency = d2d_transmit_latency + d2d_computing_task_latency
                        # 延迟效用
                        latency_cost = max(local_execute_latency, d2d_execute_latency)
                        # 获取权重
                        latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                        # 总效用
                        # total_d2d_cost = latency_weight * latency_cost + energy_weight * energy_cost
                        # scale
                        total_d2d_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                        #
                        Y[x] = total_d2d_cost
                    pbest_x = X.copy()  # personal best location of every particle in history
                    # self.pbest_x = self.X 表示地址传递,改变 X 值 pbest_x 也会变化
                    pbest_y = [numpy.inf for _ in range(config.pop_size)]  # best image of every particle in history
                    # self.gbest_x = self.pbest_x.mean(axis=0).reshape(1, -1)  # global best location for all particles
                    gbest_x = pbest_x.mean(axis=0)
                    gbest_y = numpy.inf  # global best y for all particles
                    gbest_y_hist = []  # gbest_y of every iteration
                    for this_iter in range(config.max_iter):
                        # # update
                        # r1 = config.a - this_iter * (config.a / config.max_iter)
                        # 抛物线函数
                        iter_period = this_iter / config.max_iter
                        inter_rest_phase = 1 - iter_period
                        square = pow(inter_rest_phase, 2)
                        r1 = config.a * square
                        for pop in range(config.pop_size):
                            r2 = 2 * math.pi * random.uniform(0.0, 1.0)
                            r3 = 2 * random.uniform(0.0, 1.0)
                            r4 = random.uniform(0.0, 1.0)
                            if r4 < 0.5:
                                X[pop] = X[pop] + (r1 * math.sin(r2) * abs(r3 * gbest_x - X[pop]))
                            else:
                                X[pop] = X[pop] + (r1 * math.cos(r2) * abs(r3 * gbest_x - X[pop]))
                        X = numpy.clip(a=X, a_min=0, a_max=d2d_computing_portion_up_limit)
                        for x in range(len(X)):
                            d2d_computing_portion = X[x]
                            if d2d_computing_portion > 0:
                                d2d_data_size = data_size * d2d_computing_portion
                                # 传输时间
                                d2d_transmit_latency = d2d_data_size / d2d_rate
                                d2d_transmit_latency = round(d2d_transmit_latency, 6)
                                # print('d2d_transmit_latency', d2d_transmit_latency)
                                # 传输能耗
                                d2d_trans_energy_consumption = d2d_transmit_latency * devices_temp[lucky_user].d2d_trans_power
                                # 计算能耗
                                d2d_computing_cpu_demand = d2d_data_size * config.task_cpu_frequency_demand
                                d2d_computing_power = config.SWITCHED_CAPACITANCE * math.pow(execute_device.frequency, 3)
                                d2d_computing_latency = d2d_computing_cpu_demand / execute_device.frequency
                                d2d_computing_energy_consumption = d2d_computing_latency * d2d_computing_power
                                # 总能耗
                                total_d2d_energy_consumption = d2d_trans_energy_consumption + d2d_computing_energy_consumption
                            elif d2d_computing_portion == 0:
                                # 传输时间
                                d2d_transmit_latency = 0
                                # 传输能耗
                                d2d_trans_energy_consumption = 0
                                # 计算能耗
                                d2d_computing_energy_consumption = 0
                                # 总能耗
                                total_d2d_energy_consumption = 0
                            else:
                                print('error')
                            # 收集能量
                            min_distance = 4000
                            destination = -1
                            for har_edge_id in range(0, len(devices_temp[lucky_user].distance_BS)):
                                distance = devices_temp[lucky_user].distance_BS[har_edge_id]
                                if distance < min_distance:
                                    min_distance = distance
                                    destination = har_edge_id
                            if devices_temp[lucky_user].locate_BS[destination] == 1:
                                energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
                                energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
                                # print('energy harvest slot length =', energy_harvest_slot_length)
                                energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
                                # print('energy harvest ', energy_harvest)
                            else:
                                energy_harvest = 0
                            # 本地计算时间
                            local_computing_portion = 1 - d2d_computing_portion
                            if local_computing_portion > 0:
                                local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
                                local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
                                # 本地计算时间
                                local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
                                # 本地计算能耗
                                local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
                                local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
                                local_computing_energy_cost = local_computing_latency * local_computing_power
                            elif local_computing_portion == 0:
                                local_execute_latency = 0
                                local_computing_energy_cost = 0
                            else:
                                print('error')
                            # 能量消耗
                            energy_consumption = local_computing_energy_cost + total_d2d_energy_consumption
                            # 能量效用
                            energy_cost = energy_consumption - energy_harvest
                            # print(energy_cost)
                            # 边缘计算执行时间
                            if d2d_computing_portion > 0:
                                d2d_cpu_frequency_demand = cpu_frequency_demand * d2d_computing_portion
                                device_queue_length = execute_device.task_queue_length() + d2d_cpu_frequency_demand
                                d2d_computing_task_latency = device_queue_length / execute_device.frequency
                            elif d2d_computing_portion == 0:
                                d2d_computing_task_latency = 0
                            else:
                                print('error')
                            d2d_execute_latency = d2d_transmit_latency + d2d_computing_task_latency
                            # 延迟效用
                            latency_cost = max(local_execute_latency, d2d_execute_latency)
                            # 获取权重
                            latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
                            # 总效用
                            # total_d2d_cost = latency_weight * latency_cost + energy_weight * energy_cost
                            # scale
                            total_d2d_cost = latency_weight * latency_cost + 30 * energy_weight * energy_cost
                            #
                            Y[x] = total_d2d_cost
                        # update_pbest
                        for y in range(len(Y)):
                            if pbest_y[y] > Y[y]:
                                pbest_x[y] = X[y].copy()
                                pbest_y[y] = Y[y].copy()
                        # update_gbest
                        idx_min = pbest_y.index(min(pbest_y))
                        if gbest_y > pbest_y[idx_min]:
                            gbest_x = pbest_x[idx_min].copy()  # copy很重要！
                            gbest_y = pbest_y[idx_min].copy()
                        gbest_y_hist.append(gbest_y)
                    this_total_cost = gbest_y
                    # plt.plot(gbest_y_hist)
                    # plt.show()
                    if this_total_cost <= last_total_cost:
                        decisions.execute_mode[lucky_user] = 'device'
                        decisions.execute_destination[lucky_user] = execute_device_id
                        decisions.local_computing_portion[lucky_user] = 1-gbest_x
        elif decisions.execute_mode[lucky_user] == 'null':
            pass
        else:
            pass
    return decisions


# def proposed_algorithm_v2(decisions, config, devices, edges, time_slot, task_in_each_slot):
#     decisions = random_algorithm(decisions, config, devices, edges, time_slot, task_in_each_slot)
#     for i in range(0, config.iterations_number_of_game_theory):
#         lucky_user = numpy.random.randint(0, config.total_number_of_devices)
#         while decisions.execute_mode[lucky_user] == 'null':
#             lucky_user = numpy.random.randint(0, config.total_number_of_devices)
#         if decisions.execute_mode[lucky_user] != 'null':
#             devices_temp = deepcopy(devices)
#             edges_temp = deepcopy(edges)
#             for j in range(0, lucky_user):
#                 if decisions.execute_mode[j] == 'local':
#                     cpu_frequency_demand = task_in_each_slot[time_slot][j].cpu_frequency_demand
#                     devices_temp[j].task_enqueue(cpu_frequency_demand)
#                 elif decisions.execute_mode[j] == 'edge':
#                     execute_destination = decisions.execute_destination[j]
#                     data_size = task_in_each_slot[time_slot][j].data_size
#                     local_computing_portion = decisions.local_computing_portion[j]
#                     edge_computing_portion = 1 - local_computing_portion
#                     offload_data_size = data_size * edge_computing_portion
#                     # 计算传输速率
#                     interference = 0
#                     for k in range(0, config.total_number_of_devices):
#                         if k != j and decisions.execute_mode[k] == 'edge' and decisions.execute_destination[k] == execute_destination:
#                             gain = get_upload_gain(device=devices_temp[k], edge=edges_temp[execute_destination])
#                             interference += gain
#                     upload_rate = get_upload_rate(device=devices_temp[j], edge=edges_temp[execute_destination], interference=interference)
#                     # 传输时间
#                     edge_transmit_latency = offload_data_size / upload_rate
#                     edge_transmit_latency = round(edge_transmit_latency, 6)
#                     if edge_transmit_latency >= config.time_slot_length:
#                         edge_transmit_latency = config.time_slot_length
#                     edge_transmit_data_size = edge_transmit_latency * upload_rate
#                     edge_transmit_cpu_frequency_demand = edge_transmit_data_size * config.task_cpu_frequency_demand
#                     edges_temp[execute_destination].task_enqueue(edge_transmit_cpu_frequency_demand)
#                     local_computing_data_size = data_size - edge_transmit_data_size
#                     if edge_transmit_latency == config.time_slot_length:
#                         decisions.local_computing_portion[j] = local_computing_data_size / data_size
#                     local_computing_cpu_frequency_demand = local_computing_data_size * config.task_cpu_frequency_demand
#                     devices_temp[j].task_enqueue(local_computing_cpu_frequency_demand)
#                 elif decisions.execute_mode[j] == 'device':
#                     execute_destination = decisions.execute_destination[j]
#                     data_size = task_in_each_slot[time_slot][j].data_size
#                     local_computing_portion = decisions.local_computing_portion[j]
#                     d2d_computing_portion = 1 - local_computing_portion
#                     d2d_data_size = data_size * d2d_computing_portion
#                     # 计算传输速率
#                     interference = 0
#                     for k in range(0, config.total_number_of_devices):
#                         if k != j and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == execute_destination:
#                             gain = get_d2d_gain(device1=devices_temp[k], device2=devices_temp[execute_destination])
#                             interference += gain
#                     d2d_rate = get_d2d_rate(device1=devices_temp[j], device2=devices_temp[execute_destination], interference=interference)
#                     # 传输时间
#                     d2d_transmit_latency = d2d_data_size / d2d_rate
#                     d2d_transmit_latency = round(d2d_transmit_latency, 6)
#                     if d2d_transmit_latency >= config.time_slot_length:
#                         d2d_transmit_latency = config.time_slot_length
#                     d2d_transmit_data_size = d2d_transmit_latency * d2d_rate
#                     d2d_transmit_cpu_frequency_demand = d2d_transmit_data_size * config.task_cpu_frequency_demand
#                     devices_temp[execute_destination].task_enqueue(d2d_transmit_cpu_frequency_demand)
#                     local_computing_data_size = data_size - d2d_transmit_data_size
#                     if d2d_transmit_latency == config.time_slot_length:
#                         decisions.local_computing_portion[j] = local_computing_data_size / data_size
#                     local_computing_cpu_frequency_demand = local_computing_data_size * config.task_cpu_frequency_demand
#                     devices_temp[j].task_enqueue(local_computing_cpu_frequency_demand)
#             task = task_in_each_slot[time_slot][lucky_user]
#             data_size = task_in_each_slot[time_slot][lucky_user].data_size
#             cpu_frequency_demand = task_in_each_slot[time_slot][lucky_user].cpu_frequency_demand
#             # 计算上一轮的效用
#             last_total_utility = 0
#             if decisions.execute_mode[lucky_user] == 'local':
#                 local_computing_size = devices_temp[lucky_user].task_queue_length() + cpu_frequency_demand
#                 local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                 latency_utility = local_execute_latency
#                 # 本地计算能耗
#                 local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
#                 local_computing_latency = cpu_frequency_demand / devices_temp[lucky_user].frequency
#                 energy_cost = local_computing_latency * local_computing_power
#                 # 收集能量
#                 min_distance = 4000
#                 destination = -1
#                 for j in range(0, len(devices_temp[lucky_user].distance_BS)):
#                     distance = devices_temp[lucky_user].distance_BS[j]
#                     if distance < min_distance:
#                         min_distance = distance
#                         destination = j
#                 if devices_temp[lucky_user].locate_BS[destination] == 1:
#                     energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                     energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
#                 else:
#                     energy_harvest = 0
#                 # 能量效用
#                 energy_utility = energy_cost - energy_harvest
#                 # 获取权重
#                 latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                 # 总效用
#                 total_local_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                 lya = 0
#                 for j in range(0, config.total_number_of_devices):
#                     # 计算lyapunov
#                     cpu_frequency_demand_offload = 0
#                     for k in range(0, config.total_number_of_devices):
#                         if k != j and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == j:
#                             cpu_frequency_demand_lya = task_in_each_slot[time_slot][k].cpu_frequency_demand
#                             local_computing_portion = decisions.local_computing_portion[k]
#                             offload_computing_portion = (1 - local_computing_portion)
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                     if decisions.execute_mode[j] == 'local':
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand
#                     elif decisions.execute_mode[j] != 'null':
#                         local_computing_portion = decisions.local_computing_portion[j]
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand * local_computing_portion
#                     cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                     cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                     queue_length = devices[j].task_queue_length() / config.task_cpu_frequency_demand
#                     queue_length = queue_length / 8388608
#                     lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                 last_total_utility = total_local_utility + config.V * lya
#             elif decisions.execute_mode[lucky_user] == 'edge':
#                 execute_edge_id = decisions.execute_destination[lucky_user]
#                 local_computing_portion = decisions.local_computing_portion[lucky_user]
#                 execute_edge = edges_temp[execute_edge_id]
#                 # 计算卸载数据大小
#                 offload_computing_portion = (1 - local_computing_portion)
#                 # print('offload_computing_portion', offload_computing_portion)
#                 if offload_computing_portion > 0:
#                     offload_data_size = data_size * offload_computing_portion
#                     # 计算传输速率
#                     interference = 0
#                     for j in range(0, config.total_number_of_devices):
#                         if j != lucky_user and decisions.execute_mode[j] == 'edge' and decisions.execute_destination[j] == execute_edge_id:
#                             gain = get_upload_gain(device=devices_temp[j], edge=execute_edge)
#                             interference += gain
#                     upload_rate = get_upload_rate(device=devices_temp[lucky_user], edge=execute_edge, interference=interference)
#                     # 传输时间
#                     edge_transmit_latency = offload_data_size / upload_rate
#                     edge_transmit_latency = round(edge_transmit_latency, 6)
#                     if edge_transmit_latency >= config.time_slot_length:
#                         edge_transmit_latency = config.time_slot_length
#                     # 传输能耗
#                     trans_energy_cost = edge_transmit_latency * devices_temp[lucky_user].offload_trans_power
#                 elif offload_computing_portion == 0:
#                     # 传输时间
#                     edge_transmit_latency = 0
#                     # 传输能耗
#                     trans_energy_cost = 0
#                 else:
#                     print('error')
#                 # 收集能量
#                 min_distance = 4000
#                 destination = -1
#                 for j in range(0, len(devices_temp[lucky_user].distance_BS)):
#                     distance = devices_temp[lucky_user].distance_BS[j]
#                     if distance < min_distance:
#                         min_distance = distance
#                         destination = j
#                 if devices_temp[lucky_user].locate_BS[destination] == 1:
#                     energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                     energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
#                     # print('energy harvest slot length =', energy_harvest_slot_length)
#                     energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
#                     # print('energy harvest ', energy_harvest)
#                 else:
#                     energy_harvest = 0
#                 # 本地计算时间
#                 if local_computing_portion > 0:
#                     if edge_transmit_latency == config.time_slot_length:
#                         edge_transmit_data_size = upload_rate * config.time_slot_length
#                         local_computing_data_size = data_size - edge_transmit_data_size
#                         decisions.local_computing_portion[lucky_user] = local_computing_data_size / data_size
#                         local_computing_cpu_demand = local_computing_data_size * config.task_cpu_frequency_demand
#                     else:
#                         local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
#                     local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
#                     # 本地计算时间
#                     local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                     # 本地计算能耗
#                     local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
#                     local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
#                     local_computing_energy_cost = local_computing_latency * local_computing_power
#                 elif local_computing_portion == 0:
#                     local_computing_cpu_demand = 0
#                     local_execute_latency = 0
#                     local_computing_energy_cost = 0
#                 else:
#                     print('error')
#                 # 能量消耗
#                 energy_cost = local_computing_energy_cost + trans_energy_cost
#                 # 能量效用
#                 energy_utility = energy_cost - energy_harvest
#                 # print(energy_utility)
#                 # 边缘计算执行时间
#                 if offload_computing_portion > 0:
#                     offload_computing_cpu_demand = cpu_frequency_demand - local_computing_cpu_demand
#                     edge_queue_length = execute_edge.task_queue_length() + offload_computing_cpu_demand
#                     edge_computing_task_latency = edge_queue_length / execute_edge.frequency
#                 elif offload_computing_portion == 0:
#                     edge_computing_task_latency = 0
#                 else:
#                     print('error')
#                 edge_execute_latency = edge_transmit_latency + edge_computing_task_latency
#                 # 延迟效用
#                 latency_utility = max(local_execute_latency, edge_execute_latency)
#                 # print('energy queue', devices_temp[lucky_user].energy_queue)
#                 # 获取权重
#                 latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                 # 总效用
#                 total_edge_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                 lya = 0
#                 for j in range(0, config.total_number_of_devices):
#                     # 计算lyapunov
#                     cpu_frequency_demand_offload = 0
#                     for k in range(0, config.total_number_of_devices):
#                         if k != j and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == j:
#                             cpu_frequency_demand_lya = task_in_each_slot[time_slot][k].cpu_frequency_demand
#                             local_computing_portion = decisions.local_computing_portion[k]
#                             offload_computing_portion = (1 - local_computing_portion)
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                     if decisions.execute_mode[j] == 'local':
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand
#                     elif decisions.execute_mode[j] != 'null':
#                         local_computing_portion = decisions.local_computing_portion[j]
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand * local_computing_portion
#                     cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                     cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                     queue_length = devices[j].task_queue_length() / config.task_cpu_frequency_demand
#                     queue_length = queue_length / 8388608
#                     lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                 last_total_utility = total_edge_utility + config.V * lya
#             elif decisions.execute_mode[lucky_user] == 'device':
#                 execute_device_id = decisions.execute_destination[lucky_user]
#                 local_computing_portion = decisions.local_computing_portion[lucky_user]
#                 execute_device = devices_temp[execute_device_id]
#                 # 计算卸载数据大小
#                 offload_computing_portion = (1 - local_computing_portion)
#                 if offload_computing_portion > 0:
#                     offload_data_size = data_size * offload_computing_portion
#                     # 计算传输速率
#                     interference = 0
#                     for j in range(0, config.total_number_of_devices):
#                         if j != lucky_user and decisions.execute_mode[j] == 'device' and decisions.execute_destination[j] == execute_device_id:
#                             gain = get_d2d_gain(device1=devices_temp[j], device2=execute_device)
#                             interference += gain
#                     d2d_rate = get_d2d_rate(device1=devices_temp[lucky_user], device2=execute_device, interference=interference)
#                     # 传输时间
#                     d2d_transmit_latency = offload_data_size / d2d_rate
#                     d2d_transmit_latency = round(d2d_transmit_latency, 6)
#                     if d2d_transmit_latency >= config.time_slot_length:
#                         d2d_transmit_latency = config.time_slot_length
#                     # 传输能耗
#                     trans_energy_cost = d2d_transmit_latency * devices_temp[lucky_user].d2d_trans_power
#                 elif offload_computing_portion == 0:
#                     # 传输时间
#                     d2d_transmit_latency = 0
#                     # 传输能耗
#                     trans_energy_cost = 0
#                 else:
#                     print('error')
#                 # 收集能量
#                 min_distance = 4000
#                 destination = -1
#                 for j in range(0, len(devices_temp[lucky_user].distance_BS)):
#                     distance = devices_temp[lucky_user].distance_BS[j]
#                     if distance < min_distance:
#                         min_distance = distance
#                         destination = j
#                 if devices_temp[lucky_user].locate_BS[destination] == 1:
#                     energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                     energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
#                     energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
#                 else:
#                     energy_harvest = 0
#                 # 本地计算时间
#                 if local_computing_portion > 0:
#                     if d2d_transmit_latency == config.time_slot_length:
#                         d2d_transmit_data_size = d2d_rate * config.time_slot_length
#                         local_computing_data_size = data_size - d2d_transmit_data_size
#                         decisions.local_computing_portion[lucky_user] = local_computing_data_size / data_size
#                         local_computing_cpu_demand = local_computing_data_size * config.task_cpu_frequency_demand
#                     else:
#                         local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
#                     local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
#                     # 本地计算时间
#                     local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                     # 本地计算能耗
#                     local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
#                     local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
#                     local_computing_energy_cost = local_computing_latency * local_computing_power
#                 elif local_computing_portion == 0:
#                     local_computing_cpu_demand = 0
#                     local_execute_latency = 0
#                     local_computing_energy_cost = 0
#                 else:
#                     print('error')
#                 # 能量消耗
#                 energy_cost = local_computing_energy_cost + trans_energy_cost
#                 # 能量效用
#                 energy_utility = energy_cost - energy_harvest
#                 # 边缘计算执行时间
#                 if offload_computing_portion > 0:
#                     offload_computing_cpu_demand = cpu_frequency_demand - local_computing_cpu_demand
#                     d2d_queue_length = execute_device.task_queue_length() + offload_computing_cpu_demand
#                     d2d_compute_task_latency = d2d_queue_length / execute_device.frequency
#                 elif offload_computing_portion == 0:
#                     d2d_compute_task_latency = 0
#                 else:
#                     print('error')
#                 d2d_execute_latency = d2d_transmit_latency + d2d_compute_task_latency
#                 # 延迟效用
#                 latency_utility = max(local_execute_latency, d2d_execute_latency)
#                 # 获取权重
#                 latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                 # 总效用
#                 total_d2d_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                 lya = 0
#                 for j in range(0, config.total_number_of_devices):
#                     # 计算lyapunov
#                     cpu_frequency_demand_offload = 0
#                     for k in range(0, config.total_number_of_devices):
#                         if k != j and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == j:
#                             cpu_frequency_demand_lya = task_in_each_slot[time_slot][k].cpu_frequency_demand
#                             local_computing_portion = decisions.local_computing_portion[k]
#                             offload_computing_portion = (1 - local_computing_portion)
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                     if decisions.execute_mode[j] == 'local':
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand
#                     elif decisions.execute_mode[j] != 'null':
#                         local_computing_portion = decisions.local_computing_portion[j]
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand * local_computing_portion
#                     cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                     cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                     queue_length = devices[j].task_queue_length() / config.task_cpu_frequency_demand
#                     queue_length = queue_length / 8388608
#                     lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                 last_total_utility = total_d2d_utility + config.V * lya
#             # this interation
#             rand = numpy.random.randint(1, 4)
#             if rand == 1:
#                 local_computing_size = devices_temp[lucky_user].task_queue_length() + cpu_frequency_demand
#                 local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                 latency_utility = local_execute_latency
#                 # 本地计算能耗
#                 local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
#                 local_computing_latency = cpu_frequency_demand / devices_temp[lucky_user].frequency
#                 energy_cost = local_computing_latency * local_computing_power
#                 # 收集能量
#                 min_distance = 4000
#                 destination = -1
#                 for j in range(0, len(devices_temp[lucky_user].distance_BS)):
#                     distance = devices_temp[lucky_user].distance_BS[j]
#                     if distance < min_distance:
#                         min_distance = distance
#                         destination = j
#                 if devices_temp[lucky_user].locate_BS[destination] == 1:
#                     energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                     energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
#                     # print('energy_harvest', energy_harvest)
#                 else:
#                     energy_harvest = 0
#                 # 能量效用
#                 energy_utility = energy_cost - energy_harvest
#                 # 获取权重
#                 latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                 # 总效用
#                 total_local_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                 lya = 0
#                 for j in range(0, config.total_number_of_devices):
#                     # 计算lyapunov
#                     cpu_frequency_demand_offload = 0
#                     for k in range(0, config.total_number_of_devices):
#                         if k != j and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == j:
#                             cpu_frequency_demand_lya = task_in_each_slot[time_slot][k].cpu_frequency_demand
#                             local_computing_portion = decisions.local_computing_portion[k]
#                             offload_computing_portion = (1 - local_computing_portion)
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                     if decisions.execute_mode[j] == 'local':
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand
#                     elif decisions.execute_mode[j] != 'null':
#                         local_computing_portion = decisions.local_computing_portion[j]
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand * local_computing_portion
#                     cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                     cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                     queue_length = devices[j].task_queue_length() / config.task_cpu_frequency_demand
#                     queue_length = queue_length / 8388608
#                     lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                 this_total_utility = total_local_utility + config.V * lya
#                 if this_total_utility <= last_total_utility:
#                     decisions.execute_mode[lucky_user] = 'local'
#                     decisions.execute_destination[lucky_user] = -1
#                     decisions.local_computing_portion[lucky_user] = 1
#             elif rand == 2:
#                 # 随机选动作
#                 choices_number = 0
#                 for j in range(0, config.total_number_of_edges):
#                     if devices_temp[lucky_user].locate_BS[j] == 1:
#                         choices_number = choices_number + 1
#                 if choices_number == 0:
#                     execute_mode = 'local'
#                     execute_destination = -1
#                 elif choices_number > 0:
#                     lucky_number = numpy.random.randint(1, choices_number + 1)
#                     for j in range(0, config.total_number_of_edges):
#                         if devices_temp[lucky_user].locate_BS[j] == 1:
#                             lucky_number = lucky_number - 1
#                             if lucky_number == 0:
#                                 execute_mode = 'edge'
#                                 execute_destination = j
#                 # 计算效用
#                 if execute_mode == 'local':
#                     local_computing_size = devices_temp[lucky_user].task_queue_length() + cpu_frequency_demand
#                     local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                     latency_utility = local_execute_latency
#                     # 本地计算能耗
#                     local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency,3)
#                     local_computing_latency = cpu_frequency_demand / devices_temp[lucky_user].frequency
#                     energy_cost = local_computing_latency * local_computing_power
#                     # 收集能量
#                     min_distance = 4000
#                     destination = -1
#                     for j in range(0, len(devices_temp[lucky_user].distance_BS)):
#                         distance = devices_temp[lucky_user].distance_BS[j]
#                         if distance < min_distance:
#                             min_distance = distance
#                             destination = j
#                     if devices_temp[lucky_user].locate_BS[destination] == 1:
#                         energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                         energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
#                         # print('energy_harvest', energy_harvest)
#                     else:
#                         energy_harvest = 0
#                     # 能量效用
#                     energy_utility = energy_cost - energy_harvest
#                     # 获取权重
#                     latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                     # 总效用
#                     total_local_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                     lya = 0
#                     for j in range(0, config.total_number_of_devices):
#                         # 计算lyapunov
#                         cpu_frequency_demand_offload = 0
#                         for k in range(0, config.total_number_of_devices):
#                             if k != j and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == j:
#                                 cpu_frequency_demand_lya = task_in_each_slot[time_slot][k].cpu_frequency_demand
#                                 local_computing_portion = decisions.local_computing_portion[k]
#                                 offload_computing_portion = (1 - local_computing_portion)
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                         if decisions.execute_mode[j] == 'local':
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand
#                         elif decisions.execute_mode[j] != 'null':
#                             local_computing_portion = decisions.local_computing_portion[j]
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand * local_computing_portion
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                         queue_length = devices[j].task_queue_length() / config.task_cpu_frequency_demand
#                         queue_length = queue_length / 8388608
#                         lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                     this_total_utility = total_local_utility + config.V * lya
#                     if this_total_utility <= last_total_utility:
#                         decisions.execute_mode[lucky_user] = 'local'
#                         decisions.execute_destination[lucky_user] = -1
#                         decisions.local_computing_portion[lucky_user] = 1
#                 elif execute_mode == 'edge':
#                     execute_edge_id = execute_destination
#                     execute_edge = edges_temp[execute_edge_id]
#                     interference = 0
#                     for j in range(0, config.total_number_of_devices):
#                         if j != lucky_user and decisions.execute_mode[j] == 'edge' and decisions.execute_destination[j] == execute_edge_id:
#                             gain = get_upload_gain(device=devices_temp[j], edge=execute_edge)
#                             interference += gain
#                     upload_rate = get_upload_rate(device=devices_temp[lucky_user], edge=execute_edge, interference=interference)
#                     slot_upload_data_size = upload_rate * config.time_slot_length
#                     slot_upload_data_size = round(slot_upload_data_size, 6)
#                     offload_data_size_up_limit = min(slot_upload_data_size, data_size)
#                     offload_computing_portion_up_limit = offload_data_size_up_limit / data_size
#                     offload_computing_portion_up_limit = round(offload_computing_portion_up_limit, 6)
#                     X = numpy.random.uniform(low=0, high=offload_computing_portion_up_limit, size=config.pop_size)
#                     X[0] = 0
#                     X[1] = offload_computing_portion_up_limit
#                     Y = [0 for m in range(len(X))]
#                     for j in range(len(X)):
#                         offload_computing_portion = X[j]
#                         if offload_computing_portion > 0:
#                             offload_data_size = data_size * offload_computing_portion
#                             # 传输时间
#                             edge_transmit_latency = offload_data_size / upload_rate
#                             edge_transmit_latency = round(edge_transmit_latency, 6)
#                             # print('edge_transmit_latency', edge_transmit_latency)
#                             # 传输能耗
#                             trans_energy_cost = edge_transmit_latency * devices_temp[lucky_user].offload_trans_power
#                         elif offload_computing_portion == 0:
#                             # 传输时间
#                             edge_transmit_latency = 0
#                             # 传输能耗
#                             trans_energy_cost = 0
#                         else:
#                             print('error')
#                         # 收集能量
#                         min_distance = 4000
#                         destination = -1
#                         for k in range(0, len(devices_temp[lucky_user].distance_BS)):
#                             distance = devices_temp[lucky_user].distance_BS[k]
#                             if distance < min_distance:
#                                 min_distance = distance
#                                 destination = k
#                         if devices_temp[lucky_user].locate_BS[destination] == 1:
#                             energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                             energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
#                             # print('energy harvest slot length =', energy_harvest_slot_length)
#                             energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
#                             # print('energy harvest =', energy_harvest)
#                         else:
#                             energy_harvest = 0
#                         # 本地计算时间
#                         local_computing_portion = 1 - offload_computing_portion
#                         if local_computing_portion > 0:
#                             local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
#                             local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
#                             # 本地计算时间
#                             local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                             # 本地计算能耗
#                             local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
#                             local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
#                             local_computing_energy_cost = local_computing_latency * local_computing_power
#                         elif local_computing_portion == 0:
#                             local_computing_cpu_demand = 0
#                             local_execute_latency = 0
#                             local_computing_energy_cost = 0
#                         else:
#                             print('error')
#                         # 能量消耗
#                         energy_cost = local_computing_energy_cost + trans_energy_cost
#                         # 能量效用
#                         energy_utility = energy_cost - energy_harvest
#                         # print(energy_utility)
#                         # 边缘计算执行时间
#                         if offload_computing_portion > 0:
#                             offload_computing_cpu_demand = cpu_frequency_demand * offload_computing_portion
#                             edge_queue_length = execute_edge.task_queue_length() + offload_computing_cpu_demand
#                             edge_computing_task_latency = edge_queue_length / execute_edge.frequency
#                         elif offload_computing_portion == 0:
#                             edge_computing_task_latency = 0
#                         else:
#                             print('error')
#                         edge_execute_latency = edge_transmit_latency + edge_computing_task_latency
#                         # 延迟效用
#                         latency_utility = max(local_execute_latency, edge_execute_latency)
#                         # 获取权重
#                         latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                         # 总效用
#                         total_edge_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                         lya = 0
#                         for m in range(0, config.total_number_of_devices):
#                             # 计算lyapunov
#                             cpu_frequency_demand_offload = 0
#                             for k in range(0, config.total_number_of_devices):
#                                 if k != m and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == m:
#                                     cpu_frequency_demand_lya = task_in_each_slot[time_slot][k].cpu_frequency_demand
#                                     local_computing_portion = decisions.local_computing_portion[k]
#                                     offload_computing_portion = (1 - local_computing_portion)
#                                     cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                             if decisions.execute_mode[m] == 'local':
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][m].cpu_frequency_demand
#                             elif decisions.execute_mode[m] != 'null':
#                                 local_computing_portion = decisions.local_computing_portion[m]
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][m].cpu_frequency_demand * local_computing_portion
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                             queue_length = devices[m].task_queue_length() / config.task_cpu_frequency_demand
#                             queue_length = queue_length / 8388608
#                             lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                         total_edge_utility = total_edge_utility + config.V * lya
#                         #
#                         Y[j] = total_edge_utility
#                     pbest_x = X.copy()  # personal best location of every particle in history
#                     # self.pbest_x = self.X 表示地址传递,改变 X 值 pbest_x 也会变化
#                     pbest_y = [numpy.inf for m in range(config.pop_size)]  # best image of every particle in history
#                     # self.gbest_x = self.pbest_x.mean(axis=0).reshape(1, -1)  # global best location for all particles
#                     gbest_x = pbest_x.mean(axis=0)
#                     gbest_y = numpy.inf  # global best y for all particles
#                     gbest_y_hist = []  # gbest_y of every iteration
#                     for j in range(config.max_iter):
#                         # # update
#                         # r1 = config.a - j * (config.a / config.max_iter)
#                         # 抛物线函数
#                         iter_period = j / config.max_iter
#                         inter_rest_phase = 1 - iter_period
#                         square = pow(inter_rest_phase, 2)
#                         r1 = config.a * square
#                         for k in range(config.pop_size):
#                             r2 = 2 * math.pi * random.uniform(0.0, 1.0)
#                             r3 = 2 * random.uniform(0.0, 1.0)
#                             r4 = random.uniform(0.0, 1.0)
#                             if r4 < 0.5:
#                                 X[k] = X[k] + (r1 * math.sin(r2) * abs(r3 * gbest_x - X[k]))
#                             else:
#                                 X[k] = X[k] + (r1 * math.cos(r2) * abs(r3 * gbest_x - X[k]))
#                         X = numpy.clip(a=X, a_min=0, a_max=offload_computing_portion_up_limit)
#                         for k in range(len(X)):
#                             offload_computing_portion = X[k]
#                             if offload_computing_portion > 0:
#                                 offload_data_size = data_size * offload_computing_portion
#                                 # 传输时间
#                                 edge_transmit_latency = offload_data_size / upload_rate
#                                 edge_transmit_latency = round(edge_transmit_latency, 6)
#                                 # print('edge_transmit_latency', edge_transmit_latency)
#                                 # 传输能耗
#                                 trans_energy_cost = edge_transmit_latency * devices_temp[lucky_user].offload_trans_power
#                             elif offload_computing_portion == 0:
#                                 # 传输时间
#                                 edge_transmit_latency = 0
#                                 # 传输能耗
#                                 trans_energy_cost = 0
#                             else:
#                                 print('error')
#                             # 收集能量
#                             min_distance = 4000
#                             destination = -1
#                             for m in range(0, len(devices_temp[lucky_user].distance_BS)):
#                                 distance = devices_temp[lucky_user].distance_BS[m]
#                                 if distance < min_distance:
#                                     min_distance = distance
#                                     destination = m
#                             if devices_temp[lucky_user].locate_BS[destination] == 1:
#                                 energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                                 energy_harvest_slot_length = config.time_slot_length - edge_transmit_latency
#                                 # print('energy harvest slot length =', energy_harvest_slot_length)
#                                 energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
#                                 # print('energy harvest ', energy_harvest)
#                             else:
#                                 energy_harvest = 0
#                             # 本地计算时间
#                             local_computing_portion = 1 - offload_computing_portion
#                             if local_computing_portion > 0:
#                                 local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
#                                 local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
#                                 # 本地计算时间
#                                 local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                                 # 本地计算能耗
#                                 local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
#                                 local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
#                                 local_computing_energy_cost = local_computing_latency * local_computing_power
#                             elif local_computing_portion == 0:
#                                 local_computing_cpu_demand = 0
#                                 local_execute_latency = 0
#                                 local_computing_energy_cost = 0
#                             else:
#                                 print('error')
#                             # 能量消耗
#                             energy_cost = local_computing_energy_cost + trans_energy_cost
#                             # 能量效用
#                             energy_utility = energy_cost - energy_harvest
#                             # print(energy_utility)
#                             # 边缘计算执行时间
#                             if offload_computing_portion > 0:
#                                 offload_computing_cpu_demand = cpu_frequency_demand * offload_computing_portion
#                                 edge_queue_length = execute_edge.task_queue_length() + offload_computing_cpu_demand
#                                 edge_computing_task_latency = edge_queue_length / execute_edge.frequency
#                             elif offload_computing_portion == 0:
#                                 edge_computing_task_latency = 0
#                             else:
#                                 print('error')
#                             edge_execute_latency = edge_transmit_latency + edge_computing_task_latency
#                             # 延迟效用
#                             latency_utility = max(local_execute_latency, edge_execute_latency)
#                             # 获取权重
#                             latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                             # 总效用
#                             total_edge_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                             lya = 0
#                             for m in range(0, config.total_number_of_devices):
#                                 # 计算lyapunov
#                                 cpu_frequency_demand_offload = 0
#                                 for n in range(0, config.total_number_of_devices):
#                                     if n != m and decisions.execute_mode[n] == 'device' and decisions.execute_destination[n] == m:
#                                         cpu_frequency_demand_lya = task_in_each_slot[time_slot][n].cpu_frequency_demand
#                                         local_computing_portion = decisions.local_computing_portion[n]
#                                         offload_computing_portion = (1 - local_computing_portion)
#                                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                                 if decisions.execute_mode[m] == 'local':
#                                     cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][m].cpu_frequency_demand
#                                 elif decisions.execute_mode[m] != 'null':
#                                     local_computing_portion = decisions.local_computing_portion[m]
#                                     cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][m].cpu_frequency_demand * local_computing_portion
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                                 queue_length = devices[m].task_queue_length() / config.task_cpu_frequency_demand
#                                 queue_length = queue_length / 8388608
#                                 lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                             total_edge_utility = total_edge_utility + config.V * lya
#                             #
#                             Y[k] = total_edge_utility
#                         # update_pbest
#                         for k in range(len(Y)):
#                             if pbest_y[k] > Y[k]:
#                                 pbest_x[k] = X[k].copy()
#                                 pbest_y[k] = Y[k].copy()
#                         # update_gbest
#                         idx_min = pbest_y.index(min(pbest_y))
#                         if gbest_y > pbest_y[idx_min]:
#                             gbest_x = pbest_x[idx_min].copy()  # copy很重要！
#                             gbest_y = pbest_y[idx_min]
#                         gbest_y_hist.append(gbest_y)
#                     this_total_utility = gbest_y
#                     # plt.plot(gbest_y_hist)
#                     # plt.show()
#                     if this_total_utility <= last_total_utility:
#                         decisions.execute_mode[lucky_user] = 'edge'
#                         decisions.execute_destination[lucky_user] = execute_edge_id
#                         decisions.local_computing_portion[lucky_user] = 1-gbest_x
#             elif rand == 3:
#                 choices = [0 for m in range(0, config.total_number_of_devices)]
#                 for j in range(0, config.total_number_of_edges):
#                     if devices_temp[lucky_user].locate_BS[j] == 1:
#                         for k in range(0, config.total_number_of_devices):
#                             if edges_temp[j].coverage_mobile_device[k] == 1:
#                                 choices[k] = 1
#                 choices_number = 0
#                 for j in range(0, config.total_number_of_devices):
#                     if choices[j] == 1:
#                         choices_number = choices_number + 1
#                 if choices_number == 0:
#                     # 不会走
#                     execute_mode = 'local'
#                     execute_destination = -1
#                 elif choices_number > 0:
#                     lucky_number = numpy.random.randint(1, choices_number + 1)
#                     for j in range(0, config.total_number_of_devices):
#                         if choices[j] == 1:
#                             lucky_number = lucky_number - 1
#                             if lucky_number == 0:
#                                 if lucky_user == j:
#                                     execute_mode = 'local'
#                                     execute_destination = -1
#                                 elif lucky_user != j:
#                                     execute_mode = 'device'
#                                     execute_destination = j
#                                 else:
#                                     print('error')
#                 else:
#                     print('error')
#                 # 计算效用
#                 if execute_mode == 'local':
#                     local_computing_size = devices_temp[lucky_user].task_queue_length() + cpu_frequency_demand
#                     local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                     latency_utility = local_execute_latency
#                     # 本地计算能耗
#                     local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency,3)
#                     local_computing_latency = cpu_frequency_demand / devices_temp[lucky_user].frequency
#                     energy_cost = local_computing_latency * local_computing_power
#                     # 收集能量
#                     min_distance = 4000
#                     destination = -1
#                     for j in range(0, len(devices_temp[lucky_user].distance_BS)):
#                         distance = devices_temp[lucky_user].distance_BS[j]
#                         if distance < min_distance:
#                             min_distance = distance
#                             destination = j
#                     if devices_temp[lucky_user].locate_BS[destination] == 1:
#                         energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                         energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * config.time_slot_length
#                         # print('energy_harvest', energy_harvest)
#                     else:
#                         energy_harvest = 0
#                     # 能量效用
#                     energy_utility = energy_cost - energy_harvest
#                     # 获取权重
#                     latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                     # 总效用
#                     total_local_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                     lya = 0
#                     for j in range(0, config.total_number_of_devices):
#                         # 计算lyapunov
#                         cpu_frequency_demand_offload = 0
#                         for k in range(0, config.total_number_of_devices):
#                             if k != j and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == j:
#                                 cpu_frequency_demand_lya = task_in_each_slot[time_slot][k].cpu_frequency_demand
#                                 local_computing_portion = decisions.local_computing_portion[k]
#                                 offload_computing_portion = (1 - local_computing_portion)
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                         if decisions.execute_mode[j] == 'local':
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand
#                         elif decisions.execute_mode[j] != 'null':
#                             local_computing_portion = decisions.local_computing_portion[j]
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][j].cpu_frequency_demand * local_computing_portion
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                         cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                         queue_length = devices[j].task_queue_length() / config.task_cpu_frequency_demand
#                         queue_length = queue_length / 8388608
#                         lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                     this_total_utility = total_local_utility + config.V * lya
#                     if this_total_utility <= last_total_utility:
#                         decisions.execute_mode[lucky_user] = 'local'
#                         decisions.execute_destination[lucky_user] = -1
#                         decisions.local_computing_portion[lucky_user] = 1
#                 elif execute_mode == 'device':
#                     execute_device_id = execute_destination
#                     execute_device = devices_temp[execute_device_id]
#                     interference = 0
#                     for j in range(0, config.total_number_of_devices):
#                         if j != lucky_user and decisions.execute_mode[j] == 'device' and decisions.execute_destination[j] == execute_device_id:
#                             gain = get_d2d_gain(device1=devices_temp[j], device2=execute_device)
#                             interference += gain
#                     d2d_rate = get_d2d_rate(device1=devices_temp[lucky_user], device2=execute_device, interference=interference)
#                     slot_d2d_data_size = d2d_rate * config.time_slot_length
#                     d2d_data_size_up_limit = min(slot_d2d_data_size, data_size)
#                     d2d_computing_portion_up_limit = d2d_data_size_up_limit / data_size
#                     X = numpy.random.uniform(low=0, high=d2d_computing_portion_up_limit, size=config.pop_size)
#                     X[0] = 0
#                     X[1] = d2d_computing_portion_up_limit
#                     Y = [0 for m in range(len(X))]
#                     for j in range(len(X)):
#                         d2d_computing_portion = X[j]
#                         if d2d_computing_portion > 0:
#                             d2d_data_size = data_size * d2d_computing_portion
#                             # 传输时间
#                             d2d_transmit_latency = d2d_data_size / d2d_rate
#                             d2d_transmit_latency = round(d2d_transmit_latency, 6)
#                             # print('d2d_transmit_latency', d2d_transmit_latency)
#                             # 传输能耗
#                             trans_energy_cost = d2d_transmit_latency * devices_temp[lucky_user].d2d_trans_power
#                         elif d2d_computing_portion == 0:
#                             # 传输时间
#                             d2d_transmit_latency = 0
#                             # 传输能耗
#                             trans_energy_cost = 0
#                         else:
#                             print('error')
#                         # 收集能量
#                         min_distance = 4000
#                         destination = -1
#                         for k in range(0, len(devices_temp[lucky_user].distance_BS)):
#                             distance = devices_temp[lucky_user].distance_BS[k]
#                             if distance < min_distance:
#                                 min_distance = distance
#                                 destination = k
#                         if devices_temp[lucky_user].locate_BS[destination] == 1:
#                             energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                             energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
#                             # print('energy harvest slot length =', energy_harvest_slot_length)
#                             energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
#                             # print('energy harvest ', energy_harvest)
#                         else:
#                             energy_harvest = 0
#                         # 本地计算时间
#                         local_computing_portion = 1 - d2d_computing_portion
#                         if local_computing_portion > 0:
#                             local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
#                             local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
#                             # 本地计算时间
#                             local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                             # 本地计算能耗
#                             local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
#                             local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
#                             local_computing_energy_cost = local_computing_latency * local_computing_power
#                         elif local_computing_portion == 0:
#                             local_computing_cpu_demand = 0
#                             local_execute_latency = 0
#                             local_computing_energy_cost = 0
#                         else:
#                             print('error')
#                         # 能量消耗
#                         energy_cost = local_computing_energy_cost + trans_energy_cost
#                         # 能量效用
#                         energy_utility = energy_cost - energy_harvest
#                         # print(energy_utility)
#                         # 边缘计算执行时间
#                         if d2d_computing_portion > 0:
#                             d2d_cpu_frequency_demand = cpu_frequency_demand * d2d_computing_portion
#                             device_queue_length = execute_device.task_queue_length() + d2d_cpu_frequency_demand
#                             d2d_computing_task_latency = device_queue_length / execute_device.frequency
#                         elif d2d_computing_portion == 0:
#                             d2d_computing_task_latency = 0
#                         else:
#                             print('error')
#                         d2d_execute_latency = d2d_transmit_latency + d2d_computing_task_latency
#                         # 延迟效用
#                         latency_utility = max(local_execute_latency, d2d_execute_latency)
#                         # 获取权重
#                         latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                         # 总效用
#                         total_d2d_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                         lya = 0
#                         for m in range(0, config.total_number_of_devices):
#                             # 计算lyapunov
#                             cpu_frequency_demand_offload = 0
#                             for k in range(0, config.total_number_of_devices):
#                                 if k != m and decisions.execute_mode[k] == 'device' and decisions.execute_destination[k] == m:
#                                     cpu_frequency_demand_lya = task_in_each_slot[time_slot][k].cpu_frequency_demand
#                                     local_computing_portion = decisions.local_computing_portion[k]
#                                     offload_computing_portion = (1 - local_computing_portion)
#                                     cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                             if decisions.execute_mode[m] == 'local':
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][m].cpu_frequency_demand
#                             elif decisions.execute_mode[m] != 'null':
#                                 local_computing_portion = decisions.local_computing_portion[m]
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][m].cpu_frequency_demand * local_computing_portion
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                             cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                             queue_length = devices[m].task_queue_length() / config.task_cpu_frequency_demand
#                             queue_length = queue_length / 8388608
#                             lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                         total_d2d_utility = total_d2d_utility + config.V * lya
#                         #
#                         Y[j] = total_d2d_utility
#                     pbest_x = X.copy()  # personal best location of every particle in history
#                     # self.pbest_x = self.X 表示地址传递,改变 X 值 pbest_x 也会变化
#                     pbest_y = [numpy.inf for m in range(config.pop_size)]  # best image of every particle in history
#                     # self.gbest_x = self.pbest_x.mean(axis=0).reshape(1, -1)  # global best location for all particles
#                     gbest_x = pbest_x.mean(axis=0)
#                     gbest_y = numpy.inf  # global best y for all particles
#                     gbest_y_hist = []  # gbest_y of every iteration
#                     for j in range(config.max_iter):
#                         # # update
#                         # r1 = config.a - j * (config.a / config.max_iter)
#                         # 抛物线函数
#                         iter_period = j / config.max_iter
#                         inter_rest_phase = 1 - iter_period
#                         square = pow(inter_rest_phase, 2)
#                         r1 = config.a * square
#                         for k in range(config.pop_size):
#                             r2 = 2 * math.pi * random.uniform(0.0, 1.0)
#                             r3 = 2 * random.uniform(0.0, 1.0)
#                             r4 = random.uniform(0.0, 1.0)
#                             if r4 < 0.5:
#                                 X[k] = X[k] + (r1 * math.sin(r2) * abs(r3 * gbest_x - X[k]))
#                             else:
#                                 X[k] = X[k] + (r1 * math.cos(r2) * abs(r3 * gbest_x - X[k]))
#                         X = numpy.clip(a=X, a_min=0, a_max=d2d_computing_portion_up_limit)
#                         for k in range(len(X)):
#                             d2d_computing_portion = X[k]
#                             if d2d_computing_portion > 0:
#                                 d2d_data_size = data_size * d2d_computing_portion
#                                 # 传输时间
#                                 d2d_transmit_latency = d2d_data_size / d2d_rate
#                                 d2d_transmit_latency = round(d2d_transmit_latency, 6)
#                                 # print('d2d_transmit_latency', d2d_transmit_latency)
#                                 # 传输能耗
#                                 trans_energy_cost = d2d_transmit_latency * devices_temp[lucky_user].d2d_trans_power
#                             elif d2d_computing_portion == 0:
#                                 # 传输时间
#                                 d2d_transmit_latency = 0
#                                 # 传输能耗
#                                 trans_energy_cost = 0
#                             else:
#                                 print('error')
#                             # 收集能量
#                             min_distance = 4000
#                             destination = -1
#                             for m in range(0, len(devices_temp[lucky_user].distance_BS)):
#                                 distance = devices_temp[lucky_user].distance_BS[m]
#                                 if distance < min_distance:
#                                     min_distance = distance
#                                     destination = m
#                             if devices_temp[lucky_user].locate_BS[destination] == 1:
#                                 energy_harvest_gain = config.ENERGY_CHANNEL_GAIN
#                                 energy_harvest_slot_length = config.time_slot_length - d2d_transmit_latency
#                                 # print('energy harvest slot length =', energy_harvest_slot_length)
#                                 energy_harvest = config.ENERGY_CONVERSION_EFFICIENCY * edges_temp[destination].trans_power * energy_harvest_gain * energy_harvest_slot_length
#                                 # print('energy harvest ', energy_harvest)
#                             else:
#                                 energy_harvest = 0
#                             # 本地计算时间
#                             local_computing_portion = 1 - d2d_computing_portion
#                             if local_computing_portion > 0:
#                                 local_computing_cpu_demand = cpu_frequency_demand * local_computing_portion
#                                 local_computing_size = devices_temp[lucky_user].task_queue_length() + local_computing_cpu_demand
#                                 # 本地计算时间
#                                 local_execute_latency = local_computing_size / devices_temp[lucky_user].frequency
#                                 # 本地计算能耗
#                                 local_computing_power = config.SWITCHED_CAPACITANCE * math.pow(devices_temp[lucky_user].frequency, 3)
#                                 local_computing_latency = local_computing_cpu_demand / devices_temp[lucky_user].frequency
#                                 local_computing_energy_cost = local_computing_latency * local_computing_power
#                             elif local_computing_portion == 0:
#                                 local_computing_cpu_demand = 0
#                                 local_execute_latency = 0
#                                 local_computing_energy_cost = 0
#                             else:
#                                 print('error')
#                             # 能量消耗
#                             energy_cost = local_computing_energy_cost + trans_energy_cost
#                             # 能量效用
#                             energy_utility = energy_cost - energy_harvest
#                             # print(energy_utility)
#                             # 边缘计算执行时间
#                             if d2d_computing_portion > 0:
#                                 d2d_cpu_frequency_demand = cpu_frequency_demand * d2d_computing_portion
#                                 device_queue_length = execute_device.task_queue_length() + d2d_cpu_frequency_demand
#                                 d2d_computing_task_latency = device_queue_length / execute_device.frequency
#                             elif d2d_computing_portion == 0:
#                                 d2d_computing_task_latency = 0
#                             else:
#                                 print('error')
#                             d2d_execute_latency = d2d_transmit_latency + d2d_computing_task_latency
#                             # 延迟效用
#                             latency_utility = max(local_execute_latency, d2d_execute_latency)
#                             # 获取权重
#                             latency_weight, energy_weight = devices_temp[lucky_user].get_weight()
#                             # 总效用
#                             total_d2d_utility = latency_weight * latency_utility + energy_weight * energy_utility
#                             lya = 0
#                             for m in range(0, config.total_number_of_devices):
#                                 # 计算lyapunov
#                                 cpu_frequency_demand_offload = 0
#                                 for n in range(0, config.total_number_of_devices):
#                                     if n != m and decisions.execute_mode[n] == 'device' and decisions.execute_destination[n] == m:
#                                         cpu_frequency_demand_lya = task_in_each_slot[time_slot][n].cpu_frequency_demand
#                                         local_computing_portion = decisions.local_computing_portion[n]
#                                         offload_computing_portion = (1 - local_computing_portion)
#                                         cpu_frequency_demand_offload = cpu_frequency_demand_offload + cpu_frequency_demand_lya * offload_computing_portion
#                                 if decisions.execute_mode[m] == 'local':
#                                     cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][m].cpu_frequency_demand
#                                 elif decisions.execute_mode[m] != 'null':
#                                     local_computing_portion = decisions.local_computing_portion[m]
#                                     cpu_frequency_demand_offload = cpu_frequency_demand_offload + task_in_each_slot[time_slot][m].cpu_frequency_demand * local_computing_portion
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload / config.task_cpu_frequency_demand
#                                 cpu_frequency_demand_offload = cpu_frequency_demand_offload / 8388608
#                                 queue_length = devices[m].task_queue_length() / config.task_cpu_frequency_demand
#                                 queue_length = queue_length / 8388608
#                                 lya = lya + pow(cpu_frequency_demand_offload, 2) + 2 * queue_length * cpu_frequency_demand_offload
#                             total_d2d_utility = total_d2d_utility + config.V * lya
#                             #
#                             Y[k] = total_d2d_utility
#                         # update_pbest
#                         for k in range(len(Y)):
#                             if pbest_y[k] > Y[k]:
#                                 pbest_x[k] = X[k].copy()
#                                 pbest_y[k] = Y[k].copy()
#                         # update_gbest
#                         idx_min = pbest_y.index(min(pbest_y))
#                         if gbest_y > pbest_y[idx_min]:
#                             gbest_x = pbest_x[idx_min].copy()  # copy很重要！
#                             gbest_y = pbest_y[idx_min].copy()
#                         gbest_y_hist.append(gbest_y)
#                     this_total_utility = gbest_y
#                     # plt.plot(gbest_y_hist)
#                     # plt.show()
#                     if this_total_utility <= last_total_utility:
#                         decisions.execute_mode[lucky_user] = 'device'
#                         decisions.execute_destination[lucky_user] = execute_device_id
#                         decisions.local_computing_portion[lucky_user] = 1-gbest_x
#         elif decisions.execute_mode[lucky_user] == 'null':
#             pass
#         else:
#             pass
#     return decisions



if __name__ == '__main__':
    for i in range(1000):
        print(numpy.random.randint(1, 4))