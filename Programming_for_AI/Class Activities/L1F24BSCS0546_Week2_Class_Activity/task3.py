def sanitize(emails):
    senetized_lists = [
        email.lower().strip()
        for email in emails
    ]

    return senetized_lists


emails = ["ALI@gooGle.coM", "sara@Yahoo.com",
"AHMED@uCP.EdU.PK"]
print(sanitize(emails))