# Student Grade Calculator

A simple Python project that calculates a student's average marks, assigns a grade, and determines whether the student has passed or failed.

## Features

- Input student name
- Input marks for multiple subjects
- Calculate average marks
- Assign grade based on average
- Display Pass/Fail status
- User-friendly output

## Concepts Used

- Variables
- Lists
- Loops
- Functions
- Conditional Statements (if-elif-else)
- User Input
- Basic Python Programming

## Project Structure

```text
student-grade-calculator/
│
├── grade_calculator.py
├── README.md
└── .gitignore
```

## How It Works

1. Enter the student's name.
2. Enter the number of subjects.
3. Enter marks for each subject.
4. The program calculates:
   - Average Marks
   - Grade
   - Pass/Fail Status
5. Results are displayed on the screen.

## Grade Criteria

| Average Marks | Grade |
|--------------|-------|
| 90 and above | A+ |
| 80 - 89      | A |
| 70 - 79      | B |
| 60 - 69      | C |
| 50 - 59      | D |
| Below 50     | F |

## Example Output

```text
===== Student Grade Calculator =====

Enter Student Name: Rena
Enter Number of Subjects: 5

Enter Mark for Subject 1: 95
Enter Mark for Subject 2: 88
Enter Mark for Subject 3: 90
Enter Mark for Subject 4: 92
Enter Mark for Subject 5: 85

===== RESULT =====

Student Name : Rena
Average Marks: 90.0
Grade        : A+
Status       : PASS
```

## Requirements

- Python 3.x

## How to Run

### Clone the Repository

```bash
git clone https://github.com/your-username/student-grade-calculator.git
```

### Navigate to the Project Folder

```bash
cd student-grade-calculator
```

### Run the Program

```bash
python grade_calculator.py
```

## Future Improvements

- Calculate total marks
- Find highest and lowest marks
- Add percentage calculation
- Input validation for marks
- Save results to a file
- Create a graphical user interface (GUI)

## Author

**Rena Roy V S**

Computer Science Engineering Student at LICET, Chennai, India.
Interested in Quantum Computing, Aerospace, AI, and Python Development.

## License

This project is open source and available under the MIT License.