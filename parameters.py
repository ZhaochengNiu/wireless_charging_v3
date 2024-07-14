
# 10个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 10

        self.total_number_of_active_devices = 6

        self.total_number_of_passive_devices = 4

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 100

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

        # [0.1, 0.3] MB   (1 MB = 1024 KB = 1,048,576 Bytes = 8,388,608 bits)
        self.task_size = [838860.8, 2516582.4]

        # 1000 cycles/bit
        self.task_cpu_frequency_demand = 1000

        self.max_energy_queue_length = 5000

        # -100 dBm = 10 ** -13 W
        self.GAUSSIAN_WHITE_NOISE_POWER = 10 ** -13

        # 30MHZ
        self.OFFLOAD_BANDWIDTH = 5000000

        # 1MHZ
        self.D2D_BANDWIDTH = 1000000

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

        self.coverage_radius = 120

        # sca 参数设置
        self.pop_size = 60
        self.a = 2 # 感知概率
        self.max_iter = 500  # max iter

        self.algorithm = 'local_algorithm'
        # self.algorithm = 'nearest_algorithm'
        # self.algorithm = 'random_algorithm'
        # self.algorithm = 'match_algorithm'
        # self.algorithm = 'proposed_algorithm'
        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'proposed_algorithm'

        # IoTJ: Joint Task Offloading, D2D Pairing, and Resource Allocation in Device-Enhanced MEC: A Potential Game Approach

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False
        self.devices_cache_file_path = './cache/Devices10.cache'
        self.edges_cache_file_path = './cache/Edges10.cache'
        self.task_cache_file_path = './cache/Task10.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks10.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath10.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath10.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath10.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath10.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath10.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath10.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath10.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath10.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath10.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath10.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath10.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath10.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath10.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath10.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath10.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath10.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath10.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath10.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath10.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath10.cache'

        self.local_total_energy_harvest_in_each_slot_file_path = './result/LocalTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.nearest_total_energy_harvest_in_each_slot_file_path = './result/NearestTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.random_total_energy_harvest_in_each_slot_file_path = './result/RandomTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.match_total_energy_harvest_in_each_slot_file_path = './result/MatchTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.proposed_total_energy_harvest_in_each_slot_file_path = './result/ProposedTotalEnergyHarvestInEachSlotFilePath10.cache'

        self.local_energy_utility_in_each_slot_file_path = './result/LocalEnergyUtilityInEachSlotFilePath10.cache'
        self.nearest_energy_utility_in_each_slot_file_path = './result/NearestEnergyUtilityInEachSlotFilePath10.cache'
        self.random_energy_utility_in_each_slot_file_path = './result/RandomEnergyUtilityInEachSlotFilePath10.cache'
        self.match_energy_utility_in_each_slot_file_path = './result/MatchEnergyUtilityInEachSlotFilePath10.cache'
        self.proposed_energy_utility_in_each_slot_file_path = './result/ProposedEnergyUtilityInEachSlotFilePath10.cache'

        self.local_latency_utility_in_each_slot_file_path = './result/LocalLatencyUtilityInEachSlotFilePath10.cache'
        self.nearest_latency_utility_in_each_slot_file_path = './result/NearestLatencyUtilityInEachSlotFilePath10.cache'
        self.random_latency_utility_in_each_slot_file_path = './result/RandomLatencyUtilityInEachSlotFilePath10.cache'
        self.match_latency_utility_in_each_slot_file_path = './result/MatchLatencyUtilityInEachSlotFilePath10.cache'
        self.proposed_latency_utility_in_each_slot_file_path = './result/ProposedLatencyUtilityInEachSlotFilePath10.cache'

        self.local_total_utility_in_each_slot_file_path = './result/LocalTotalUtilityInEachSlotFilePath10.cache'
        self.nearest_total_utility_in_each_slot_file_path = './result/NearestTotalUtilityInEachSlotFilePath10.cache'
        self.random_total_utility_in_each_slot_file_path = './result/RandomTotalUtilityInEachSlotFilePath10.cache'
        self.match_total_utility_in_each_slot_file_path = './result/MatchTotalUtilityInEachSlotFilePath10.cache'
        self.proposed_total_utility_in_each_slot_file_path = './result/ProposedTotalUtilityInEachSlotFilePath10.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath10.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath10.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath10.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath10.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath10.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath10.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath10.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath10.cache'


========================================================================================================================

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

        self.iterations_number_of_game_theory = 100

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

        # [0.1, 0.3] MB   (1 MB = 1024 KB = 1,048,576 Bytes = 8,388,608 bits)
        self.task_size = [838860.8, 2516582.4]

        # 1000 cycles/bit
        self.task_cpu_frequency_demand = 1000

        self.max_energy_queue_length = 5000

        # -100 dBm = 10 ** -13 W
        self.GAUSSIAN_WHITE_NOISE_POWER = 10 ** -13

        # 30MHZ
        self.OFFLOAD_BANDWIDTH = 5000000

        # 1MHZ
        self.D2D_BANDWIDTH = 1000000

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

        self.coverage_radius = 120

        # sca 参数设置
        self.pop_size = 60
        self.a = 2 # 感知概率
        self.max_iter = 500  # max iter

        # self.algorithm = 'local_algorithm'
        # self.algorithm = 'nearest_algorithm'
        # self.algorithm = 'random_algorithm'
        # self.algorithm = 'match_algorithm'
        self.algorithm = 'proposed_algorithm'
        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'proposed_algorithm'

        # IoTJ: Joint Task Offloading, D2D Pairing, and Resource Allocation in Device-Enhanced MEC: A Potential Game Approach

        # 缓存设置
        self.cache = True
        # True False
        self.devices_cache_file_path = './cache/Devices20.cache'
        self.edges_cache_file_path = './cache/Edges20.cache'
        self.task_cache_file_path = './cache/Task20.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks20.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath20.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath20.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath20.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath20.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath20.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath20.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath20.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath20.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath20.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath20.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath20.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath20.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath20.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath20.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath20.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath20.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath20.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath20.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath20.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath20.cache'

        self.local_total_energy_harvest_in_each_slot_file_path = './result/LocalTotalEnergyHarvestInEachSlotFilePath20.cache'
        self.nearest_total_energy_harvest_in_each_slot_file_path = './result/NearestTotalEnergyHarvestInEachSlotFilePath20.cache'
        self.random_total_energy_harvest_in_each_slot_file_path = './result/RandomTotalEnergyHarvestInEachSlotFilePath20.cache'
        self.match_total_energy_harvest_in_each_slot_file_path = './result/MatchTotalEnergyHarvestInEachSlotFilePath20.cache'
        self.proposed_total_energy_harvest_in_each_slot_file_path = './result/ProposedTotalEnergyHarvestInEachSlotFilePath20.cache'

        self.local_energy_utility_in_each_slot_file_path = './result/LocalEnergyUtilityInEachSlotFilePath20.cache'
        self.nearest_energy_utility_in_each_slot_file_path = './result/NearestEnergyUtilityInEachSlotFilePath20.cache'
        self.random_energy_utility_in_each_slot_file_path = './result/RandomEnergyUtilityInEachSlotFilePath20.cache'
        self.match_energy_utility_in_each_slot_file_path = './result/MatchEnergyUtilityInEachSlotFilePath20.cache'
        self.proposed_energy_utility_in_each_slot_file_path = './result/ProposedEnergyUtilityInEachSlotFilePath20.cache'

        self.local_latency_utility_in_each_slot_file_path = './result/LocalLatencyUtilityInEachSlotFilePath20.cache'
        self.nearest_latency_utility_in_each_slot_file_path = './result/NearestLatencyUtilityInEachSlotFilePath20.cache'
        self.random_latency_utility_in_each_slot_file_path = './result/RandomLatencyUtilityInEachSlotFilePath20.cache'
        self.match_latency_utility_in_each_slot_file_path = './result/MatchLatencyUtilityInEachSlotFilePath20.cache'
        self.proposed_latency_utility_in_each_slot_file_path = './result/ProposedLatencyUtilityInEachSlotFilePath20.cache'

        self.local_total_utility_in_each_slot_file_path = './result/LocalTotalUtilityInEachSlotFilePath20.cache'
        self.nearest_total_utility_in_each_slot_file_path = './result/NearestTotalUtilityInEachSlotFilePath20.cache'
        self.random_total_utility_in_each_slot_file_path = './result/RandomTotalUtilityInEachSlotFilePath20.cache'
        self.match_total_utility_in_each_slot_file_path = './result/MatchTotalUtilityInEachSlotFilePath20.cache'
        self.proposed_total_utility_in_each_slot_file_path = './result/ProposedTotalUtilityInEachSlotFilePath20.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath20.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath20.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath20.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath20.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath20.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath20.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath20.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath20.cache'

========================================================================================================================

# 30 个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 30

        self.total_number_of_active_devices = 15

        self.total_number_of_passive_devices = 15

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 100

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

        # [0.1, 0.3] MB   (1 MB = 1024 KB = 1,048,576 Bytes = 8,388,608 bits)
        self.task_size = [838860.8, 2516582.4]

        # 1000 cycles/bit
        self.task_cpu_frequency_demand = 1000

        self.max_energy_queue_length = 5000

        # -100 dBm = 10 ** -13 W
        self.GAUSSIAN_WHITE_NOISE_POWER = 10 ** -13

        # 30MHZ
        self.OFFLOAD_BANDWIDTH = 5000000

        # 1MHZ
        self.D2D_BANDWIDTH = 1000000

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

        self.coverage_radius = 120

        # sca 参数设置
        self.pop_size = 60
        self.a = 2 # 感知概率
        self.max_iter = 500  # max iter

        # self.algorithm = 'local_algorithm'
        # self.algorithm = 'nearest_algorithm'
        # self.algorithm = 'random_algorithm'
        # self.algorithm = 'match_algorithm'
        self.algorithm = 'proposed_algorithm'
        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'proposed_algorithm'

        # IoTJ: Joint Task Offloading, D2D Pairing, and Resource Allocation in Device-Enhanced MEC: A Potential Game Approach

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False

        self.devices_cache_file_path = './cache/Devices30.cache'
        self.edges_cache_file_path = './cache/Edges30.cache'
        self.task_cache_file_path = './cache/Task30.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks30.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath30.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath30.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath30.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath30.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath30.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath30.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath30.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath30.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath30.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath30.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath30.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath30.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath30.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath30.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath30.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath30.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath30.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath30.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath30.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath30.cache'

        self.local_total_energy_harvest_in_each_slot_file_path = './result/LocalTotalEnergyHarvestInEachSlotFilePath30.cache'
        self.nearest_total_energy_harvest_in_each_slot_file_path = './result/NearestTotalEnergyHarvestInEachSlotFilePath30.cache'
        self.random_total_energy_harvest_in_each_slot_file_path = './result/RandomTotalEnergyHarvestInEachSlotFilePath30.cache'
        self.match_total_energy_harvest_in_each_slot_file_path = './result/MatchTotalEnergyHarvestInEachSlotFilePath30.cache'
        self.proposed_total_energy_harvest_in_each_slot_file_path = './result/ProposedTotalEnergyHarvestInEachSlotFilePath30.cache'

        self.local_energy_utility_in_each_slot_file_path = './result/LocalEnergyUtilityInEachSlotFilePath30.cache'
        self.nearest_energy_utility_in_each_slot_file_path = './result/NearestEnergyUtilityInEachSlotFilePath30.cache'
        self.random_energy_utility_in_each_slot_file_path = './result/RandomEnergyUtilityInEachSlotFilePath30.cache'
        self.match_energy_utility_in_each_slot_file_path = './result/MatchEnergyUtilityInEachSlotFilePath30.cache'
        self.proposed_energy_utility_in_each_slot_file_path = './result/ProposedEnergyUtilityInEachSlotFilePath30.cache'

        self.local_latency_utility_in_each_slot_file_path = './result/LocalLatencyUtilityInEachSlotFilePath30.cache'
        self.nearest_latency_utility_in_each_slot_file_path = './result/NearestLatencyUtilityInEachSlotFilePath30.cache'
        self.random_latency_utility_in_each_slot_file_path = './result/RandomLatencyUtilityInEachSlotFilePath30.cache'
        self.match_latency_utility_in_each_slot_file_path = './result/MatchLatencyUtilityInEachSlotFilePath30.cache'
        self.proposed_latency_utility_in_each_slot_file_path = './result/ProposedLatencyUtilityInEachSlotFilePath30.cache'

        self.local_total_utility_in_each_slot_file_path = './result/LocalTotalUtilityInEachSlotFilePath30.cache'
        self.nearest_total_utility_in_each_slot_file_path = './result/NearestTotalUtilityInEachSlotFilePath30.cache'
        self.random_total_utility_in_each_slot_file_path = './result/RandomTotalUtilityInEachSlotFilePath30.cache'
        self.match_total_utility_in_each_slot_file_path = './result/MatchTotalUtilityInEachSlotFilePath30.cache'
        self.proposed_total_utility_in_each_slot_file_path = './result/ProposedTotalUtilityInEachSlotFilePath30.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath30.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath30.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath30.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath30.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath30.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath30.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath30.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath30.cache'

========================================================================================================================

# 40 个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 40

        self.total_number_of_active_devices = 20

        self.total_number_of_passive_devices = 20

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 100

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

        # [0.1, 0.3] MB   (1 MB = 1024 KB = 1,048,576 Bytes = 8,388,608 bits)
        self.task_size = [838860.8, 2516582.4]

        # 1000 cycles/bit
        self.task_cpu_frequency_demand = 1000

        self.max_energy_queue_length = 5000

        # -100 dBm = 10 ** -13 W
        self.GAUSSIAN_WHITE_NOISE_POWER = 10 ** -13

        # 30MHZ
        self.OFFLOAD_BANDWIDTH = 5000000

        # 1MHZ
        self.D2D_BANDWIDTH = 1000000

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

        self.coverage_radius = 120

        # sca 参数设置
        self.pop_size = 60
        self.a = 2 # 感知概率
        self.max_iter = 500  # max iter

        # self.algorithm = 'local_algorithm'
        # self.algorithm = 'nearest_algorithm'
        # self.algorithm = 'random_algorithm'
        self.algorithm = 'match_algorithm'
        # self.algorithm = 'proposed_algorithm'
        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'proposed_algorithm'

        # IoTJ: Joint Task Offloading, D2D Pairing, and Resource Allocation in Device-Enhanced MEC: A Potential Game Approach

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False

        self.devices_cache_file_path = './cache/Devices40.cache'
        self.edges_cache_file_path = './cache/Edges40.cache'
        self.task_cache_file_path = './cache/Task40.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks40.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath40.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath40.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath40.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath40.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath40.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath40.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath40.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath40.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath40.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath40.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath40.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath40.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath40.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath40.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath40.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath40.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath40.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath40.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath40.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath40.cache'

        self.local_total_energy_harvest_in_each_slot_file_path = './result/LocalTotalEnergyHarvestInEachSlotFilePath40.cache'
        self.nearest_total_energy_harvest_in_each_slot_file_path = './result/NearestTotalEnergyHarvestInEachSlotFilePath40.cache'
        self.random_total_energy_harvest_in_each_slot_file_path = './result/RandomTotalEnergyHarvestInEachSlotFilePath40.cache'
        self.match_total_energy_harvest_in_each_slot_file_path = './result/MatchTotalEnergyHarvestInEachSlotFilePath40.cache'
        self.proposed_total_energy_harvest_in_each_slot_file_path = './result/ProposedTotalEnergyHarvestInEachSlotFilePath40.cache'

        self.local_energy_utility_in_each_slot_file_path = './result/LocalEnergyUtilityInEachSlotFilePath40.cache'
        self.nearest_energy_utility_in_each_slot_file_path = './result/NearestEnergyUtilityInEachSlotFilePath40.cache'
        self.random_energy_utility_in_each_slot_file_path = './result/RandomEnergyUtilityInEachSlotFilePath40.cache'
        self.match_energy_utility_in_each_slot_file_path = './result/MatchEnergyUtilityInEachSlotFilePath40.cache'
        self.proposed_energy_utility_in_each_slot_file_path = './result/ProposedEnergyUtilityInEachSlotFilePath40.cache'

        self.local_latency_utility_in_each_slot_file_path = './result/LocalLatencyUtilityInEachSlotFilePath40.cache'
        self.nearest_latency_utility_in_each_slot_file_path = './result/NearestLatencyUtilityInEachSlotFilePath40.cache'
        self.random_latency_utility_in_each_slot_file_path = './result/RandomLatencyUtilityInEachSlotFilePath40.cache'
        self.match_latency_utility_in_each_slot_file_path = './result/MatchLatencyUtilityInEachSlotFilePath40.cache'
        self.proposed_latency_utility_in_each_slot_file_path = './result/ProposedLatencyUtilityInEachSlotFilePath40.cache'

        self.local_total_utility_in_each_slot_file_path = './result/LocalTotalUtilityInEachSlotFilePath40.cache'
        self.nearest_total_utility_in_each_slot_file_path = './result/NearestTotalUtilityInEachSlotFilePath40.cache'
        self.random_total_utility_in_each_slot_file_path = './result/RandomTotalUtilityInEachSlotFilePath40.cache'
        self.match_total_utility_in_each_slot_file_path = './result/MatchTotalUtilityInEachSlotFilePath40.cache'
        self.proposed_total_utility_in_each_slot_file_path = './result/ProposedTotalUtilityInEachSlotFilePath40.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath40.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath40.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath40.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath40.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath40.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath40.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath40.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath40.cache'

========================================================================================================================


class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 50

        self.total_number_of_active_devices = 25

        self.total_number_of_passive_devices = 25

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 100

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

        # [0.1, 0.3] MB   (1 MB = 1024 KB = 1,048,576 Bytes = 8,388,608 bits)
        self.task_size = [838860.8, 2516582.4]

        # 1000 cycles/bit
        self.task_cpu_frequency_demand = 1000

        self.max_energy_queue_length = 5000

        # -100 dBm = 10 ** -13 W
        self.GAUSSIAN_WHITE_NOISE_POWER = 10 ** -13

        # 30MHZ
        self.OFFLOAD_BANDWIDTH = 5000000

        # 1MHZ
        self.D2D_BANDWIDTH = 1000000

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

        self.coverage_radius = 120

        # sca 参数设置
        self.pop_size = 60
        self.a = 2 # 感知概率
        self.max_iter = 500  # max iter

        # self.algorithm = 'local_algorithm'
        # self.algorithm = 'nearest_algorithm'
        # self.algorithm = 'random_algorithm'
        # self.algorithm = 'match_algorithm'
        self.algorithm = 'proposed_algorithm'
        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'proposed_algorithm'

        # IoTJ: Joint Task Offloading, D2D Pairing, and Resource Allocation in Device-Enhanced MEC: A Potential Game Approach

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False

        self.devices_cache_file_path = './cache/Devices50.cache'
        self.edges_cache_file_path = './cache/Edges50.cache'
        self.task_cache_file_path = './cache/Task50.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks50.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath50.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath50.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath50.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath50.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath50.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath50.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath50.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath50.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath50.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath50.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath50.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath50.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath50.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath50.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath50.cache'

        self.local_total_energy_harvest_in_each_slot_file_path = './result/LocalTotalEnergyHarvestInEachSlotFilePath50.cache'
        self.nearest_total_energy_harvest_in_each_slot_file_path = './result/NearestTotalEnergyHarvestInEachSlotFilePath50.cache'
        self.random_total_energy_harvest_in_each_slot_file_path = './result/RandomTotalEnergyHarvestInEachSlotFilePath50.cache'
        self.match_total_energy_harvest_in_each_slot_file_path = './result/MatchTotalEnergyHarvestInEachSlotFilePath50.cache'
        self.proposed_total_energy_harvest_in_each_slot_file_path = './result/ProposedTotalEnergyHarvestInEachSlotFilePath50.cache'

        self.local_energy_utility_in_each_slot_file_path = './result/LocalEnergyUtilityInEachSlotFilePath50.cache'
        self.nearest_energy_utility_in_each_slot_file_path = './result/NearestEnergyUtilityInEachSlotFilePath50.cache'
        self.random_energy_utility_in_each_slot_file_path = './result/RandomEnergyUtilityInEachSlotFilePath50.cache'
        self.match_energy_utility_in_each_slot_file_path = './result/MatchEnergyUtilityInEachSlotFilePath50.cache'
        self.proposed_energy_utility_in_each_slot_file_path = './result/ProposedEnergyUtilityInEachSlotFilePath50.cache'

        self.local_latency_utility_in_each_slot_file_path = './result/LocalLatencyUtilityInEachSlotFilePath50.cache'
        self.nearest_latency_utility_in_each_slot_file_path = './result/NearestLatencyUtilityInEachSlotFilePath50.cache'
        self.random_latency_utility_in_each_slot_file_path = './result/RandomLatencyUtilityInEachSlotFilePath50.cache'
        self.match_latency_utility_in_each_slot_file_path = './result/MatchLatencyUtilityInEachSlotFilePath50.cache'
        self.proposed_latency_utility_in_each_slot_file_path = './result/ProposedLatencyUtilityInEachSlotFilePath50.cache'

        self.local_total_utility_in_each_slot_file_path = './result/LocalTotalUtilityInEachSlotFilePath50.cache'
        self.nearest_total_utility_in_each_slot_file_path = './result/NearestTotalUtilityInEachSlotFilePath50.cache'
        self.random_total_utility_in_each_slot_file_path = './result/RandomTotalUtilityInEachSlotFilePath50.cache'
        self.match_total_utility_in_each_slot_file_path = './result/MatchTotalUtilityInEachSlotFilePath50.cache'
        self.proposed_total_utility_in_each_slot_file_path = './result/ProposedTotalUtilityInEachSlotFilePath50.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath50.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath50.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath50.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath50.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath50.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath50.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath50.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath50.cache'

==================================================================================================================

# 第二轮配置
#
# 尝试加大任务量，和通信带宽

===================================================================================================================

# 10个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 10

        self.total_number_of_active_devices = 6

        self.total_number_of_passive_devices = 4

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 100

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
        self.algorithm = 'proposed_algorithm'
        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'proposed_algorithm'

        # IoTJ: Joint Task Offloading, D2D Pairing, and Resource Allocation in Device-Enhanced MEC: A Potential Game Approach

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False
        self.devices_cache_file_path = './cache/Devices10.cache'
        self.edges_cache_file_path = './cache/Edges10.cache'
        self.task_cache_file_path = './cache/Task10.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks10.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath10.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath10.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath10.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath10.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath10.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath10.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath10.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath10.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath10.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath10.cache'

        self.local_energy_consumption_in_each_slot_file_path = './result/LocalEnergyConsumptionInEachSlotFilePath10.cache'
        self.nearest_energy_consumption_in_each_slot_file_path = './result/NearestEnergyConsumptionInEachSlotFilePath10.cache'
        self.random_energy_consumption_in_each_slot_file_path = './result/RandomEnergyConsumptionInEachSlotFilePath10.cache'
        self.match_energy_consumption_in_each_slot_file_path = './result/MatchEnergyConsumptionInEachSlotFilePath10.cache'
        self.proposed_energy_consumption_in_each_slot_file_path = './result/ProposedEnergyConsumptionInEachSlotFilePath10.cache'

        self.local_energy_harvest_in_each_slot_file_path = './result/LocalEnergyHarvestInEachSlotFilePath10.cache'
        self.nearest_energy_harvest_in_each_slot_file_path = './result/NearestEnergyHarvestInEachSlotFilePath10.cache'
        self.random_energy_harvest_in_each_slot_file_path = './result/RandomEnergyHarvestInEachSlotFilePath10.cache'
        self.match_energy_harvest_in_each_slot_file_path = './result/MatchEnergyHarvestInEachSlotFilePath10.cache'
        self.proposed_energy_harvest_in_each_slot_file_path = './result/ProposedEnergyHarvestInEachSlotFilePath10.cache'

        self.local_energy_cost_in_each_slot_file_path = './result/LocalEnergyCostInEachSlotFilePath10.cache'
        self.nearest_energy_cost_in_each_slot_file_path = './result/NearestEnergyCostInEachSlotFilePath10.cache'
        self.random_energy_cost_in_each_slot_file_path = './result/RandomEnergyCostInEachSlotFilePath10.cache'
        self.match_energy_cost_in_each_slot_file_path = './result/MatchEnergyCostInEachSlotFilePath10.cache'
        self.proposed_energy_cost_in_each_slot_file_path = './result/ProposedEnergyCostInEachSlotFilePath10.cache'

        self.local_latency_cost_in_each_slot_file_path = './result/LocalLatencyCostInEachSlotFilePath10.cache'
        self.nearest_latency_cost_in_each_slot_file_path = './result/NearestLatencyCostInEachSlotFilePath10.cache'
        self.random_latency_cost_in_each_slot_file_path = './result/RandomLatencyCostInEachSlotFilePath10.cache'
        self.match_latency_cost_in_each_slot_file_path = './result/MatchLatencyCostInEachSlotFilePath10.cache'
        self.proposed_latency_cost_in_each_slot_file_path = './result/ProposedLatencyCostInEachSlotFilePath10.cache'

        self.local_total_cost_in_each_slot_file_path = './result/LocalTotalCostInEachSlotFilePath10.cache'
        self.nearest_total_cost_in_each_slot_file_path = './result/NearestTotalCostInEachSlotFilePath10.cache'
        self.random_total_cost_in_each_slot_file_path = './result/RandomTotalCostInEachSlotFilePath10.cache'
        self.match_total_cost_in_each_slot_file_path = './result/MatchTotalCostInEachSlotFilePath10.cache'
        self.proposed_total_cost_in_each_slot_file_path = './result/ProposedTotalCostInEachSlotFilePath10.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath10.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath10.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath10.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath10.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath10.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath10.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath10.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath10.cache'

========================================================================================================================

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

========================================================================================================================

# 30 个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 30

        self.total_number_of_active_devices = 15

        self.total_number_of_passive_devices = 15

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 100

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

        self.devices_cache_file_path = './cache/Devices30.cache'
        self.edges_cache_file_path = './cache/Edges30.cache'
        self.task_cache_file_path = './cache/Task30.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks30.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath30.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath30.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath30.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath30.cache'
        self.dot_ave_queue_length_in_each_slot_file_path = './result/DotAveQueueLengthInEachSlotFilePath30.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath30.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath30.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath30.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath30.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath30.cache'
        self.dot_ave_execute_latency_in_each_slot_file_path = './result/DotAveExecuteLatencyInEachSlotFilePath30.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath30.cache'

        self.local_energy_consumption_in_each_slot_file_path = './result/LocalEnergyConsumptionInEachSlotFilePath30.cache'
        self.nearest_energy_consumption_in_each_slot_file_path = './result/NearestEnergyConsumptionInEachSlotFilePath30.cache'
        self.random_energy_consumption_in_each_slot_file_path = './result/RandomEnergyConsumptionInEachSlotFilePath30.cache'
        self.match_energy_consumption_in_each_slot_file_path = './result/MatchEnergyConsumptionInEachSlotFilePath30.cache'
        self.dot_energy_consumption_in_each_slot_file_path = './result/DotEnergyConsumptionInEachSlotFilePath30.cache'
        self.proposed_energy_consumption_in_each_slot_file_path = './result/ProposedEnergyConsumptionInEachSlotFilePath30.cache'

        self.local_energy_harvest_in_each_slot_file_path = './result/LocalEnergyHarvestInEachSlotFilePath30.cache'
        self.nearest_energy_harvest_in_each_slot_file_path = './result/NearestEnergyHarvestInEachSlotFilePath30.cache'
        self.random_energy_harvest_in_each_slot_file_path = './result/RandomEnergyHarvestInEachSlotFilePath30.cache'
        self.match_energy_harvest_in_each_slot_file_path = './result/MatchEnergyHarvestInEachSlotFilePath30.cache'
        self.dot_energy_harvest_in_each_slot_file_path = './result/DotEnergyHarvestInEachSlotFilePath30.cache'
        self.proposed_energy_harvest_in_each_slot_file_path = './result/ProposedEnergyHarvestInEachSlotFilePath30.cache'

        self.local_energy_cost_in_each_slot_file_path = './result/LocalEnergyCostInEachSlotFilePath30.cache'
        self.nearest_energy_cost_in_each_slot_file_path = './result/NearestEnergyCostInEachSlotFilePath30.cache'
        self.random_energy_cost_in_each_slot_file_path = './result/RandomEnergyCostInEachSlotFilePath30.cache'
        self.match_energy_cost_in_each_slot_file_path = './result/MatchEnergyCostInEachSlotFilePath30.cache'
        self.dot_energy_cost_in_each_slot_file_path = './result/DotEnergyCostInEachSlotFilePath30.cache'
        self.proposed_energy_cost_in_each_slot_file_path = './result/ProposedEnergyCostInEachSlotFilePath30.cache'

        self.local_latency_cost_in_each_slot_file_path = './result/LocalLatencyCostInEachSlotFilePath30.cache'
        self.nearest_latency_cost_in_each_slot_file_path = './result/NearestLatencyCostInEachSlotFilePath30.cache'
        self.random_latency_cost_in_each_slot_file_path = './result/RandomLatencyCostInEachSlotFilePath30.cache'
        self.match_latency_cost_in_each_slot_file_path = './result/MatchLatencyCostInEachSlotFilePath30.cache'
        self.dot_latency_cost_in_each_slot_file_path = './result/DotLatencyCostInEachSlotFilePath30.cache'
        self.proposed_latency_cost_in_each_slot_file_path = './result/ProposedLatencyCostInEachSlotFilePath30.cache'

        self.local_total_cost_in_each_slot_file_path = './result/LocalTotalCostInEachSlotFilePath30.cache'
        self.nearest_total_cost_in_each_slot_file_path = './result/NearestTotalCostInEachSlotFilePath30.cache'
        self.random_total_cost_in_each_slot_file_path = './result/RandomTotalCostInEachSlotFilePath30.cache'
        self.match_total_cost_in_each_slot_file_path = './result/MatchTotalCostInEachSlotFilePath30.cache'
        self.dot_total_cost_in_each_slot_file_path = './result/DotTotalCostInEachSlotFilePath30.cache'
        self.proposed_total_cost_in_each_slot_file_path = './result/ProposedTotalCostInEachSlotFilePath30.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath30.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath30.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath30.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath30.cache'
        self.dot_io_in_each_slot_file_path = './result/DotIOInEachSlotFilePath30.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath30.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath30.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath30.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath30.cache'

========================================================================================================================

# 40 个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 40

        self.total_number_of_active_devices = 20

        self.total_number_of_passive_devices = 20

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 200

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

        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'match_algorithm' 'dot_algorithm' 'proposed_algorithm'

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False

        self.devices_cache_file_path = './cache/Devices40.cache'
        self.edges_cache_file_path = './cache/Edges40.cache'
        self.task_cache_file_path = './cache/Task40.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks40.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath40.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath40.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath40.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath40.cache'
        self.dot_ave_queue_length_in_each_slot_file_path = './result/DotAveQueueLengthInEachSlotFilePath40.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath40.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath40.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath40.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath40.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath40.cache'
        self.dot_ave_execute_latency_in_each_slot_file_path = './result/DotAveExecuteLatencyInEachSlotFilePath40.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath40.cache'

        self.local_energy_consumption_in_each_slot_file_path = './result/LocalEnergyConsumptionInEachSlotFilePath40.cache'
        self.nearest_energy_consumption_in_each_slot_file_path = './result/NearestEnergyConsumptionInEachSlotFilePath40.cache'
        self.random_energy_consumption_in_each_slot_file_path = './result/RandomEnergyConsumptionInEachSlotFilePath40.cache'
        self.match_energy_consumption_in_each_slot_file_path = './result/MatchEnergyConsumptionInEachSlotFilePath40.cache'
        self.dot_energy_consumption_in_each_slot_file_path = './result/DotEnergyConsumptionInEachSlotFilePath40.cache'
        self.proposed_energy_consumption_in_each_slot_file_path = './result/ProposedEnergyConsumptionInEachSlotFilePath40.cache'

        self.local_energy_harvest_in_each_slot_file_path = './result/LocalEnergyHarvestInEachSlotFilePath40.cache'
        self.nearest_energy_harvest_in_each_slot_file_path = './result/NearestEnergyHarvestInEachSlotFilePath40.cache'
        self.random_energy_harvest_in_each_slot_file_path = './result/RandomEnergyHarvestInEachSlotFilePath40.cache'
        self.match_energy_harvest_in_each_slot_file_path = './result/MatchEnergyHarvestInEachSlotFilePath40.cache'
        self.dot_energy_harvest_in_each_slot_file_path = './result/DotEnergyHarvestInEachSlotFilePath40.cache'
        self.proposed_energy_harvest_in_each_slot_file_path = './result/ProposedEnergyHarvestInEachSlotFilePath40.cache'

        self.local_energy_cost_in_each_slot_file_path = './result/LocalEnergyCostInEachSlotFilePath40.cache'
        self.nearest_energy_cost_in_each_slot_file_path = './result/NearestEnergyCostInEachSlotFilePath40.cache'
        self.random_energy_cost_in_each_slot_file_path = './result/RandomEnergyCostInEachSlotFilePath40.cache'
        self.match_energy_cost_in_each_slot_file_path = './result/MatchEnergyCostInEachSlotFilePath40.cache'
        self.dot_energy_cost_in_each_slot_file_path = './result/DotEnergyCostInEachSlotFilePath40.cache'
        self.proposed_energy_cost_in_each_slot_file_path = './result/ProposedEnergyCostInEachSlotFilePath40.cache'

        self.local_latency_cost_in_each_slot_file_path = './result/LocalLatencyCostInEachSlotFilePath40.cache'
        self.nearest_latency_cost_in_each_slot_file_path = './result/NearestLatencyCostInEachSlotFilePath40.cache'
        self.random_latency_cost_in_each_slot_file_path = './result/RandomLatencyCostInEachSlotFilePath40.cache'
        self.match_latency_cost_in_each_slot_file_path = './result/MatchLatencyCostInEachSlotFilePath40.cache'
        self.dot_latency_cost_in_each_slot_file_path = './result/DotLatencyCostInEachSlotFilePath40.cache'
        self.proposed_latency_cost_in_each_slot_file_path = './result/ProposedLatencyCostInEachSlotFilePath40.cache'

        self.local_total_cost_in_each_slot_file_path = './result/LocalTotalCostInEachSlotFilePath40.cache'
        self.nearest_total_cost_in_each_slot_file_path = './result/NearestTotalCostInEachSlotFilePath40.cache'
        self.random_total_cost_in_each_slot_file_path = './result/RandomTotalCostInEachSlotFilePath40.cache'
        self.match_total_cost_in_each_slot_file_path = './result/MatchTotalCostInEachSlotFilePath40.cache'
        self.dot_total_cost_in_each_slot_file_path = './result/DotTotalCostInEachSlotFilePath40.cache'
        self.proposed_total_cost_in_each_slot_file_path = './result/ProposedTotalCostInEachSlotFilePath40.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath40.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath40.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath40.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath40.cache'
        self.dot_io_in_each_slot_file_path = './result/DotIOInEachSlotFilePath40.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath40.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath40.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath40.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath40.cache'

========================================================================================================================

# 50 个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 50

        self.total_number_of_active_devices = 25

        self.total_number_of_passive_devices = 25

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 200

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

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False

        self.devices_cache_file_path = './cache/Devices50.cache'
        self.edges_cache_file_path = './cache/Edges50.cache'
        self.task_cache_file_path = './cache/Task50.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks50.cache'
        self.x_location_in_each_slot_file_path = './cache/XLocation50.cache'
        self.y_location_in_each_slot_file_path = './cache/YLocation50.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath50.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath50.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath50.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath50.cache'
        self.dot_ave_queue_length_in_each_slot_file_path = './result/DotAveQueueLengthInEachSlotFilePath50.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath50.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath50.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath50.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath50.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath50.cache'
        self.dot_ave_execute_latency_in_each_slot_file_path = './result/DotAveExecuteLatencyInEachSlotFilePath50.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath50.cache'

        self.local_energy_consumption_in_each_slot_file_path = './result/LocalEnergyConsumptionInEachSlotFilePath50.cache'
        self.nearest_energy_consumption_in_each_slot_file_path = './result/NearestEnergyConsumptionInEachSlotFilePath50.cache'
        self.random_energy_consumption_in_each_slot_file_path = './result/RandomEnergyConsumptionInEachSlotFilePath50.cache'
        self.match_energy_consumption_in_each_slot_file_path = './result/MatchEnergyConsumptionInEachSlotFilePath50.cache'
        self.dot_energy_consumption_in_each_slot_file_path = './result/DotEnergyConsumptionInEachSlotFilePath50.cache'
        self.proposed_energy_consumption_in_each_slot_file_path = './result/ProposedEnergyConsumptionInEachSlotFilePath50.cache'

        self.local_energy_harvest_in_each_slot_file_path = './result/LocalEnergyHarvestInEachSlotFilePath50.cache'
        self.nearest_energy_harvest_in_each_slot_file_path = './result/NearestEnergyHarvestInEachSlotFilePath50.cache'
        self.random_energy_harvest_in_each_slot_file_path = './result/RandomEnergyHarvestInEachSlotFilePath50.cache'
        self.match_energy_harvest_in_each_slot_file_path = './result/MatchEnergyHarvestInEachSlotFilePath50.cache'
        self.dot_energy_harvest_in_each_slot_file_path = './result/DotEnergyHarvestInEachSlotFilePath50.cache'
        self.proposed_energy_harvest_in_each_slot_file_path = './result/ProposedEnergyHarvestInEachSlotFilePath50.cache'

        self.local_energy_cost_in_each_slot_file_path = './result/LocalEnergyCostInEachSlotFilePath50.cache'
        self.nearest_energy_cost_in_each_slot_file_path = './result/NearestEnergyCostInEachSlotFilePath50.cache'
        self.random_energy_cost_in_each_slot_file_path = './result/RandomEnergyCostInEachSlotFilePath50.cache'
        self.match_energy_cost_in_each_slot_file_path = './result/MatchEnergyCostInEachSlotFilePath50.cache'
        self.dot_energy_cost_in_each_slot_file_path = './result/DotEnergyCostInEachSlotFilePath50.cache'
        self.proposed_energy_cost_in_each_slot_file_path = './result/ProposedEnergyCostInEachSlotFilePath50.cache'

        self.local_latency_cost_in_each_slot_file_path = './result/LocalLatencyCostInEachSlotFilePath50.cache'
        self.nearest_latency_cost_in_each_slot_file_path = './result/NearestLatencyCostInEachSlotFilePath50.cache'
        self.random_latency_cost_in_each_slot_file_path = './result/RandomLatencyCostInEachSlotFilePath50.cache'
        self.match_latency_cost_in_each_slot_file_path = './result/MatchLatencyCostInEachSlotFilePath50.cache'
        self.dot_latency_cost_in_each_slot_file_path = './result/DotLatencyCostInEachSlotFilePath50.cache'
        self.proposed_latency_cost_in_each_slot_file_path = './result/ProposedLatencyCostInEachSlotFilePath50.cache'

        self.local_total_cost_in_each_slot_file_path = './result/LocalTotalCostInEachSlotFilePath50.cache'
        self.nearest_total_cost_in_each_slot_file_path = './result/NearestTotalCostInEachSlotFilePath50.cache'
        self.random_total_cost_in_each_slot_file_path = './result/RandomTotalCostInEachSlotFilePath50.cache'
        self.match_total_cost_in_each_slot_file_path = './result/MatchTotalCostInEachSlotFilePath50.cache'
        self.dot_total_cost_in_each_slot_file_path = './result/DotTotalCostInEachSlotFilePath50.cache'
        self.proposed_total_cost_in_each_slot_file_path = './result/ProposedTotalCostInEachSlotFilePath50.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath50.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath50.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath50.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath50.cache'
        self.dot_io_in_each_slot_file_path = './result/DotIOInEachSlotFilePath50.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath50.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath50.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath50.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath50.cache'

========================================================================================================================

# lya的参数

========================================================================================================================


# 10个用户

class Config:
    '''配置类'''

    def __init__(self) -> None:
        super().__init__()

        # 边的数量
        self.total_number_of_edges = 4

        # 设备总数量
        self.total_number_of_devices = 10

        self.total_number_of_active_devices = 6

        self.total_number_of_passive_devices = 4

        # self.V = 0
        self.V = 500

        # 迭代次数
        self.times = 1000

        self.iterations_number_of_game_theory = 200

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

        self.coverage_radius = 120

        # sca 参数设置
        self.pop_size = 60
        self.a = 2 # 感知概率
        self.max_iter = 500  # max iter

        # self.algorithm = 'local_algorithm'
        # self.algorithm = 'nearest_algorithm'
        # self.algorithm = 'random_algorithm'
        # self.algorithm = 'match_algorithm'
        # self.algorithm = 'proposed_algorithm'
        self.algorithm = 'proposed_algorithm_v2'
        # 'local_algorithm'  'nearest_algorithm' 'random_algorithm' 'proposed_algorithm'

        # IoTJ: Joint Task Offloading, D2D Pairing, and Resource Allocation in Device-Enhanced MEC: A Potential Game Approach

        # 缓存设置
        self.cache = True
        # self.cache = False
        # True False
        self.devices_cache_file_path = './cache/Devices10.cache'
        self.edges_cache_file_path = './cache/Edges10.cache'
        self.task_cache_file_path = './cache/Task10.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks10.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath10.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath10.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath10.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath10.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath10.cache'
        self.lya5_proposed_ave_queue_length_in_each_slot_file_path = './result/Lya5ProposedAveQueueLengthInEachSlotFilePath10.cache'
        self.lya100_proposed_ave_queue_length_in_each_slot_file_path = './result/Lya100ProposedAveQueueLengthInEachSlotFilePath10.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath10.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath10.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath10.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath10.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath10.cache'
        self.lya5_proposed_ave_execute_latency_in_each_slot_file_path = './result/Lya5ProposedAveExecuteLatencyInEachSlotFilePath10.cache'
        self.lya100_proposed_ave_execute_latency_in_each_slot_file_path = './result/Lya100ProposedAveExecuteLatencyInEachSlotFilePath10.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath10.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath10.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath10.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath10.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath10.cache'
        self.lya5_proposed_total_energy_cost_in_each_slot_file_path = './result/Lya5ProposedTotalEnergyCostInEachSlotFilePath10.cache'
        self.lya100_proposed_total_energy_cost_in_each_slot_file_path = './result/Lya100ProposedTotalEnergyCostInEachSlotFilePath10.cache'

        self.local_total_energy_cost_in_each_slot_file_path = './result/LocalTotalEnergyCostInEachSlotFilePath10.cache'
        self.nearest_total_energy_cost_in_each_slot_file_path = './result/NearestTotalEnergyCostInEachSlotFilePath10.cache'
        self.random_total_energy_cost_in_each_slot_file_path = './result/RandomTotalEnergyCostInEachSlotFilePath10.cache'
        self.match_total_energy_cost_in_each_slot_file_path = './result/MatchTotalEnergyCostInEachSlotFilePath10.cache'
        self.proposed_total_energy_cost_in_each_slot_file_path = './result/ProposedTotalEnergyCostInEachSlotFilePath10.cache'
        self.lya5_proposed_total_energy_cost_in_each_slot_file_path = './result/Lya5ProposedTotalEnergyCostInEachSlotFilePath10.cache'
        self.lya100_proposed_total_energy_cost_in_each_slot_file_path = './result/Lya100ProposedTotalEnergyCostInEachSlotFilePath10.cache'

        self.local_total_energy_harvest_in_each_slot_file_path = './result/LocalTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.nearest_total_energy_harvest_in_each_slot_file_path = './result/NearestTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.random_total_energy_harvest_in_each_slot_file_path = './result/RandomTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.match_total_energy_harvest_in_each_slot_file_path = './result/MatchTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.proposed_total_energy_harvest_in_each_slot_file_path = './result/ProposedTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.lya5_proposed_total_energy_harvest_in_each_slot_file_path = './result/Lya5ProposedTotalEnergyHarvestInEachSlotFilePath10.cache'
        self.lya100_proposed_total_energy_harvest_in_each_slot_file_path = './result/Lya100ProposedTotalEnergyHarvestInEachSlotFilePath10.cache'

        self.local_energy_utility_in_each_slot_file_path = './result/LocalEnergyUtilityInEachSlotFilePath10.cache'
        self.nearest_energy_utility_in_each_slot_file_path = './result/NearestEnergyUtilityInEachSlotFilePath10.cache'
        self.random_energy_utility_in_each_slot_file_path = './result/RandomEnergyUtilityInEachSlotFilePath10.cache'
        self.match_energy_utility_in_each_slot_file_path = './result/MatchEnergyUtilityInEachSlotFilePath10.cache'
        self.proposed_energy_utility_in_each_slot_file_path = './result/ProposedEnergyUtilityInEachSlotFilePath10.cache'
        self.lya5_proposed_energy_utility_in_each_slot_file_path = './result/Lya5ProposedEnergyUtilityInEachSlotFilePath10.cache'
        self.lya100_proposed_energy_utility_in_each_slot_file_path = './result/Lya100ProposedEnergyUtilityInEachSlotFilePath10.cache'

        self.local_latency_utility_in_each_slot_file_path = './result/LocalLatencyUtilityInEachSlotFilePath10.cache'
        self.nearest_latency_utility_in_each_slot_file_path = './result/NearestLatencyUtilityInEachSlotFilePath10.cache'
        self.random_latency_utility_in_each_slot_file_path = './result/RandomLatencyUtilityInEachSlotFilePath10.cache'
        self.match_latency_utility_in_each_slot_file_path = './result/MatchLatencyUtilityInEachSlotFilePath10.cache'
        self.proposed_latency_utility_in_each_slot_file_path = './result/ProposedLatencyUtilityInEachSlotFilePath10.cache'
        self.lya5_proposed_latency_utility_in_each_slot_file_path = './result/Lya5ProposedLatencyUtilityInEachSlotFilePath10.cache'
        self.lya100_proposed_latency_utility_in_each_slot_file_path = './result/Lya100ProposedLatencyUtilityInEachSlotFilePath10.cache'

        self.local_total_utility_in_each_slot_file_path = './result/LocalTotalUtilityInEachSlotFilePath10.cache'
        self.nearest_total_utility_in_each_slot_file_path = './result/NearestTotalUtilityInEachSlotFilePath10.cache'
        self.random_total_utility_in_each_slot_file_path = './result/RandomTotalUtilityInEachSlotFilePath10.cache'
        self.match_total_utility_in_each_slot_file_path = './result/MatchTotalUtilityInEachSlotFilePath10.cache'
        self.proposed_total_utility_in_each_slot_file_path = './result/ProposedTotalUtilityInEachSlotFilePath10.cache'
        self.lya5_proposed_total_utility_in_each_slot_file_path = './result/Lya5ProposedTotalUtilityInEachSlotFilePath10.cache'
        self.lya100_proposed_total_utility_in_each_slot_file_path = './result/Lya100ProposedTotalUtilityInEachSlotFilePath10.cache'

        self.local_io_in_each_slot_file_path = './result/LocalIOInEachSlotFilePath10.cache'
        self.nearest_io_in_each_slot_file_path = './result/NearestIOInEachSlotFilePath10.cache'
        self.random_io_in_each_slot_file_path = './result/RandomIOInEachSlotFilePath10.cache'
        self.match_io_in_each_slot_file_path = './result/MatchIOInEachSlotFilePath10.cache'
        self.proposed_io_in_each_slot_file_path = './result/ProposedIOInEachSlotFilePath10.cache'
        self.lya5_proposed_io_in_each_slot_file_path = './result/Lya5ProposedIOInEachSlotFilePath10.cache'
        self.lya100_proposed_io_in_each_slot_file_path = './result/Lya100ProposedIOInEachSlotFilePath10.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath10.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath10.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath10.cache'
