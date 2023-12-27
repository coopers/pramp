def calc_drone_min_energy(route):
    start = route[0][-1]
    maximum = max(route[i][-1] for i in range(len(route)))
    return max(0, maximum - start)


def calc_drone_min_energy(route):
  energy = 0
  needed = 0
  for i in range(1, len(route)):
    energy += route[i-1][-1] - route[i][-1]
    needed = min(needed, energy)
        
  return -needed