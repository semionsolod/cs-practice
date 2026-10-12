
import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    data = sys.stdin.read().splitlines()
    
    records = read_valid(data)
    non_empty = [line for line in data if line.strip()]
    skipped_count = len(non_empty) - len(records)

    if records:
        best_city = warmest_city(records)
        averages = average_by_city(records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0
    
    print(len(records))
    print(skipped_count)
    print(f"{best_temp:.1f}")

if __name__ == "__main__":
    main()
