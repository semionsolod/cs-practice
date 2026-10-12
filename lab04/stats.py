def parse_record(line: str) -> dict:
    p = line.split(";")
    
    if len(p) != 3:
        raise ValueError(f"Полей не ровно три, их {len(p)}")
    
    city, temp_str, date = p
    
    if not city or not date:
        raise ValueError("Город или дата пустые")
    
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не число")
    
    return {
        "city": city,
        "temperature": temp,
        "date": date
    }

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
            
    return valid_records
