import pandas as pd
import numpy as np

DATA_FILE = "students.csv"
SUBJECTS = ["Python", "Mathematics", "Data_Analysis"]
PASS_MARK = 40
ATTENDANCE_WARNING = 75

def load_data(file_name=DATA_FILE):
    """Load CSV data and verify the expected columns."""
    data = pd.read_csv(file_name)
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError("Missing columns: " + ", ".join(missing))
    return data

def assign_grade(average):
    """Assign a grade based on average marks."""
    if average >= 90: return "A+"
    elif average >= 80: return "A"
    elif average >= 70: return "B"
    elif average >= 60: return "C"
    elif average >= 50: return "D"
    return "F"

def process_results(data):
    data = data.copy()
    marks = data[SUBJECTS].to_numpy(dtype=float)
    data["Total_Marks"] = np.sum(marks, axis=1)
    data["Average_Marks"] = np.round(np.mean(marks, axis=1), 2)
    grades, results = [], []
    for average, subject_marks in zip(data["Average_Marks"], marks):
        grades.append(assign_grade(average))
        results.append("Pass" if all(mark >= PASS_MARK for mark in subject_marks) else "Fail")
    data["Grade"] = grades
    data["Result"] = results
    data["Attendance_Status"] = ["Good" if x >= ATTENDANCE_WARNING else "Low" for x in data["Attendance"]]
    return data

def show_student_summary(data):
    print("\\n=== STUDENT PERFORMANCE SUMMARY ===")
    cols = ["Student_ID","Name","Department","Total_Marks","Average_Marks","Grade","Result","Attendance_Status"]
    print(data[cols].to_string(index=False))

def show_class_analysis(data):
    averages = data["Average_Marks"].to_numpy()
    print("\n=== CLASS ANALYSIS ===")
    print(f"Number of students: {len(data)}")
    print(f"Overall class average: {np.mean(averages):.2f}")
    print(f"Highest student average: {np.max(averages):.2f}")
    print(f"Lowest student average: {np.min(averages):.2f}")
    passed = (data["Result"] == "Pass").sum()
    failed = (data["Result"] == "Fail").sum()
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Pass percentage: {passed / len(data) * 100:.2f}%")

def show_subject_analysis(data):
    print("\\n=== SUBJECT-WISE ANALYSIS ===")
    averages = data[SUBJECTS].mean()
    for subject in SUBJECTS:
        print(f"{subject.replace('_',' ')} average: {averages[subject]:.2f}")
    print("Best-performing subject:", averages.idxmax().replace("_"," "))
    print("Lowest-performing subject:", averages.idxmin().replace("_"," "))

def show_top_performers(data, count=3):
    print(f"\\n=== TOP {count} PERFORMERS ===")
    top = data.sort_values("Average_Marks", ascending=False).head(count)
    print(top[["Student_ID","Name","Department","Average_Marks","Grade"]].to_string(index=False))

def main():
    try:
        raw = load_data()
        data = process_results(raw)
        print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
        print("Dataset preview:")
        print(raw.head().to_string(index=False))
        print(f"\\nDataset contains {len(raw)} records and {len(raw.columns)} original columns.")
        show_student_summary(data)
        show_class_analysis(data)
        show_subject_analysis(data)
        show_top_performers(data)
        print("\\n=== DEPARTMENT-WISE AVERAGE ===")
        print(data.groupby("Department")["Average_Marks"].mean().round(2).to_string())
        data.to_csv("student_performance_results.csv", index=False)
        print("\\nSaved results to student_performance_results.csv")
    except FileNotFoundError:
        print(f"Error: '{DATA_FILE}' not found. Keep it beside main.py.")
    except (ValueError, pd.errors.ParserError) as error:
        print("Could not process dataset:", error)

if __name__ == "__main__":
    main()
