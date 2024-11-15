import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    #read remaining row[TMAX]
    dates, highs = [], []

    for row in reader:
        high = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(high)

print(highs)
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.set_title("Daily high temporature, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()

#for index, column_header in enumerate(header_row):
#    print(index, column_header)

