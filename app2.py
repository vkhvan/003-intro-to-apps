
######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

# define some variables
vacation = ['Couch','Beach','Mountain']
volume = [4500,1360,543]

def make_that_cool_piechart(vacation, volume):

# create the data trace
  trace = go.Pie(labels=vacation, 
               values=volume
              )

# combine into a figure
  vac_fig = go.Figure([trace])
  vac_fig.update_traces(textinfo='value')
  return vac_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_piechart(vacation, volume)
    fig.write_html('docs/piechart.html')
    print('We successfully updated the piechart!')
