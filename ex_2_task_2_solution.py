# solution (needs to go between the 2 your code here lines!)

while attempts_left > 0:
    email = input("What's your email address?")
    r, err_str = is_valid_email_address(email)

    if r == None:
        print(email, "is valid!")
        break
    # error
    else:
        attempts_left -= 1
        print(email, "is invalid!")
        print("Reason:", err_str)
        if attempts_left > 0:
            print(f"Try again, {attempts_left} attempts left")
        else:
            print("No attempts left, bailing out")
