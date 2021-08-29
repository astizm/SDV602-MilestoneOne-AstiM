import pandas as pd
import plotly.express as px


mzz = pd.read_csv('NZ_MZZ_CAPTURE_2000-2019.csv')
mzz.head()


fig = px.line(mzz, y = 'VALUE', x = 'PERIOD')

fig.show()


wag = pd.read_csv('CL_FL_WATERAREA_GROUPS.csv')
cgo = pd.read_csv('CL_FL_COUNTRYGROUPS_OCEANIA.csv')
cgo.head()
wag.head()
