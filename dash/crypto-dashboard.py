from turtle import width
import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                dcc.Graph(
                    id='figure1',
                    figure={
                        'data': [
                            go.Indicator(mode='number', value=123)
                        ],
                        'layout': go.Layout(title='Portfolio Value (USDT)')
                    }
                ),
            ],
            style={
                'width': '30%',
                'display': 'inline-block',
            },
        ),
    ],
)


if __name__ == '__main__':
    app.run_server(debug=True)
