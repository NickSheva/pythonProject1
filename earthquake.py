import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors
for key in colors.PLOTLY_SCALES.keys():
    print(key)


filename = 'data/eq.json'
with open(filename) as f:
    all_earth_quake = json.load(f)
title = all_earth_quake['metadata']['title']
dicts_eq = all_earth_quake["features"]
print(len(dicts_eq))

mags, lons, lats, hover_text = [], [], [], []
for eq in dicts_eq:
    mags.append(eq["properties"]['mag'])
    lons.append(eq["geometry"]['coordinates'][0])
    lats.append(eq["geometry"]['coordinates'][1])
    hover_text.append(eq["properties"]['title'])



data = [{'type': 'scattergeo', 'lon':lons, 'lat':lats, 'text': hover_text,
        'marker': {'size' :[5 * mag for mag in mags],
                   'color': mags,
                   'colorscale': 'Viridis',
                   'reversescale': True,
                   'colorbar': {'title': 'Magnitude'}}}]
my_layout = Layout(title=title)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, 'eq_map.html')