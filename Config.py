
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
        self.edge_cpu_frequency = 5 * (10 ** 9)

        self.SWITCHED_CAPACITANCE = 10 ** -28

        self.ENERGY_CONVERSION_EFFICIENCY = 1

        # [0.2, 0.4] MB   (1 MB = 1024 KB = 1,048,576 Bytes = 8,388,608 bits)
        self.task_size = [1677721.6, 3355443.2]

        # 1000 cycles/bit
        self.task_cpu_frequency_demand = 1000

        self.max_energy_queue_length = 5000

        # -100 dBm = 10 ** -13 W
        self.GAUSSIAN_WHITE_NOISE_POWER = 10 ** -13

        # 10MHZ
        self.OFFLOAD_BANDWIDTH = 10000000

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
        # self.cache = True
        self.cache = False
        # True False
        self.devices_cache_file_path = './cache/Devices10.cache'
        self.edges_cache_file_path = './cache/Edges10.cache'
        self.task_cache_file_path = './cache/Task10.cache'
        self.number_of_tasks_cache_file_path = './cache/NumberOfTasks10.cache'
        self.x_location_in_each_slot_file_path = './cache/XLocation10.cache'
        self.y_location_in_each_slot_file_path = './cache/YLocation10.cache'

        self.local_ave_queue_length_in_each_slot_file_path = './result/LocalAveQueueLengthInEachSlotFilePath10.cache'
        self.nearest_ave_queue_length_in_each_slot_file_path = './result/NearestAveQueueLengthInEachSlotFilePath10.cache'
        self.random_ave_queue_length_in_each_slot_file_path = './result/RandomAveQueueLengthInEachSlotFilePath10.cache'
        self.match_ave_queue_length_in_each_slot_file_path = './result/MatchAveQueueLengthInEachSlotFilePath10.cache'
        self.dot_ave_queue_length_in_each_slot_file_path = './result/DotAveQueueLengthInEachSlotFilePath10.cache'
        self.proposed_ave_queue_length_in_each_slot_file_path = './result/ProposedAveQueueLengthInEachSlotFilePath10.cache'

        self.local_ave_execute_latency_in_each_slot_file_path = './result/LocalAveExecuteLatencyInEachSlotFilePath10.cache'
        self.nearest_ave_execute_latency_in_each_slot_file_path = './result/NearestAveExecuteLatencyInEachSlotFilePath10.cache'
        self.random_ave_execute_latency_in_each_slot_file_path = './result/RandomAveExecuteLatencyInEachSlotFilePath10.cache'
        self.match_ave_execute_latency_in_each_slot_file_path = './result/MatchAveExecuteLatencyInEachSlotFilePath10.cache'
        self.dot_ave_execute_latency_in_each_slot_file_path = './result/DotAveExecuteLatencyInEachSlotFilePath10.cache'
        self.proposed_ave_execute_latency_in_each_slot_file_path = './result/ProposedAveExecuteLatencyInEachSlotFilePath10.cache'

        self.local_energy_consumption_in_each_slot_file_path = './result/LocalEnergyConsumptionInEachSlotFilePath10.cache'
        self.nearest_energy_consumption_in_each_slot_file_path = './result/NearestEnergyConsumptionInEachSlotFilePath10.cache'
        self.random_energy_consumption_in_each_slot_file_path = './result/RandomEnergyConsumptionInEachSlotFilePath10.cache'
        self.match_energy_consumption_in_each_slot_file_path = './result/MatchEnergyConsumptionInEachSlotFilePath10.cache'
        self.dot_energy_consumption_in_each_slot_file_path = './result/DotEnergyConsumptionInEachSlotFilePath10.cache'
        self.proposed_energy_consumption_in_each_slot_file_path = './result/ProposedEnergyConsumptionInEachSlotFilePath10.cache'

        self.local_energy_harvest_in_each_slot_file_path = './result/LocalEnergyHarvestInEachSlotFilePath10.cache'
        self.nearest_energy_harvest_in_each_slot_file_path = './result/NearestEnergyHarvestInEachSlotFilePath10.cache'
        self.random_energy_harvest_in_each_slot_file_path = './result/RandomEnergyHarvestInEachSlotFilePath10.cache'
        self.match_energy_harvest_in_each_slot_file_path = './result/MatchEnergyHarvestInEachSlotFilePath10.cache'
        self.dot_energy_harvest_in_each_slot_file_path = './result/DotEnergyHarvestInEachSlotFilePath10.cache'
        self.proposed_energy_harvest_in_each_slot_file_path = './result/ProposedEnergyHarvestInEachSlotFilePath10.cache'

        self.local_energy_cost_in_each_slot_file_path = './result/LocalEnergyCostInEachSlotFilePath10.cache'
        self.nearest_energy_cost_in_each_slot_file_path = './result/NearestEnergyCostInEachSlotFilePath10.cache'
        self.random_energy_cost_in_each_slot_file_path = './result/RandomEnergyCostInEachSlotFilePath10.cache'
        self.match_energy_cost_in_each_slot_file_path = './result/MatchEnergyCostInEachSlotFilePath10.cache'
        self.dot_energy_cost_in_each_slot_file_path = './result/DotEnergyCostInEachSlotFilePath10.cache'
        self.proposed_energy_cost_in_each_slot_file_path = './result/ProposedEnergyCostInEachSlotFilePath10.cache'

        self.local_latency_cost_in_each_slot_file_path = './result/LocalLatencyCostInEachSlotFilePath10.cache'
        self.nearest_latency_cost_in_each_slot_file_path = './result/NearestLatencyCostInEachSlotFilePath10.cache'
        self.random_latency_cost_in_each_slot_file_path = './result/RandomLatencyCostInEachSlotFilePath10.cache'
        self.match_latency_cost_in_each_slot_file_path = './result/MatchLatencyCostInEachSlotFilePath10.cache'
        self.dot_latency_cost_in_each_slot_file_path = './result/DotLatencyCostInEachSlotFilePath10.cache'
        self.proposed_latency_cost_in_each_slot_file_path = './result/ProposedLatencyCostInEachSlotFilePath10.cache'

        self.local_total_cost_in_each_slot_file_path = './result/LocalTotalCostInEachSlotFilePath10.cache'
        self.nearest_total_cost_in_each_slot_file_path = './result/NearestTotalCostInEachSlotFilePath10.cache'
        self.random_total_cost_in_each_slot_file_path = './result/RandomTotalCostInEachSlotFilePath10.cache'
        self.match_total_cost_in_each_slot_file_path = './result/MatchTotalCostInEachSlotFilePath10.cache'
        self.dot_total_cost_in_each_slot_file_path = './result/DotTotalCostInEachSlotFilePath10.cache'
        self.proposed_total_cost_in_each_slot_file_path = './result/ProposedTotalCostInEachSlotFilePath10.cache'

        self.local_ratio_in_each_slot_file_path = './result/LocalRatioInEachSlotFilePath10.cache'
        self.edge_ratio_in_each_slot_file_path = './result/EdgeRatioInEachSlotFilePath10.cache'
        self.d2d_ratio_in_each_slot_file_path = './result/D2DRatioInEachSlotFilePath10.cache'