######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
distance_values=[3.0, 5.5, 7.0, 5.7, 8.5, 10.0, 3.5]
effort_values=[2.4, 4.1, 6.2, 4.3, 7.3, 9.0, 2.0]
color1='darkblue'
color2='orange'
mytitle='Running log'

label1='Distance'
label2='Effort'

########### Set up the chart

def make_that_cool_barchart(beers, ibu_values, abv_values, color1, color2, mytitle):
    distance = go.Bar(
        x=days,
        y=distance_values,
        name=label1,
        marker={'color':color1}
    )
    effort = go.Bar(
        x=days,
        y=effort_values,
        name=label2,
        marker={'color':color2}
    )

    running_data = [distance, effort]
    running_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    running_fig = go.Figure(data=running_data, layout=running_layout)
    return running_fig

######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(days, distance_values, effort_values, color1, color2, mytitle)
    fig.write_html('docs/barchart.html')
    print('We successfully updated the barchart!')
