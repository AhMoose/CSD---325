import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

filename = r'C:\Users\Obliv\Downloads\sitka_weather_2018_simple.csv'

dates = []
highs = []
lows = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            continue

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

while True:

    print("\nSitka Weather Menu")
    print("1 - Show High Temperatures")
    print("2 - Show Low Temperatures")
    print("3 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, color='red')

        plt.title("Daily High Temperatures - Sitka 2018")
        plt.xlabel("Date")
        plt.ylabel("Temperature (F)")
        plt.show()

    elif choice == "2":

        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots()
        ax.plot(dates, lows, color='blue')

        plt.title("Daily Low Temperatures - Sitka 2018")
        plt.xlabel("Date")
        plt.ylabel("Temperature (F)")
        plt.show()

    elif choice == "3":
        print("Exiting program. Goodbye!")
        sys.exit()

    else:
        print("Invalid choice. Please try again.")