import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Constants
# -----------------------------
PASS_MARK = 50

# -----------------------------
# Logic functions
# -----------------------------
def calculate_total(test_score, exam_score):
    return test_score + exam_score

def assign_grade(total):
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

def validate_scores(test_str, exam_str):
    try:
        test = float(test_str)
        exam = float(exam_str)
    except ValueError:
        raise ValueError("Test and Exam scores must be numbers.")

    if not (0 <= test <= 50):
        raise ValueError("Test score must be between 0 and 50.")
    if not (0 <= exam <= 50):
        raise ValueError("Exam score must be between 0 and 50.")

    return test, exam

# -----------------------------
# GUI callback functions
# -----------------------------
def on_calculate():
    name = entry_name.get().strip()
    sid = entry_id.get().strip()
    course = entry_course.get().strip()
    test_str = entry_test.get().strip()
    exam_str = entry_exam.get().strip()

    if not name or not sid or not course or not test_str or not exam_str:
        messagebox.showwarning("Missing Data", "Please fill in all fields.")
        return

    try:
        test, exam = validate_scores(test_str, exam_str)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return

    total = calculate_total(test, exam)
    grade, remark = assign_grade(total)

    label_total_value.config(text=f"{total:.2f}")
    label_grade_value.config(text=grade)
    label_remark_value.config(text=remark)

    # Store record in listbox
    record = f"{sid} | {name} | {course} | {total:.2f} | {grade} | {remark}"
    listbox_records.insert(tk.END, record)

def on_clear():
    entry_name.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_test.delete(0, tk.END)
    entry_exam.delete(0, tk.END)

    label_total_value.config(text="--")
    label_grade_value.config(text="--")
    label_remark_value.config(text="--")

def on_exit():
    root.destroy()

# -----------------------------
# Main GUI
# -----------------------------
root = tk.Tk()
root.title("EduTrack SL - Student Academic Record Portal")
root.geometry("800x500")

# Title
title_label = tk.Label(root, text="EduTrack SL – Student Academic Record Portal",
                       font=("Tahoma", 14, "bold"))
title_label.pack(pady=10)

# Input frame
frame_input = tk.Frame(root)
frame_input.pack(pady=5)

# Row 1
tk.Label(frame_input, text="Student Name:", font=("Tahoma", 10)).grid(row=0, column=0, sticky="e", padx=5, pady=3)
entry_name = tk.Entry(frame_input, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=3)

tk.Label(frame_input, text="Student ID:", font=("Tahoma", 10)).grid(row=0, column=2, sticky="e", padx=5, pady=3)
entry_id = tk.Entry(frame_input, width=20)
entry_id.grid(row=0, column=3, padx=5, pady=3)

# Row 2
tk.Label(frame_input, text="Course:", font=("Tahoma", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=3)
entry_course = tk.Entry(frame_input, width=30)
entry_course.grid(row=1, column=1, padx=5, pady=3)

tk.Label(frame_input, text="Test Score (0–50):", font=("Tahoma", 10)).grid(row=1, column=2, sticky="e", padx=5, pady=3)
entry_test = tk.Entry(frame_input, width=20)
entry_test.grid(row=1, column=3, padx=5, pady=3)

# Row 3
tk.Label(frame_input, text="Exam Score (0–50):", font=("Tahoma", 10)).grid(row=2, column=2, sticky="e", padx=5, pady=3)
entry_exam = tk.Entry(frame_input, width=20)
entry_exam.grid(row=2, column=3, padx=5, pady=3)

# Buttons frame
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_calculate = tk.Button(frame_buttons, text="Calculate", width=12, command=on_calculate)
btn_calculate.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(frame_buttons, text="Clear", width=12, command=on_clear)
btn_clear.grid(row=0, column=1, padx=10)

btn_exit = tk.Button(frame_buttons, text="Exit", width=12, command=on_exit)
btn_exit.grid(row=0, column=2, padx=10)

# Output frame
frame_output = tk.LabelFrame(root, text="Result", font=("Tahoma", 10, "bold"))
frame_output.pack(fill="x", padx=20, pady=10)

tk.Label(frame_output, text="Total Score:", font=("Tahoma", 10)).grid(row=0, column=0, sticky="e", padx=5, pady=3)
label_total_value = tk.Label(frame_output, text="--", font=("Tahoma", 10, "bold"))
label_total_value.grid(row=0, column=1, sticky="w", padx=5, pady=3)

tk.Label(frame_output, text="Grade:", font=("Tahoma", 10)).grid(row=1, column=0, sticky="e", padx=5, pady=3)
label_grade_value = tk.Label(frame_output, text="--", font=("Tahoma", 10, "bold"))
label_grade_value.grid(row=1, column=1, sticky="w", padx=5, pady=3)

tk.Label(frame_output, text="Remark:", font=("Tahoma", 10)).grid(row=2, column=0, sticky="e", padx=5, pady=3)
label_remark_value = tk.Label(frame_output, text="--", font=("Tahoma", 10, "bold"))
label_remark_value.grid(row=2, column=1, sticky="w", padx=5, pady=3)

# Records list frame
frame_records = tk.LabelFrame(root, text="Student Records", font=("Tahoma", 10, "bold"))
frame_records.pack(fill="both", expand=True, padx=20, pady=10)

listbox_records = tk.Listbox(frame_records, width=100, height=8)
listbox_records.pack(side="left", fill="both", expand=True, padx=5, pady=5)

scrollbar_records = tk.Scrollbar(frame_records, orient="vertical", command=listbox_records.yview)
scrollbar_records.pack(side="right", fill="y")

listbox_records.config(yscrollcommand=scrollbar_records.set)

root.mainloop()
