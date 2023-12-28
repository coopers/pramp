def calc_drone_min_energy(route):
    return max(r[-1] for r in route) - route[0][-1]


def calc_drone_min_energy(route):
    energy = 0
    needed = 0
    for i in range(1, len(route)):
        energy += route[i-1][-1] - route[i][-1]
        needed = min(needed, energy)
    
    return -needed