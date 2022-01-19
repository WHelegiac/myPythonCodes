from collections import Counter


def frequency(data):
    """求一组数据的频率"""
    counter = Counter(data)
    ret = []
    for point in counter.most_common():
        ret.append((point[0], point[1] / len(data)))
    return ret

def mode(data):
    """求一组数的众数"""
    counter = Counter(data)

