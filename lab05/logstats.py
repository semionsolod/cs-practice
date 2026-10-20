def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"Неверный формат строки: {line}")
    time, level, message = parts
    return {'time': time, 'level': level, 'message': message}
def count_levels(lines):
    counts = {}
    for line in lines:
        try:
            level = parse_event(line)['level']
        except ValueError:
            level = 'BROKEN'
        counts[level] = counts.get(level, 0) + 1
    return counts
