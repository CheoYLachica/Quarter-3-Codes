import numpy as np

names = ["Sebastian", "Justin", "Tim"]
steps = np.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])

totals = np.sum(steps, axis=1)

for i in range(len(names)):
    print(f"{names[i]} total: {totals[i]}")

winner_idx = np.argmax(totals)
diff = np.max(totals) - np.min(totals)

print(f"Highest: {names[winner_idx]} ({totals[winner_idx]})")
print(f"Difference: {diff}")