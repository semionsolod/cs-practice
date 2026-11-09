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

def preobrazovat_znachenie(text):
    mal = text.lower()
    if mal == "true" or mal == "yes":
        return True
    if mal == "false" or mal == "no":
        return False
    if text.startswith("-"):
        bez_minus = text[1:]
    else:
        bez_minus = text
    if bez_minus.isdecimal():
        return int(text)
    parts = bez_minus.split(".")
    if len(parts) == 2 and parts[0].isdecimal() and parts[1].isdecimal():
        return float(text)
    return text

def parse_settings(stroki):
    settings = {}
    tekushiy_spisok = None
    for stroka in stroki:
        stroka = stroka.split("#")[0].strip()
        if stroka == "":
            continue
        if stroka == "-" or stroka.startswith("- "):
            if tekushiy_spisok is not None:
                tekushiy_spisok.append(preobrazovat_znachenie(stroka[1:].strip()))
            continue
        key, dvoetochie, value = stroka.partition(":")
        if dvoetochie == "":
            continue
        key = key.strip()
        value = value.strip()
        if value == "":
            tekushiy_spisok = []
            settings[key] = tekushiy_spisok
        else:
            settings[key] = preobrazovat_znachenie(value)
            tekushiy_spisok = None
    return settings
