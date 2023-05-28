pass_marks = 40
my_marks = int(input('Enter marks: '))

if my_marks >= pass_marks:
    if 40 <= my_marks <= 50:
        print("Grade D")
    elif 51 <= my_marks <= 60:
        print("Grade C")
    elif 61 <= my_marks <= 70:
        print("Grade B")
    elif 71 <= my_marks <= 80:
        print("Grade A-")
    elif 81 <= my_marks <= 90:
        print("Grade A")
    elif 91 <= my_marks <= 100:
        print("Grade A+")
    else: print("Invalid marks.No grade")

else: print ("Failed")