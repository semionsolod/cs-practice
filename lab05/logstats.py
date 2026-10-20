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
def top_errors(lines, n):
    errors = {}
    for line in lines:
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event['level'] == 'ERROR':
            msg = event['message']
            errors[msg] = errors.get(msg, 0) + 1
    return sorted(errors.items(), key=lambda item: (-item[1], item[0]))[:n]
def format_report(counts, errors):
    lines = ["Отчёт по журналу:"]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    if not errors:
        lines.append("-")      
    else:
        for msg, cnt in errors:
            lines.append(f"- {msg} — {cnt}")
    return "\n".join(lines) + "\n"
