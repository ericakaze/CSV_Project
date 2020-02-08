import matplotlib.pyplot as plt
import csv
from datetime import datetime 

open_file= open("death_valley_2018_simple.csv", "r")
open_file= open("sitka_weather_07-2018_simple.csv", "r")
place_name = ''

csv_file=csv.reader(open_file, delimiter=",")

header_row= next (csv_file)

print(type(header_row))

date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

for index, column_header in enumerate (header_row):
    print(index, column_header)

highs =[]
dates= []
lows= []
for row in csv_file:

        if not place_name:
            place_name = row[name_index]
            print(place_name)
        
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

""" fig, ax = plt.subplots(2,2)

plt.subplot(dates, highs,color='red', alpha=0.5)
plt.subplot(dates, lows, color='blue', alpha=0.5) """

fig, (ax1, ax2)= plt.subplots(2,2)
ax1.plot(dates, highs,lows, color='red', alpha=0.5)
ax1.set_title('Highs')
ax2.plot(dates, highs,lows, color='blue', alpha=0.5)
ax2.set_title('lows')

plt.show()


""" plt.plot(dates, highs,color='red', alpha=0.5)
plt.plot(dates, lows, color='blue', alpha=0.5)

plt.fill_between(dates,highs,lows,facecolor="blue", alpha=0.3)
plt.title("daily high temps for death valley 2018", fontsize=16)
plt.xlabel ("", fontsize=8)
plt.ylabel ("Temperature (F)", fontsize=12)
plt.tick_params (axis='both', which="major", labelsize=12)

fig.autofmt_xdate() """