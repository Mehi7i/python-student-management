students=[]
import json
import os
def save_students():
    print(os.getcwd())
    with open("students.json", "w") as file:
        json.dump(students,file)
# --------------------------------------------------
def load_students():
    global students
    try:
        with open("students.json","r") as file:
            students=json.load(file)
    except FileNotFoundError:
        students=[]
# ----------------------------------------------------
def add_student():
        name=input("enter  name:")
        age=get_valid_int("Enter Age:")
        score=get_valid_float("enter  score:")
        student={
        "id":get_next_id(),
        "name":name,
        "age":age,
        "score":score
        }
        students.append(student)
        save_students()
        print("Student Added Successfully")
# ----------------------------------------
def show_student():
     if not students:
           print("No students found")
           return
     else:
        for student in students:
            print(f"Id : {student['id']}")
            print(f"Name : {student['name']}")
            print(f"Age  : {student['age']}")
            print(f"Score: {student['score']}")
            print("-------------------")
# ---------------------------------------
def search_student():
        student_id=get_valid_int("Enter student ID: ")
        found = False
        for student in students:
            if student_id == student["id"]:
                found = True
                print(
                    f"Name: {student['name']}, "
                    f"Age: {student['age']}, "
                    f"Score: {student['score']}, "
                    f"ID: {student['id']}"
                )
                break
        if not found:
            print("not found")
# ----------------------------------------
def edit_student():
        student_id=get_valid_int("what id:")
        found=False
        for student in students:
            if student_id==student["id"]:
                found=True
                choise=get_edit_choice()
                if choise==1:
                        new_age=get_valid_int("new age?")
                        student["age"]=new_age
                        break
                elif choise==2:
                        new_score=get_valid_float("new score?")
                        student["score"]=new_score
                        break
                elif choise==3:
                    new_name=input("new name?")
                    student["name"]=new_name
                    break 
                print("saved")
                save_students()                    
        if not found:
            print("not dound your student")
# -------------------------------------------
def del_student():
        student_id=get_valid_int("Enter student ID: ")
        found=False
        for student in students:
            if student_id==student["id"]:
                found= True
                students.remove(student)
                save_students()
                print("saved")
                break
        if not found:
            print("not found")
# ------------------------------------------------------
def get_next_id():
    if not students:
        return 1
    else:
        return students[-1]["id"] + 1
      
# ------------------------------------
def get_valid_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("incorrect input")

def get_valid_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("incorrect input")
# --------------------------------------------------
def get_edit_choice():
    while True:
        choice = get_valid_int(
            "Which for change: 1-age, 2-score, 3-name: "
        )

        if choice in [1, 2, 3]:
            return choice

        print("wrong input")
# -------------------------------------------
load_students()
while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Edit Student")
    print("5. Delete Student")
    print("6. Exit")
    choice=input("select:")
    print("\n")

    if choice=="1":
        add_student()

    elif choice=="2":
        show_student()
    
    elif choice=="3":
        search_student()
    
    elif choice=="4":
        edit_student()
    
    elif choice=="5":
        del_student()

    elif choice=="6":
         print("Good Bye")
         break
    else:
        print("Invalid Option")