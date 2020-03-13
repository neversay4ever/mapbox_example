import pandas as pd
import geojson
import json


def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
    geojson = {'type': 'FeatureCollection', 'features': []}
    for _, row in df.iterrows():
        feature = {'type': 'Feature',
                   'properties': {},
                   'geometry': {'type': 'Point',
                                'coordinates': []}}
        feature['geometry']['coordinates'] = [row[lon], row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson


data = pd.read_csv("./v2_sample_stat.csv")
cols = ['sample_species', 'pie_type', 'count']

geo_json = df_to_geojson(data, cols)
print(geo_json)
