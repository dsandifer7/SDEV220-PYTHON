## Darrick Sandifer
## Darrick_Sandifer_M02_lab.py
## This application will determine if a student made the Dean's List or Honor Roll based on their GPA.



while True:
    lastname=input("Enter your last name or zzz to quit: ")
    if lastname.upper()=="ZZZ":
        print("Goodbye")
        break
    
    firstname=input("Enter your first name: ")
    gpa=float(input("Enter your GPA: "))
    
    if gpa >=3.5:
        print(f"{firstname} {lastname} made the Dean's List")
    elif gpa >3.25:
        print(f"{firstname} {lastname} made the Honor Roll")