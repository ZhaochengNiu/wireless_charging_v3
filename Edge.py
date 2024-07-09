class Edge:

    def __init__(self, nid, frequency, ncp_type, x, y, coverage_radius, total_number_of_devices) -> None:
        super().__init__()
        self.id = nid       # 序号
        self.frequency = frequency          # 当前计算能力
        # 传输功率 100W
        self.trans_power = 50
        self.ncp_type = ncp_type   # 节点类型
        self.queue = []
        self.x = x  # x 坐标
        self.y = y  # y 坐标
        self.coverage_radius = coverage_radius
        self.coverage_mobile_device = [0 for i in range(0, total_number_of_devices)]
        self.distance_device = [0 for i in range(0, total_number_of_devices)]


if __name__ == '__main__':
    # queue = []
    # for i in range(0, 10):
    #     queue.insert(0, i)
    # print(queue)
    # print(len(queue))
    # for i in range(0, 3):
    #     queue.pop()
    # print(queue)
    # print(len(queue))
    # for i in range(0, 50):
    #     destination = random.randint(-1, config.total_number_of_edges)
    #     print(destination)
    # test = []
    # for i in range(0, 10):
    #     test.append(i)
    # print(test)
    # coverage_mobile_device = [0 for i in range(0, 10)]
    # print(coverage_mobile_device)
    # for i in range(0, 10):
    #     print(i)
    task_queue = []
    print(len(queue))