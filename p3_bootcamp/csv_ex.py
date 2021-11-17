from csv import reader, writer


def update_users(old_first, old_last, first, last):
    with open("users.csv", "r") as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        # next(csv_reader)

    count = 0
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for user in data:
            if user[0] == old_first and user[1] == old_last:
                csv_writer.writerow([first, last])
                count += 1
            else:
                csv_writer.writerow(user)

    return f"Users updated: {str(count)}."


print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
print(update_users("Colt", "Steele", "Boba", "Fett")) # Users updated: 2.
print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0.
