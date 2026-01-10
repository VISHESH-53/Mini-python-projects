email=input("Enter your email address: ")
if len(email) > 7:
    if "@" in email and email.count("@") == 1:
        if email.endswith(".com") or email.endswith(".in") or email.endswith(".org"):
            print("Valid email address")
        else:
            print("Invalid email address: Domain must end with .com, .in, or .org")
    else:
        print("Invalid email address: Must contain exactly one '@' symbol")