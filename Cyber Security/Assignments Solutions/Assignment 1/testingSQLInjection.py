while True:
    username = input("Username: ")
    password = input("Password: ")

    query = (
        "SELECT * FROM users WHERE username = '"
        + username
        + "' AND password = '"
        + password
        + "'"
    )

    print(query)