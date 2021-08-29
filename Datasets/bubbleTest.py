import pandas as pd
import plotly.express as px
mzz = pd.read_csv('GLOBAL_PRODUCTION_QUANTITY_OCEANIA.csv')
mzz.head()

fig = px.scatter(mzz.query("PERIOD==2012"), x="VALUE", y = ("PRODUCTION_SOURCE_DET.CODE"),
                 size="VALUE", color="COUNTRY.UN_CODE",
                 hover_name="VALUE", size_max=60)
fig.show()
