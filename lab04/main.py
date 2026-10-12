
import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    data = sys.stdin.read().splitlines()
    
    records = read_valid(data)
    
    skipped_count = len(data) - len(records)
    
    if records:
        best_city = warmest_city(records)
        averages = average_by_city(records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0
    
    print(len(records))
    print(skipped_count)
    print(best_temp)

if __name__ == "__main__":
    main()
