import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps = np.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])

day_totals = np.sum(steps, axis=0)

for i in range(len(days)):
    print(f"{days[i]} total: {day_totals[i]}")

best_day_idx = np.argmax(day_totals)

print(f"Most active day: {days[best_day_idx]} ({day_totals[best_day_idx]})")