#%% Read csv using pandas
import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\Chen\OneDrive\GA\Dash_Avocado\avocado.csv")
data['Date'] = pd.to_datetime(data['Date'],format="%Y-%m-%d")
data.sort_values('Date',inplace=True)

# %% Graphing in Jupyter
import matplotlib.pyplot as plt
import plotly.express as px

i_location = data['region']=='California'
i_type = data['type'] == 'organic'

#pandas plotting (simpliest, fastest, but lacks customization)
data[i_location&i_type].plot(x='Date',y='AveragePrice',kind='line')

#matlibplot
df_plt = data[i_location&i_type]
fig,ax = plt.subplots(figsize=(10,5))
ax.plot(df_plt['Date'],df_plt['AveragePrice'])

#plotly express
plotly_fig = px.line(data_frame=df_plt,x='Date',y='AveragePrice')
#plotly_fig.show()


# %% API website
import dash
from dash import dcc, html,Input,Output

#server and connection
app = dash.Dash(__name__)

#dropdown
opt_dict = [{"label": region, "value": region} 
            for region in np.sort(data.region.unique())]

region_filter = dcc.Dropdown(id='region-filter',
                            options=opt_dict)
#figure
html_fig = dcc.Graph(id="price-chart")

#HTML client browser
html_page = html.Div([
    html.H1(children='Hello world',id='text_greet'),
    region_filter,
    dcc.Graph(id="price-chart")
])
app.layout = html_page

#defining the post behavior -> what to do when user select the dropdown item...
@app.callback(
    Output(component_id="price-chart",component_property="figure"),
    [Input(component_id="region-filter",component_property='value')])
def update_charts(region):
    i_location = data['region']==region
    i_type = data['type'] == 'organic'

    #plotly express
    df_plt = data[i_location&i_type]
    
    plotly_fig = px.line(data_frame=df_plt,x='Date',y='AveragePrice')
    return plotly_fig

#open the whole thing up to the world
app.run_server()
# %%
