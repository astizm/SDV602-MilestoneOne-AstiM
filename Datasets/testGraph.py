import pandas as pd
import plotly.express as px


mzz = pd.read_csv('newTest.csv')
mzz.head()


fig = px.line(mzz.query('PERIOD == 2010'), x = 'VALUE', y = 'STATUS')

fig.show()


