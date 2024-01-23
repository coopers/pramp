def calc_drone_min_energy(route):
    INITIAL = 0
    ALTITUDE = 2
    return max(point[ALTITUDE] for point in route) - route[INITIAL][ALTITUDE]

assert calc_drone_min_energy(
    [
        [0,   2, 10],
        [3,   5,  0],
        [9,  20,  6],
        [10, 12, 15],
        [10, 10,  8]
    ]
) == 5