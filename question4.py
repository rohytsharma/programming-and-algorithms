marks_obtained = int(input("Enter your marks please: "))

if marks_obtained < 25:
    print("f")
elif marks_obtained >=25 and marks_obtained <45:
    print("E")
elif marks_obtained >=45 and marks_obtained<50:
    print("D")
elif marks_obtained >=50 and marks_obtained<60:
    print('C')
elif marks_obtained >=60 and marks_obtained<80:
    print("B")
elif marks_obtained >=80 and marks_obtained<=100:
    print("A")
elif marks_obtained >100:
    print("Not Valid Marks")