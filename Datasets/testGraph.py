import pandas as pd
import plotly.express as px


mzz = pd.read_csv('NZ_MZZ_CAPTURE_2000-2019.csv')
mzz.head()


fig = px.line(mzz, y = 'VALUE', x = 'PERIOD')

fig.show()


