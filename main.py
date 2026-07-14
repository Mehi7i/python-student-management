students=[]
import json
import os
def save_students():
    print(os.getcwd())
    with open("students.json", "w") as file:
        json.dump(students,file)

def load_students():
    global students
    try:
        with open("students.json","r") as file:
            students=json.load(file)
    except FileNotFoundError:
        students=[]

def add_student():

    name=input("enter  name:")
    age=int(input("enter  age:"))
    score=float(input("enter  score:"))
    student={
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
            print(f"Name : {student['name']}")
            print(f"Age  : {student['age']}")
            print(f"Score: {student['score']}")
            print("-------------------")

# ---------------------------------------
def search_student():
    vorudi=input(f"what name:")
    found=False
    for student in students:
        if vorudi==student["name"]:
            found=True
            print(f"Name: {student['name']}, Age: {student['age']}, Score: {student['score']}")
            break
    if not found:
        print("not found")
# ----------------------------------------
def edit_student():
    vorudi=input(f"what name:")
    found=False
    for student in students:
        if vorudi==student["name"]:
            found=True
            vorudy=int(input(f"whch for change: 1-edit age:{student['age']}, 2-edit score:{student['score']}:, 3-edit name:{student['name']}"))
            if vorudy==1:
                new_age=int(input("new age?"))
                student["age"]=new_age
                print("saved")
                save_students()
                break
            elif vorudy==2:
                new_score=float(input("new score?"))
                student["score"]=new_score
                save_students()
                print("saved")
                break
            elif vorudy==3:
                new_name=input("new name?")
                student["name"]=new_name
                print("saved")
                save_students()    
            else:
                print("wrong input")
    if not found:
        print("not dound your student")

# -------------------------------------------
def del_student():
    entekhab=input("which student?")
    found=False
    for student in students:
        if entekhab==student["name"]:
            found= True
            students.remove(student)
            save_students()
            print("saved")
            break
    if not found:
        print("not found")


# -------------------------------------------
load_students()
while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Edit Student")
    print("5. Delete Student")
    print("6. Exiف")
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




