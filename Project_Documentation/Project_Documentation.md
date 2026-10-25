# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details
**Project:** Student Performance Analytics System  
**Student:** [Enter your name]  
**Course:** Python with AI  
**Organization:** EWB Courses

## 2. Objective
Analyse student marks and attendance using Python, Pandas and NumPy. Calculate totals and averages, assign grades, identify pass/fail status, compare subjects and report top performers.

## 3. Technologies Used
Python, Pandas, NumPy and CSV.

## 4. Dataset Description
The included `students.csv` contains 20 fictional records. Columns: Student_ID, Name, Department, Python, Mathematics, Data_Analysis and Attendance. Marks are out of 100; attendance is a percentage.

## 5. Implementation
1. `load_data()` reads the CSV using Pandas and checks required columns.
2. `process_results()` converts subject marks to a NumPy array and calculates total and average marks.
3. `assign_grade()` assigns grades using the documented scale.
4. A loop checks whether each student scores at least 40 in every subject.
5. Reporting functions display student summaries, class statistics, subject averages and top performers.
6. Pandas saves calculated results to `student_performance_results.csv`.

## 6. Key Features
Student totals and averages; grades; pass/fail; class average and highest/lowest average; subject averages; top three performers; department averages; attendance warning; CSV results output.

## 7. Output / Screenshots
Run `main.py` and capture a screenshot showing the dataset preview and reports. Add your actual screenshot here or commit it to the repository.

## 8. Final Outcome
The system converts raw CSV student data into a readable performance report and a processed CSV file using introductory data-analysis techniques.

## 9. Challenges and Learning
The project practises CSV reading, DataFrame operations, NumPy calculations, functions, loops, conditions and readable output. Add any challenges you personally faced and how you resolved them.

## 10. GitHub Repository
Repository URL: [Paste your final GitHub repository URL here]

## Rules
Grades: A+ >= 90; A >= 80; B >= 70; C >= 60; D >= 50; F < 50. Pass requires at least 40 marks in every subject. Attendance is Good at 75% or above; otherwise Low.
