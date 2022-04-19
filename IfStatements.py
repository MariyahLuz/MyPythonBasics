#this program intoduces us to the if statement and it checks if a condition is true or else it continues to the next instruction.

enter_grade=int(input("Enter your grade: "))

if enter_grade >=80 :
    print('Your score is an A')
elif enter_grade >=70:
    print("Your score is B")
elif enter_grade >=60:
    print("Your score is C")
elif enter_grade >=50:
    print("Your score is D")
elif enter_grade >=40:
    print("Your score is E")
elif enter_grade >=30:
    print("Your score is F")
else:
    print("This is a total fail")




