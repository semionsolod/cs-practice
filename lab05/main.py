from logstats import count_levels, top_errors, format_report

def main():
    with open("events.log", encoding="utf-8") as f:
        lines = f.readlines()

    counts = count_levels(lines)
    all_errors = top_errors(lines, n=10**9)   # получаем ВСЕ уникальные ошибки

    print("Строк всего:", len(lines))
    print("Уровней ERROR:", counts.get("ERROR", 0))
    print("Уникальных сообщений ERROR:", len(all_errors))

    report_errors = all_errors[:5]            # в отчёт — 5 самых частых
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(format_report(counts, report_errors))

if __name__ == "__main__":
    main()
