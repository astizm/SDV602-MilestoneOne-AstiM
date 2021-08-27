import pandas as pd
import plotly.express as px

wag = pd.read_csv('CL_FL_WATERAREA_GROUPS.csv')
cgo = pd.read_csv('CL_FL_COUNTRYGROUPS_OCEANIA.csv')
mzz = pd.read_csv('NZ_MZZ_CAPTURE_2000-2019.csv')

mzz.head()
cgo.head()
wag.head()

fig = px.line(mzz, y = 'VALUE', x = 'PERIOD')

fig.show()
