import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_sitka = 'data/sitka_weather_2018_simple.csv'
filename_deathvalley = 'data/death_valley_2018_simple.csv'
with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    #read remaining row[TMAX]
    dates_stika, rains_stika, highs_stika, lows_stika = [], [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain_stika = float(row[3])
            high_stika = int(row[5])
            low_stika = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_stika.append(current_date)
            rains_stika.append(rain_stika)
            highs_stika.append(high_stika)
            lows_stika.append(low_stika)

with open(filename_deathvalley) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    dates_deathvalley, rains_deathvalley, highs_deathvalley, lows_deathvalley = [], [], [], []

    for row in reader:
        current_date_deathvalley = datetime.strptime(row[header_row.index("DATE")], '%Y-%m-%d')
        try:
            rain_deathvalley = float(row[header_row.index("PRCP")])
            high_deathvalley = int(row[header_row.index("TMAX")])
            low_deathvalley = int(row[header_row.index("TMIN")])
        except ValueError:
            print(f"Missing data for {current_date_deathvalley}")
        else:
            dates_deathvalley.append(current_date_deathvalley)
            rains_deathvalley.append(rain_deathvalley)
            highs_deathvalley.append(high_deathvalley)
            lows_deathvalley.append(low_deathvalley)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_deathvalley, highs_deathvalley, c='red')
ax.plot(dates_deathvalley, lows_deathvalley, c='yellow')
ax.fill_between(dates_deathvalley, highs_deathvalley, lows_deathvalley, facecolor='blue', alpha=0.1)

ax.plot(dates_stika, highs_stika, c='blue')
ax.plot(dates_stika, lows_stika, c='green')
ax.fill_between(dates_stika, highs_stika, lows_stika, facecolor='blue', alpha=0.1)

#ax.plot(dates, lows, c='blue')
#ax.plot(dates, rains, c='yellow')
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily high and low temporature and rain, 2018\nDeath Valley, CA", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()
