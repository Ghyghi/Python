'''
To practice the python fundamentals, we will create a simple grading system.
'''
def greeting(func):
    def wrapper(*args, **kwargs):
        print("Welcome back to the school's grading system.")
        return func(*args, **kwargs)
    return wrapper

def get_grade(stuList):
    for kid in stuList:
        mark = int(kid['grade'])
        match mark:
            case mark if mark >=95:
                print(f"{kid['name']} has got A+")
            case mark if mark >=80 and mark <= 94:
                print(f"{kid['name']} has got A")
            case mark if mark >=70 and mark<= 79:
                print(f"{kid['name']} has got B")
            case mark if mark >= 60 and mark <= 69:
                print(f"{kid['name']} has got C")
            case mark if mark >= 50 and mark <= 59:
                print(f"{kid['name']} has got D")
            case _:
                print(f"{kid['name']} has got F")

def get_class_average(stuList):
    try:
        sum = 0
        grades = [student['grade'] for student in stuList]
        for grade in grades:
            sum += grade
        average = sum/len(grades)
        print(f'Class average: {average:.2f}')
    except:
        print("Error calculating the average")

def get_student_grade(name, stuList):
    for student in stuList:
        if student['name'] == name:
            print(f"{name} has {student['grade']}%")
            return
    print(f"{name} doesn't exist")

def grade_filtering(mark, stuList, filter='5'):
    filters = {
        '1': 'Greater than',
        '2': 'Less than',
        '3': 'Equal to',
        '4': 'Less than or equal to',
        '5': 'Greater than or equal to',
    }
    print(f"Filtering for {mark} using the {filters[filter]} filter")
    for student in stuList:
        match filter:
            case '1':
                if student['grade'] > mark:
                    print(f"{student['name']}")
            case '2':
                if student['grade'] < mark:
                    print(f"{student['name']}")
            case '3':
                if student['grade'] == mark:
                    print(f"{student['name']}")
            case '4':
                if student['grade'] <= mark:
                    print(f"{student['name']}")
            case '5':
                if student['grade'] >= mark:
                    print(f"{student['name']}")
            case _:
                print("Invalid choice")

def top_students(stuList):
    students = [student['name'] for student in stuList if student.get('grade', 0) >= 80]
    print(students)


@greeting
def main():
    students = [
        {'name' : 'Alice','grade': 80},
        {'name' : 'Bob','grade': 40},
        {'name' : 'Grace','grade': 30},
        {'name' : 'Tammy','grade': 20},
        {'name' : 'Elvis','grade': 70},
        {'name' : 'Gray','grade': 10},
        {'name' : 'Mart','grade': 100},
        {'name' : 'Lewis','grade': 75},
    ]
    option=input("Enter 1 for class grades, 2 for class average, 3 for a student's grade, 4 for grade filtering, 5 for top students: ")
    match option:
        case '1':
            get_grade(students)
        case '2':
            get_class_average(students)
        case '3':
            x = input("Enter Student Name: ")
            get_student_grade(x, students)
        case '4':
            try:
                x = int(input("Enter grade to filter for: "))
            except:
                print("Enter a number")
            filter = input("Which filter: 1 for greater, 2 for less, 3 for equal, 4 for <=. Default is >=, leave empty to use the default: ")
            if filter:
                grade_filtering(x, students, filter)
            else:
                grade_filtering(x, students)
        case '5':
            top_students(students)
        case _:
            print("Invalid choice")

if __name__ == "__main__":
    main()