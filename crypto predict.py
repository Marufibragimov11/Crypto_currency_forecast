from dash import Dash, html, dcc
import pandas as pd
from datetime import date
import plotly.graph_objs as go

colors = {
    'background': '#111111',
    'text': '#b80404'
}

df = pd.read_csv('History_data3', sep=',')
trade_close = go.Scatter(x=list(df.Date),
                         y=list(df.Close),
                         name='Close',
                         line=dict(color='#b80404'))

data = [trade_close]

layout = dict(title='Price of BTC',
              plot_bgcolor=colors['background'],
              paper_bgcolor=colors['background'],
              font_color=colors['text'],
              showlegend=False,
              xaxis=dict(
                  rangeselector=dict(
                      buttons=list([
                          dict(count=15,
                               label="15-kun",
                               step="day",
                               stepmode="backward"),
                          dict(count=1,
                               label="1-Oy",
                               step="month",
                               stepmode="backward"),
                          dict(count=6,
                               label="6-Oy",
                               step="month",
                               stepmode="backward"),
                          dict(count=1,
                               label="1-Yil",
                               step="year",
                               stepmode="backward"),
                          dict(label="Xammasi",
                               step="all")
                      ])
                  ),
                  rangeslider=dict(
                      visible=True
                  ),
                  type="date"
              ))

fig = dict(data=data, layout=layout)

app = Dash()

app.layout = html.Div([
    html.Div([html.H1(children="Crypto Currency forecast",
                      style={
                          'textAlign': 'center',
                          'color': '#b80404',
                      }
                      ),
              html.Div("Crypto is  new money from 2022",
                       style={
                           'textAlign': 'center',
                           'color': '#b80404',
                       }
                       ),
              html.Img(src="assets/stock-icon.png"),
              html.Div(
                  dcc.DatePickerSingle(
                      date=date(2020, 1, 1),
                      display_format='Y-M-D')
              )
              ], className="banner"),

    html.Div(
        dcc.Graph(id="Stock Chart",
                  figure=fig)
    )
])

# app.css.append_css({
#     "external_url":'http://"'
# })

if __name__ == "__main__":
    app.run_server(debug=True)
