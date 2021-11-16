from csv import reader
from csv import DictReader
from csv import writer
from csv import DictWriter


# using reader
def read_csv():
    with open("fighters.csv") as file:
        csv_reader = reader(file)
        next(csv_reader)
        for fighter in csv_reader:
            print(f"{fighter[0]} is from {fighter[1]}")
    print("------------------")


def read_csv_in_list():
    with open("fighters.csv") as file:
        csv_reader = reader(file)
        data = list(csv_reader)
        print(data)
    print("------------------")


#using DictReader - ordered list
def read_csv_dict():
    with open("fighters.csv") as file:
        csv_reader = DictReader(file)
        for fighter in csv_reader:
            print(fighter)
    print("------------------")


def read_csv_dict_delim():
    with open("fighters2.csv") as file:
        csv_reader = DictReader(file, delimiter="|")
        for fighter in csv_reader:
            print(f"{fighter['Name']} from {fighter['Country']}")
    print("------------------")


# using writer
def write_csv():
    with open("dogs.csv", "w") as file:
        csv_writer = writer(file)
        csv_writer.writerow(["Name", "Age"])
        csv_writer.writerow(["Shpizyk", "2"])
        csv_writer.writerow(["Doggy", "3"])
    print("------------------")


def read_write_csv_1():
    with open("fighters.csv") as file:
        csv_reader = reader(file)
        fighters = [[s.upper() for s in row] for row in csv_reader]

    with open("modify_fighters.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in fighters:
            csv_writer.writerow(fighter)


def read_write_csv():
    with open("fighters.csv") as file:
        csv_reader = reader(file)
        with open("modify_fighters.csv", "w") as file:
            csv_writer = writer(file)
            for fighter in csv_reader:
                csv_writer.writerow([s.upper() for s in fighter])


# using DictWriter
def write_csv_dict():
    with open("dogs.csv", "w") as file:
        headers = ["Name", "Breed", "Age"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerow({
            "Name": "Shpizyk",
            "Breed": "Shpitz",
            "Age": "3"
        })


def run():
    # read_csv()
    # read_csv_in_list()
    # read_csv_dict()
    # read_csv_dict_delim()
    # write_csv()
    # read_write_csv()
    write_csv_dict()


if __name__ == "__main__":
    run()
