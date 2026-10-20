def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"Неверный формат строки: {line}")
    time, level, message = parts
    return {'time': time, 'level': level, 'message': message}
