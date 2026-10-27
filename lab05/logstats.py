def parse_event(line):
    parts = line.strip().split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("bad line")
    return {"time": parts[0], "level": parts[1], "message": parts[2]}

def count_levels(lines):
    res = {}
    for line in lines:
        try:
            lvl = parse_event(line)["level"]
        except (ValueError, KeyError):
            lvl = "BROKEN"
        res[lvl] = res.get(lvl, 0) + 1
    return res

def top_errors(lines, n):
    res = {}
    for line in lines:
        try:
            ev = parse_event(line)
            if ev["level"] == "ERROR":
                msg = ev["message"]
                res[msg] = res.get(msg, 0) + 1
        except (ValueError, KeyError):
            pass
    
    sorted_list = sorted(res.items(), key=lambda x: (-x[1], x[0]))
    return sorted_list[:n]

def format_report(counts, errors):
    out = []
    out.append("Отчёт по журналу")
    out.append("")
    for k in sorted(counts.keys()):
        out.append(f"{k}: {counts[k]}")
    
    out.append("")
    out.append("Частые ошибки:")
    for msg, cnt in errors:
        out.append(f"- {msg} — {cnt}")
        
    return "\n".join(out)+"/n"
