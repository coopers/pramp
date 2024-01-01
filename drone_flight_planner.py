def calc_drone_min_energy(route):
    return max(r[-1] for r in route) - route[0][-1]

assert calc_drone_min_energy(
    [
        [0,   2, 10],
        [3,   5,  0],
        [9,  20,  6],
        [10, 12, 15],
        [10, 10,  8]
    ]
) == 5