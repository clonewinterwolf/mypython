import csv
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

lons, lats, brights = [], [], []

filename = "data/world_fires_1_day.csv" 
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    for row in reader:
        try:       
            lat = float(row[0])
            lon = float(row[1])
            bright = float(row[2])
        except ValueError:
            print(f"wrong data excpet")
        else:
            lons.append(lon)
            lats.append(lat)
            brights.append(bright)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bright/80 for bright in brights],
        'color': brights,
        'colorscale': 'Bluered',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    }
}]
my_layout = Layout(title="World Fire in one day")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fire.html')