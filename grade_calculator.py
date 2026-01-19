"""
Grade Calculator Program
Author: Student
Description:
- Takes marks input from the user
- Uses conditional statements and logical operators
- Handles invalid input
- Simulates real-world grading rules
"""

def calculate_grade(marks, attendance):
    """
    Determines grade based on marks and attendance.
    """

    # Invalid marks check
    if marks < 0 or marks > 100:
        return "❌ Invalid marks! Please enter a value between 0 and 100."

    # Attendance rule (business logic simulation)
    if attendance < 75:
        return "❌ Failed due to low attendance (below 75%)."

    # Grade calculation
    if marks >= 90:
        return "🏆 Grade A+ : Excellent performance!"
    elif marks >= 80:
        return "🥇 Grade A : Very good job!"
    elif marks >= 70:
        return "🥈 Grade B : Good effort!"
    elif marks >= 60:
        return "🥉 Grade C : You passed."
    elif marks >= 50:
        return "⚠️ Grade D : Needs improvement."
    else:
        return "❌ Grade F : Failed."


def get_user_input():
    """
    Takes user input safely.
    """
    try:
        marks = float(input("Enter your marks (0 - 100): "))
        attendance = float(input("Enter your attendance percentage: "))
        return marks, attendance
    except ValueError:
        return None, None


def main():
    """
    Main program execution.
    """
    print("📘 Welcome to the Grade Calculator 📘")
    print("-" * 40)

    marks, attendance = get_user_input()

    if marks is None or attendance is None:
        print("❌ Invalid input! Please enter numeric values only.")
    else:
        result = calculate_grade(marks, attendance)
        print("\nResult:")
        print(result)


# Run program
if __name__ == "__main__":
    main()
