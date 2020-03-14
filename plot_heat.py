import plotly.express as px
import numpy as np
import pandas as pd
# in order to have a single root node
df = pd.read_csv('sample_species_strain_genus_count.csv')
df["ALL"] = "ALL"
fig = px.treemap(df, path=['ALL', 'sample_species', 'strain_genus'], values='count',
                 color='strain_genus_color',
                 color_discrete_map={'(?)': '#A0AFB2',
                                     'x50': '#ED8b94',
                                     'x55': '#FCC3B2',
                                     'x60': '#F5E9E2',
                                     'x65': '#5C638B',
                                     'x70': '#B5CDF5',
                                     'x75': '#5191E1',
                                     'x10': '#E5AB93',
                                     'x200': '#D79851',
                                     'x80': '#F1D6B1',
                                     'x85': '#C8E0EC',
                                     'x150': '#6AB6CF',
                                     'x140': '#87944E',
                                     'x145': '#4E2B1C',
                                     'x120': '#D0505D',
                                     'x135': '#E1929A',
                                     'x180': '#DDEAF6',
                                     'x185': '#2F5C85',
                                     'x165': '#6F9294',
                                     'x170': '#F7D98D',
                                     'x175': '#9E3E42'}
                 )
fig.show()
