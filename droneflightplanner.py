def calc_drone_min_energy(route):
  energy = 0
  needed = 0
  for i in range(1, len(route)):
    energy += route[i-1][-1] - route[i][-1]
    if energy < 0:
      needed = max(needed, -energy)
        
  return needed