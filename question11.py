user_age= int(input("Enter your Age: "))

if user_age < 13:
    print(f"Your age is {user_age}, so you are a child")
elif 13<=user_age<=19:
    print(f"Your age is {user_age},so you are a Teenager")
elif user_age > 19:
    print(f"your age is {user_age}, so you are an adult")