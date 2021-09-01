import pandas as pd
import plotly.express as px
mzz = pd.read_csv('newTest.csv')
mzz.head()

fig = px.scatter(mzz, x="VALUE", y = ("PRODUCTION_SOURCE_DET.CODE"),
                 size="VALUE", color="COUNTRY.UN_CODE",
                 hover_name="VALUE", size_max=60)
fig.show()
