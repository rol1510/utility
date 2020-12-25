from collections import deque

def rotate_list(data, amount):
    d = deque(data)
    d.rotate(amount)
    return list(d)

def pad_1d_list(data, element):
    data.insert(0, element)
    data.append(element)
    return data

def pad_2d_list(data, element):
    # pad sides
    for i in range(len(data)):
        pad_1d_list(data[i], element)

    # pad top and bottom
    width = len(data[0])
    top_bottom_padding = [element] * width
    pad_1d_list(data, top_bottom_padding)
    return data
