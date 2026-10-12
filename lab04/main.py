
import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    data = sys.stdin.read().splitlines()
    
    records, skipped_count = read_valid(data)
    
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
