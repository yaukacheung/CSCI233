import sys

def main():
    student_grades = []
    
    while True:
        print("\n--- Grade Tracker Menu ---")
        print("1. Add a grade")
        print("2. Remove a grade")
        print("3. Show all grades")
        print("4. Show average grade")
        print("5. Show highest and lowest grade (Challenge)")
        print("6. Exit")
        
        try:
            choice = input("Enter choice (1-6): ").strip()
        except EOFError:
            break
            
        if choice == '1':
            try:
                grade = float(input("Enter grade to add: ").strip())
                student_grades.append(grade)
                print(f"Grade {grade} added successfully.")
            except ValueError:
                print("Error: Invalid grade format.")
                
        elif choice == '2':
            try:
                grade = float(input("Enter grade to remove: ").strip())
                if grade in student_grades:
                    student_grades.remove(grade)
                    print(f"Grade {grade} removed successfully.")
                else:
                    print("Error: Grade not found in the list.")
            except ValueError:
                print("Error: Invalid grade format.")
                
        elif choice == '3':
            if student_grades:
                print(f"Current Grades: {student_grades}")
            else:
                print("The grade list is currently empty.")
                
        elif choice == '4':
            if student_grades:
                average = sum(student_grades) / len(student_grades)
                print(f"Average Grade: {average:.2f}")
            else:
                print("Cannot calculate average: No grades available.")
                
        elif choice == '5':
            if student_grades:
                highest = max(student_grades)
                lowest = min(student_grades)
                print(f"Highest Grade: {highest}")
                print(f"Lowest Grade: {lowest}")
            else:
                print("Cannot determine highest/lowest: No grades available.")
                
        elif choice == '6':
            print("Exiting Grade Tracker...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()
