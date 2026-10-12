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

def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    
    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        
        totals[city] = totals.get(city, 0) + temp
        counts[city] = counts.get(city, 0) + 1
        
    averages = {}
    for city in totals:
        averages[city] = round(totals[city] / counts[city], 1)
        
    return averages

def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    
    if not averages:
        return ""
    
    sorted_cities = sorted(averages.items(), key=lambda item: (-item[1], item[0]))
    
    return sorted_cities[0][0]
