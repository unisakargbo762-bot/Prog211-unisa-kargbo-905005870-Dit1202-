# ============================================================
# EduTrack SL – Terminal-Based Student Academic Record Portal
# PROG103 – Principles of Structured Programming
# Author: [UNISA]
# Institution: Limkokwing University of Creative Technology
# ============================================================


# ============================================================
# 1. CONSTANTS SECTION
# ============================================================

PASS_MARK = 50   # Minimum score required to pass


# ============================================================
# 2. LOGIC FUNCTIONS SECTION
#    (Handles calculations and grading logic)
# ============================================================

def calculate_total(test_score, exam_score):
    """
    Calculate the total score from test and exam.
    Returns:
        float: total score
    """
    return test_score + exam_score


def assign_grade(total):
    """
    Assign a grade and remark based on the total score.
    Returns:
        tuple: (grade, remark)
    """
    if total >= 80:
        return "A", "Excellent"
    elif total >= 70:
        return "B", "Very Good"
    elif total >= 60:
        return "C", "Good"
    elif total >= 50:
        return "D", "Pass"
    else:
        return "F", "Fail"


# ============================================================
# 3. INPUT VALIDATION SECTION
#    (Ensures numeric input and valid score ranges)
# ============================================================

def get_float_input(prompt, min_val=0, max_val=50):
    """
    Get a valid numeric input from the user within a given range.
    Keeps asking until valid input is provided.
    """
    while True:
        value_str = input(prompt).strip()
        try:
            value = float(value_str)
            if value < min_val or value > max_val:
                print(f"Value must be between {min_val} and {max_val}. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


# ============================================================
# 4. RECORD ENTRY SECTION
#    (Collects student data and processes results)
# ============================================================

def enter_student_record():
    """
    Collect one student record from user input.
    Processes the record and returns a dictionary.
    """
    print("\n--- Enter Student Record ---")

    name = input("Student Name: ").strip()
    sid = input("Student ID: ").strip()
    course = input("Course: ").strip()

    # Validated numeric inputs
    test_score = get_float_input("Test Score (0–50): ")
    exam_score = get_float_input("Exam Score (0–50): ")

    # Processing
    total = calculate_total(test_score, exam_score)
    grade, remark = assign_grade(total)

    # Store record in dictionary
    record = {
        "id": sid,
        "name": name,
        "course": course,
        "test": test_score,
        "exam": exam_score,
        "total": total,
        "grade": grade,
        "remark": remark,
    }

    # Display result to user
    print("\n--- Result ---")
    print(f"Student: {name} ({sid})")
    print(f"Course:  {course}")
    print(f"Test:    {test_score}")
    print(f"Exam:    {exam_score}")
    print(f"Total:   {total}")
    print(f"Grade:   {grade}")
    print(f"Remark:  {remark}")

    return record


# ============================================================
# 5. DISPLAY SECTION
#    (Shows all stored student records)
# ============================================================

def display_all_records(records):
    """
    Display all student records in a formatted table.
    """
    if not records:
        print("\nNo records available yet.")
        return

    print("\n=== All Student Records ===")
    print("ID       | Name                | Course           | Total | Grade | Remark")
    print("-" * 75)

    for r in records:
        print(f"{r['id']:<8} | {r['name']:<18} | {r['course']:<15} | "
              f"{r['total']:<5.1f} | {r['grade']:^5} | {r['remark']}")

    print("-" * 75)


# ============================================================
# 6. MAIN MENU SECTION
#    (Handles user navigation and program flow)
# ============================================================

def main_menu():
    """
    Main menu loop for the terminal application.
    Allows user to enter records, view records, or exit.
    """
    records = []  # List to store all student records

    while True:
        print("\n==============================")
        print(" EduTrack SL - Terminal Portal")
        print("==============================")
        print("1. Enter New Student Record")
        print("2. View All Records")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            record = enter_student_record()
            records.append(record)

        elif choice == "2":
            display_all_records(records)

        elif choice == "3":
            print("Exiting EduTrack SL. Goodbye.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


# ============================================================
# 7. PROGRAM EXECUTION SECTION
# ============================================================

if __name__ == "__main__":
    main_menu()
