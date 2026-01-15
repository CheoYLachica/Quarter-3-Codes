import numpy as np

steps = np.array([
    ["Name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    ["Sebastian", 4500, 5200, 4800, 5000, 5300],
    ["Justin", 4000, 4100, 3900, 4200, 4600],
    ["Tim", 6000, 5800, 5900, 6100, 6200]
])

print("Output")

for i in [1, 2, 3]:
    row = steps[i]
    
    name = row[0]
    text_numbers = row[1:]
    real_numbers = text_numbers.astype(int)
    
    total = np.sum(real_numbers)
    avg = np.mean(real_numbers)
    low = np.min(real_numbers)
    high = np.max(real_numbers)
    
    print(f"{name} - Total Steps: {total} | Average: {avg:.1f} | Min: {low} | Max: {high}")