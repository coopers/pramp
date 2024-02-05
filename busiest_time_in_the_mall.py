# Time:  O(n)
# Space: O(1)

def find_busiest_period(data):
    N = len(data)
    busy_time = None
    max_count = None
    count = 0
    for i in range(N):
        time, amount, is_positive = data[i]
        count += amount * (1 if is_positive else -1)
        if i < N - 1 and data[i + 1][0] == time:
            continue

        if max_count is None or count > max_count:
            max_count = count
            busy_time = time

    return busy_time


data = [
    [1487799425, 14, 1], 
    [1487799425, 4,  0],
    [1487799425, 2,  0],
    [1487800378, 10, 1],
    [1487801478, 18, 0],
    [1487801478, 18, 1],
    [1487901013, 1,  0],
    [1487901211, 7,  1],
    [1487901211, 7,  0]
]
output = 1487800378
assert find_busiest_period(data) == output