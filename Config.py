
# 20个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 20

        self.total_number_of_active_devices = 13

        self.total_number_of_passive_devices = 7

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 300

        self.iterations_number_of_proposed_algorithm = 200

        self.generating_tasks_probability_of_active_device = 0.6

        self.generating_tasks_probability_of_passive_device = 0.4

        # 时隙长度 100ms
        self.time_slot_length = 0.1

        # 1 GHZ  cycles/s = 1
        self.activate_device_cpu_frequency = 3 * (10 ** 9)

        self.passive_device_cpu_frequency = 5 * (10 ** 9)

        # 边缘服务器的算力
        self.edge_cpu_frequency = 10 * (10 ** 9)

        self.SWITCHED_CAPACITANCE = 10 ** -28

        self.ENERGY_CONVERSION_EFFICIENCY = 1

        # [0.2, 0.4] MB   (1 MB = 1024 KB = 1,048,576 Bytes = 8,388,608 bits)
        self.task_size = [1677721.6, 3355443.2]

        # 1000 cycles/bit
        self.task_cpu_frequency_demand = 1000

        self.max_energy_queue_length = 5000

        # -100 dBm = 10 ** -13 W
        self.GAUSSIAN_WHITE_NOISE_POWER = 10 ** -13

        # 30MHZ
        self.OFFLOAD_BANDWIDTH = 30000000

        # 1MHZ
        self.D2D_BANDWIDTH = 2000000

        self.D2D_CHANNEL_GAIN = 1

        # self.EDGE_CHANNEL_GAIN = 10 ** -4

        # - 50dB
        self.EDGE_CHANNEL_GAIN = 10 ** -4

        self.ENERGY_CHANNEL_GAIN = 0.1

        self.RSU_PATH_LOSS_EXPONENT = 4

        self.MIN_X_LOCATION = 0

        self.MAX_X_LOCATION = 500

        self.MIN_Y_LOCATION = 0

        self.MAX_Y_LOCATION = 500

        # 移动速度 10m/s
        self.MOVE_DISTANCE = 10

        self.edge_locations = [[125, 125], [125, 375], [375, 125], [375, 375]]

        self.coverage_radius = 200

        # sca 参数设置
        self.pop_size = 60
        self.a = 2 # 感知概率
        self.max_iter = 500  # max iter

        # self.algorithm = 'local_algorithm'
        # self.algorithm = 'nearest_algorithm'
        # self.algorithm = 'random_algorithm'
        # self.algorithm = 'match_algorithm'
        # self.algorithm = 'dot_algorithm'
        self.algorithm = 'proposed_algorithm'
        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'proposed_algorithm'

        # IoTJ: Joint Task Offloading, D2D Pairing, and Resource Allocation in Device-Enhanced MEC: A Potential Game Approach

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False
        self.devices_cache_file_path = './cache/Devices20.cache'
        self.edges_cache_file_path = './cache/Edges20.cache'
        self.task_cache_file_path = './cache/Task20.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks20.cache'
        self.x_location_in_each_slot_file_path = './cache/XLocation20.cache'
        self.y_location_in_each_slot_file_path = './cache/YLocation20.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath20.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath20.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath20.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath20.cache'
        self.dot_ave_queue_length_in_each_slot_file_path = './result/DotAveQueueLengthInEachSlotFilePath20.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath20.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath20.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath20.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath20.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath20.cache'
        self.dot_ave_execute_latency_in_each_slot_file_path = './result/DotAveExecuteLatencyInEachSlotFilePath20.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath20.cache'

        self.local_energy_consumption_in_each_slot_file_path = './result/LocalEnergyConsumptionInEachSlotFilePath20.cache'
        self.nearest_energy_consumption_in_each_slot_file_path = './result/NearestEnergyConsumptionInEachSlotFilePath20.cache'
        self.random_energy_consumption_in_each_slot_file_path = './result/RandomEnergyConsumptionInEachSlotFilePath20.cache'
        self.match_energy_consumption_in_each_slot_file_path = './result/MatchEnergyConsumptionInEachSlotFilePath20.cache'
        self.dot_energy_consumption_in_each_slot_file_path = './result/DotEnergyConsumptionInEachSlotFilePath20.cache'
        self.proposed_energy_consumption_in_each_slot_file_path = './result/ProposedEnergyConsumptionInEachSlotFilePath20.cache'

        self.local_energy_harvest_in_each_slot_file_path = './result/LocalEnergyHarvestInEachSlotFilePath20.cache'
        self.nearest_energy_harvest_in_each_slot_file_path = './result/NearestEnergyHarvestInEachSlotFilePath20.cache'
        self.random_energy_harvest_in_each_slot_file_path = './result/RandomEnergyHarvestInEachSlotFilePath20.cache'
        self.match_energy_harvest_in_each_slot_file_path = './result/MatchEnergyHarvestInEachSlotFilePath20.cache'
        self.dot_energy_harvest_in_each_slot_file_path = './result/DotEnergyHarvestInEachSlotFilePath20.cache'
        self.proposed_energy_harvest_in_each_slot_file_path = './result/ProposedEnergyHarvestInEachSlotFilePath20.cache'

        self.local_energy_cost_in_each_slot_file_path = './result/LocalEnergyCostInEachSlotFilePath20.cache'
        self.nearest_energy_cost_in_each_slot_file_path = './result/NearestEnergyCostInEachSlotFilePath20.cache'
        self.random_energy_cost_in_each_slot_file_path = './result/RandomEnergyCostInEachSlotFilePath20.cache'
        self.match_energy_cost_in_each_slot_file_path = './result/MatchEnergyCostInEachSlotFilePath20.cache'
        self.dot_energy_cost_in_each_slot_file_path = './result/DotEnergyCostInEachSlotFilePath20.cache'
        self.proposed_energy_cost_in_each_slot_file_path = './result/ProposedEnergyCostInEachSlotFilePath20.cache'

        self.local_latency_cost_in_each_slot_file_path = './result/LocalLatencyCostInEachSlotFilePath20.cache'
        self.nearest_latency_cost_in_each_slot_file_path = './result/NearestLatencyCostInEachSlotFilePath20.cache'
        self.random_latency_cost_in_each_slot_file_path = './result/RandomLatencyCostInEachSlotFilePath20.cache'
        self.match_latency_cost_in_each_slot_file_path = './result/MatchLatencyCostInEachSlotFilePath20.cache'
        self.dot_latency_cost_in_each_slot_file_path = './result/DotLatencyCostInEachSlotFilePath20.cache'
        self.proposed_latency_cost_in_each_slot_file_path = './result/ProposedLatencyCostInEachSlotFilePath20.cache'

        self.local_total_cost_in_each_slot_file_path = './result/LocalTotalCostInEachSlotFilePath20.cache'
        self.nearest_total_cost_in_each_slot_file_path = './result/NearestTotalCostInEachSlotFilePath20.cache'
        self.random_total_cost_in_each_slot_file_path = './result/RandomTotalCostInEachSlotFilePath20.cache'
        self.match_total_cost_in_each_slot_file_path = './result/MatchTotalCostInEachSlotFilePath20.cache'
        self.dot_total_cost_in_each_slot_file_path = './result/DotTotalCostInEachSlotFilePath20.cache'
        self.proposed_total_cost_in_each_slot_file_path = './result/ProposedTotalCostInEachSlotFilePath20.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath20.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath20.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath20.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath20.cache'
        self.dot_io_in_each_slot_file_path = './result/DotIOInEachSlotFilePath20.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath20.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath20.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath20.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath20.cache'