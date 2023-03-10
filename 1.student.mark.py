def pause():
    pass


def input_number(unit):
    return int(input(f"enter the number of {unit} in this class:"))


def input_infos(item_type, infos):
    item = {}
    for info in infos:
        item[info] = input(f"\tEnter the {item_type}'s {info}:")
    return item


def display(lst):
    for i, item in enumerate(lst):
        print(f"{1 + i}, {item}")


def input_marks(student, course_id):
    if "marks" not in student:
        student["marks"] = {}
    student["marks"][course_id] = input("enter the student mark for the class ")


def list_students(students):
    if len(students) <= 0:
        print("There aren't any student yet ")
        return1
    print(" here is the student list: ")
    for i, student in enumerate(students):
        print(f"{i + 1}. {student['id']} - {student['name']} - {student['DoB']}")
        if "marks" in student:
            print("Marks (course Id - Mark):", end="")
            for course_id, mark in student["marks"].items():
                print(f"({course_id} - {mark})", end="\t")
            print()


def list_courses(courses):
    if len(courses) <= 0:
        print("there aren't any courses yet")
        return
    print("here is the course list ")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course['id']} - {course['name']}")


def select(option_range, input_message="choose an option: "):
    selection = input(input_message)
    if not selection.isnumeric():
        return -1
    selection = int(selection)
    if selection not in option_range:
        return -1
    return selection


def main():
    course = []
    student = []
    num_students = 0
    num_courses = 0
    while True:
        print("""

     0. exit 
     1. input number of students"
     2. input student information (id,name,DoB)"
     3. input number of courses "
     4. input course information (id,name)"
     5. input marks for student in a course"
     6. list course"
     7. list students         
              """)
        selection = select(range(0, 8))
        if selection == 0:
            break
        elif selection == 1:
            num_students = input_number("students")
            print(f"there are {num_students} student(s) in this class")
        elif selection == 2:
            if num_students <= 0:
                print("pleas input the number of student first")
                pause()
                continue
            students = []
            for i in range(num_students):
                print(f"student No. {i + 1}")
                students.append(input_infos("student", ("id", "name", "DoB")))
            list_students(students)
        elif selection == 3:
            num_courses = input_number("courses")
            print(f" there are {num_courses} course(s) in this class")
        elif selection == 4:
            if num_courses <= 0:
                print("pleas input the number of course first ")
                pause()
                continue
            courses = []
            for i in range(num_courses):
                print(f"Course No. {i + 1}")
                courses.append(input_infos("course", ("id", "name")))
            list_courses(courses)
        elif selection == 5:
            list_courses(course)
            if len(course) > 0:
                selected_course = select(range(1, num_courses + 1), "sele")
                if selected_course < 0:
                    print("invalid input ")
                else:
                    for i in range(num_students):
                        print(f"Student . No {i + 1}. {student[i]['name']}", end="\t")
                        input_marks(student[i], course[selected_course])
        elif selection == 6:
            list_courses(course)
        elif selection == 7:
            list_students(student)
        else:
            print("invalid input: pleas try agian ")
        pause()


if __name__ == "__main__":
    main()
