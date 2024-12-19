user_input = input("enter Character: ")
a= "aeiouAEIOU"
if user_input in a:
    print(f"{user_input} is a vowel")
else:
    print(f"{user_input} is a constant")