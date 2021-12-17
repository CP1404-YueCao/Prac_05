def main():
    """Creat a dictionary of emails and names"""
    email_and_name = {}
    while email != "":
        name = get_name(email)
        confirmation = input("Is your name {}? (Y/n)".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_and_name[email] = name
        email = input("Email: ")
    for email, name in email_and_name.items():
        print(f"{name} ({email})")


main()