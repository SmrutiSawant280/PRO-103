import pandas as p
import plotly.express as px
df = p.read_csv("C:/Users/DELL/Desktop/PRO97/103.csv")
fig = px.scatter(df,x = "cases",y = "date",color = "country")
fig.show()