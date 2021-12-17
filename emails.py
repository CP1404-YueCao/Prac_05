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


def get_name(email):
    """Pick expected name from emails"""
    pre = email.split('@')[0]
    parts = pre.split('.')
    name = " ".join(parts).title()
    return name


main()