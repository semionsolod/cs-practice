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

def merge_by_key(records, sprav, key):
    res = []
    for rec in records:
        dannye = sprav.get(rec.get(key), {})
        new_record = {}
        new_record.update(dannye)
        new_record.update(rec)
        res.append(new_record)
    return res

def ekranirovat_stroku(text):
    res = ""
    for symb in text:
        if symb == '"':
            res += '\\"'
        elif symb == "\\":
            res += "\\\\"
        elif symb == "\n":
            res += "\\n"
        elif symb == "\r":
            res += "\\r"
        elif symb == "\t":
            res += "\\t"
        elif symb == "\b":
            res += "\\b"
        elif symb == "\f":
            res += "\\f"
        elif ord(symb) < 32:
            res += "\\u" + format(ord(symb), "04x")
        else:
            res += symb
    return '"' + res + '"'

def perevod_v_json(value, level):
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, str):
        return ekranirovat_stroku(value)
    if isinstance(value, int) or isinstance(value, float):
        return str(value)
    if isinstance(value, list) or isinstance(value, tuple):
        if len(value) == 0:
            return "[]"
        parts = []
        for element in value:
            parts.append("  " * (level + 1) + perevod_v_json(element, level + 1))
        return "[\n" + ",\n".join(parts) + "\n" + "  " * level + "]"
    if isinstance(value, dict):
        if len(value) == 0:
            return "{}"
        parts = []
        for key in sorted(value):
            stroka = "  " * (level + 1) + ekranirovat_stroku(str(key)) + ": "
            stroka += perevod_v_json(value[key], level + 1)
            parts.append(stroka)
        return "{\n" + ",\n".join(parts) + "\n" + "  " * level + "}"
    raise TypeError("Нельзя записать в JSON: " + type(value).__name__)
