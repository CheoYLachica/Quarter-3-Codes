import numpy as np

steps = np.array([
    ["Name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    ["Sebastian", 4500, 5200, 4800, 5000, 5300],
    ["Justin", 4000, 4100, 3900, 4200, 4600],
    ["Tim", 6000, 5800, 5900, 6100, 6200]
])

for row in steps:
    print("".join(f"{cell:<10}" for cell in row))