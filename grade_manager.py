import grade_utils
try:
    name=input("enter student name: ")
    marks = int(input("enter marks: "))
    grade=grade_utils.calculate_grade(marks)
    with open("results.txt", "a") as file:
        file.write(f"name:{name},grade:{grade}\n")
    print("result saved successfully!")
except ValueError:
    print("Invalid marks! please enter a number.")
finally:
    print("process complete")
