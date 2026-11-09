def csv_to_records(text):
    stroki = text.splitlines()
    records = []
    if len(stroki) == 0:
        return records
    zaglav = stroki[0].split(",")
    for stroka in stroki[1:]:
        if stroka.strip() == "":
            continue
        znach = stroka.split(",")
        records.append(dict(zip(zaglav, znach)))
    return records
