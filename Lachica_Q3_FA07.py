students = []

for i in range(3):
    print(f"--- Student {i+1} ---")
    
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    
    student_data = {
        "name": name,
        "age": age,
        "grade": grade
    }
    
    
    students.append(student_data)
    print() 

print("Class Directory:")
for s in students:
    print(f"{s['name']} | Age: {s['age']} | Grade: {s['grade']}")