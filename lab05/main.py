import sys
import logstats

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else input().strip()

    total = 0
    err = 0
    bad = 0

    with open(name, "r", encoding="utf-8") as f:
        for line in f:
            total += 1
            try:
                if logstats.parse_event(line)["level"] == "ERROR":
                    err += 1
            except ValueError:
                bad += 1

    print(total)
    print(err)
    print(bad)

    with open(name, "r", encoding="utf-8") as f:
        data = f.readlines()

    c = logstats.count_levels(data)
    t = logstats.top_errors(data, 3)
    txt = logstats.format_report(c, t)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(txt)

if __name__ == "__main__":
    main()
