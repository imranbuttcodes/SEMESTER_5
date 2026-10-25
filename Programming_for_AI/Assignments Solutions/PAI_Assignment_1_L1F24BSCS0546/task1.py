import csv

scp_dict = {}

with open("scp_statements.csv", "r") as file:
    reader = csv.DictReader(file)

    scp_dict = {
        row[reader.fieldnames[0]]: row[reader.fieldnames[1]]

        for row in reader

        if row[reader.fieldnames[7]] == "Myocardial Infarction"
    }


    print(scp_dict)