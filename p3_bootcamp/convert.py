from csv import DictReader, DictWriter


def cm_to_in(cm):
    return round(float(cm) * 0.393701, 2)


def add_inch():
    # open csv file for read and save all info into list fighters
    with open("fighters.csv") as file:
        csv_reader = DictReader(file)
        fighters = list(csv_reader)

    # open csv file for write and write data with modification of the last column
    with open("fighters_inches.csv", "w") as file:
        headers = ("Name", "Country", "Height")
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for fighter in fighters:
            csv_writer.writerow({
                "Name": fighter["Name"],
                "Country": fighter["Country"],
                "Height": cm_to_in(fighter["Height (in cm)"])
            })


def run():
    add_inch()


if __name__ == "__main__":
    run()