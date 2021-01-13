from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/nilvarshney/Google Drive/Machine Learning/PythonML/Datasets/foods.csv")
print(df.head())

#data = df.groupby(['Item']).['Spend'].sum()
#print(data.head(3))


def Histogram2dContour():


    x = np.random.randn(2000)
    y = np.random.randn(2000)
    plot([go.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap')),
           go.Scatter(x=x, y=y, mode='markers', marker=dict(color='white', size=3, opacity=0.3))], show_link=False,
          auto_open=False, filename='test_plot.html')


def BarPlot(df):
    plot([go.Bar(x = df['Frequency'], y=df['Spend'])],show_link=False,
      auto_open=False, filename='test_plot.html',)


BarPlot(df)
go.Bar(ti)