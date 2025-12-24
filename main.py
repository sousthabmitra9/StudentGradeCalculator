#Student Grade Calculator
import csv
from typing import List, Dict
#MODULE 1: Input 
def get_student_data() -> Dict:
    print("\n- Add New Student -")
    name = input("Enter Name: ").strip()
    roll = input("Enter Roll No: ").strip()
    print("Enter marks (0-100):")
    subjects = ['Math', 'Physics', 'Chemistry', 'English', 'Computer Science']
    marks = []
    for sub in subjects:
        while True:
            m = input(f"  {sub}: ")
            if m.isdigit() and 0 <= int(m) <= 100:
                marks.append(int(m))
                break
            print("Invalid! Enter 0-100.")
    return {
        'name': name,
        'roll': roll,
        'marks': marks,
        'subjects': subjects
    }
#MODULE 2: Calculation 
def calculate_grade(avg: float) -> str:
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    elif avg >= 50: return 'E'
    else: return 'F'
def analyze_student(student: Dict) -> Dict:
    total = sum(student['marks'])
    avg = total / 5
    grade = calculate_grade(avg)
    
    student['total'] = total
    student['average'] = round(avg, 2)
    student['grade'] = grade
    return student
#MODULE 3: Storage
def save_to_csv(students: List[Dict]):
    if not students:
        print("No data to save.")
        return
    keys = ['name', 'roll', 'Math', 'Physics', 'Chemistry', 'English', 'Computer Science', 
            'total', 'average', 'grade']
    with open('students.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for s in students:
            row = {'name': s['name'], 'roll': s['roll'], 'total': s['total'],
                   'average': s['average'], 'grade': s['grade']}
            for i, sub in enumerate(s['subjects']):
                row[sub] = s['marks'][i]
            writer.writerow(row)
    print("Data saved to students.csv")
#MODULE 4: Display 
def display_students(students: List[Dict]):
    if not students:
        print("No students recorded.")
        return
    print("\n" + "="*50)
    print(f"{'Name':<15} {'Roll':<8} {'Total':<6} {'Avg':<6} {'Grade':<6}")
    print("-"*50)
    for s in students:
        print(f"{s['name']:<15} {s['roll']:<8} {s['total']:<6} {s['average']:<6} {s['grade']:<6}")
    print("="*50)
def find_topper(students: List[Dict]):
    if not students:
        print("No data.")
        return
    top = max(students, key=lambda x: x['average'])
    print(f"\nTOPPER: {top['name']} (Roll: {top['roll']}) - Avg: {top['average']}, Grade: {top['grade']}")
#MODULE 5: Main Menu 
def main():
    students = []
    print("STUDENT GRADE CALCULATOR")
    while True:
        print("\n1. Add Student")
        print("2. View All")
        print("3. Find Topper")
        print("4. Save & Exit")
        choice = input("\nChoose (1-4): ").strip()
        if choice == '1':
            data = get_student_data()
            student = analyze_student(data)
            students.append(student)
            print(f"Added {student['name']} - Grade: {student['grade']}")
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            find_topper(students)
        elif choice == '4':
            save_to_csv(students)
            print("Thank you!")
            break
        else:
            print("Invalid choice!")
# Run program
if __name__ == "__main__":
    main()