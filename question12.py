user_input = input("Enter a single character: ")
if len(user_input) == 1:
    if user_input.isupper():
        print(f"'{user_input}' is an uppercase letter.")
    elif user_input.islower():
        print(f"'{user_input}' is a lowercase letter.")
    elif user_input.isdigit():
        print(f"'{user_input}' is a digit.")
    else:
        print(f"'{user_input}' is neither an uppercase letter, a lowercase letter, nor a digit.")
else:
    print("Please enter only a single character!")