# Student Performance Analytics System

Beginner-friendly Python data analysis project using Python, Pandas and NumPy.

## Features
- Loads 20 fictional student records from `students.csv` with Pandas.
- Checks required columns.
- Uses NumPy for per-student total and average marks.
- Assigns grades, pass/fail results, and attendance status.
- Reports class average, highest/lowest student average, pass/fail counts and pass percentage.
- Reports subject averages, best/lowest subject, top three students and department averages.
- Saves calculated results to `student_performance_results.csv`.

## Requirements
Python 3.10+, Pandas and NumPy.

## Run on Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```
If `.venv` already exists, skip the first command. Keep `main.py` and `students.csv` in the same folder.

## Grade rules
A+ = average >= 90; A = 80–89.99; B = 70–79.99; C = 60–69.99; D = 50–59.99; F = below 50.

A student passes only if every subject mark is at least 40. Attendance is `Good` at 75% or above and `Low` below 75%; attendance does not affect pass/fail.

## Dataset
`students.csv` has 20 fictional records with ID, name, department, marks in Python, Mathematics and Data Analysis, plus attendance percentage. Do not treat this sample data as real student records.

## Project structure
- `main.py` — loading, calculations and reports
- `students.csv` — sample data
- `requirements.txt` — dependencies
- `Project_Documentation/Project_Documentation.md` — project report

## GitHub submission
Create a repository named `student-performance-analytics`, then run in this folder:
```bash
git init
git add .
git commit -m "Add student performance analytics project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-performance-analytics.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your GitHub username. Verify the files are visible and submit the repository URL through the Google Form supplied by EWB.
