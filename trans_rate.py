import math
from Config import Config

config = Config()


def get_upload_gain(device, edge):
    # x1 = device.x
    # y1 = device.y
    # x2 = edge.x
    # y2 = edge.y
    # distance = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    # distance2 = math.pow(distance, 2)
    power = device.offload_trans_power
    # gain = config.DEVICE_CHANNEL_GAIN / distance2
    gain = config.EDGE_CHANNEL_GAIN
    signal = power * gain
    return signal


def get_d2d_gain(device1, device2):
    x1 = device1.x
    y1 = device1.y
    x2 = device2.x
    y2 = device2.y
    distance = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    distance2 = math.pow(distance, 2)
    power = device1.d2d_trans_power
    if distance2 > 1:
        gain = config.D2D_CHANNEL_GAIN / distance2
    else:
        gain = config.D2D_CHANNEL_GAIN
    signal = power * gain
    return signal


def get_upload_rate(device, edge, interference):
    # x1 = device.x
    # y1 = device.y
    # x2 = edge.x
    # y2 = edge.y
    # distance = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    # distance2 = math.pow(distance, 2)
    power = device.offload_trans_power
    noise2 = config.GAUSSIAN_WHITE_NOISE_POWER + interference
    # gain = config.DEVICE_CHANNEL_GAIN / distance2
    gain = config.EDGE_CHANNEL_GAIN
    signal = power * gain
    snr = signal / noise2
    bandwidth = config.OFFLOAD_BANDWIDTH
    rate = bandwidth * (math.log2(1 + snr))
    return rate


def get_d2d_rate(device1, device2, interference):
    x1 = device1.x
    y1 = device1.y
    x2 = device2.x
    y2 = device2.y
    distance = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    distance2 = math.pow(distance, 2)
    power = device1.d2d_trans_power
    noise2 = config.GAUSSIAN_WHITE_NOISE_POWER + interference
    if distance2 < 1:
        gain = config.D2D_CHANNEL_GAIN / 1
    else:
        gain = config.D2D_CHANNEL_GAIN / distance2
    signal = power * gain
    snr = signal / noise2
    bandwidth = config.D2D_BANDWIDTH
    rate = bandwidth * (math.log2(1 + snr))
    return rate

