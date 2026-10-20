import sys
from logstats import count_levels, top_errors, format_report

def main():
    with open("events.log", encoding="utf-8") as f:
        lines = f.readlines()

    counts = count_levels(lines)
    all_errors = top_errors(lines, n=10**9)   
    print( len(lines))
    print( counts.get("ERROR", 0))
    unique = set(msg for msg, count in all_errors if msg.strip())
    print(len(unique))

    report_errors = all_errors[:5]            
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(format_report(counts, report_errors))

if __name__ == "__main__":
    main()
