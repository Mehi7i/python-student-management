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
    try:
       
        name=input("enter  name:")
        while True:
            try:
                age=int(input("enter  age:"))
                break
            except ValueError:
                  print("incorrect input")
        while True:          
            try:
                score=float(input("enter  score:"))
                break
            except ValueError:
                print("incorrect input")
        student={
        "id":get_next_id(),
        "name":name,
        "age":age,
        "score":score
        }
        students.append(student)
        save_students()
        print("Student Added Successfully")
    except ValueError:
         print("incorrect input")
         return
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
    try:
        vorudi = int(input("what ID:"))

        found = False

        for student in students:
            if vorudi == student["id"]:
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

    except ValueError:
        print("incorrect input")      
# ----------------------------------------
def edit_student():
    try:
        while True:
            try:
                vorudi=int(input(f"what id:"))
                break
            except ValueError:
                print("incorrect input") 
        found=False
        for student in students:
            if vorudi==student["id"]:
                found=True
                while True:
                    try:
                        vorudy=int(input(f"whch for change: 1-edit age:{student['age']}, 2-edit score:{student['score']}:, 3-edit name:{student['name']}"))
                        if vorudy in [1, 2, 3]:
                            break
                        else:
                            print("wrong input")
                    except ValueError:
                        print("incorrect input")
                if vorudy==1:
                    while True:
                        try:
                            new_age=int(input("new age?"))
                            student["age"]=new_age
                            print("saved")
                            break
                        except ValueError:
                            print("incorrect input")
                    save_students()
                    break
                elif vorudy==2:
                    while True:
                        try:
                            new_score=float(input("new score?"))
                            student["score"]=new_score
                            save_students()    
                            print("saved")
                            break
                        except ValueError:
                            print("incorrect input")
                elif vorudy==3:
                    new_name=input("new name?")
                    student["name"]=new_name
                    print("saved")
                    save_students()
                    break                     
        if not found:
            print("not dound your student")
    except ValueError:
        print("incorrect input")
# -------------------------------------------
def del_student():
    try:
        student_id=int(input("which student?"))
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
    except ValueError:
            print("incorrect input")
# ------------------------------------------------------
def get_next_id():
    if not students:
        return 1
    else:
        return students[-1]["id"] + 1
      




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




