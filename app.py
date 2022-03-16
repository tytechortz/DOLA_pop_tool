from dash import Dash, html, dcc
import pandas as pd
from datetime import date



def get_layout():
    return html.Div(
        [
            html.Div([
                html.H4('DOLA Pop')
            ])
        ]
    )

app = dash.Dash(__name__)
app.layout = get_layout
app.config['suppress_callback_exceptions']=True


if __name__=="__main__":
    app.run_server(debug=True)