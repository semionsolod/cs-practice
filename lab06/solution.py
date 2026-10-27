def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for p in paths:
        name = p.split("/")[-1]
        dot = name.rfind(".")
        if dot > 0:
            ext = name[dot + 1:].lower()
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))

def human_size(n_bytes: int) -> str:
    names = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes
    i = 0
    while size >= 1024 and i < len(names) - 1:
        size /= 1024
        i += 1
    if i == 0:
        return f"{n_bytes} Б"
    return f"{size:.1f} {names[i]}"
