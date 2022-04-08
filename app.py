from dash import Dash, html, dcc
import pandas as pd
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

layout = dict(title='Current price of BTC',
              plot_bgcolor=colors['background'],
              paper_bgcolor=colors['background'],
              font_color=colors['text'],
              showlegend=False,
              autosize=False,
              width=1349,
              height=800,
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

df2 = pd.read_csv('New data2', sep=',')
trade_close2 = go.Scatter(x=list(df2.Date),
                          y=list(df2.Close),
                          name='Close',
                          line=dict(color='#b80404'))

data2 = [trade_close2]

layout2 = dict(title='Predicted price of BTC',
               plot_bgcolor=colors['background'],
               paper_bgcolor=colors['background'],
               font_color=colors['text'],
               showlegend=False,
               autosize=False,
               width=1349,
               height=800,
               xaxis=dict(
                   rangeselector=dict(
                       buttons=list([
                           dict(count=10,
                                label="10-kun",
                                step="day",
                                stepmode="backward"),
                           dict(count=20,
                                label="20-kun",
                                step="day",
                                stepmode="backward"),
                           dict(count=30,
                                label="30-kun",
                                step="day",
                                stepmode="backward"),
                           dict(count=2,
                                label="2-Oy",
                                step="month",
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

fig2 = dict(data=data2, layout=layout2)

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
                  dcc.Dropdown(['Predicted Price', 'History Price'], 'History Price', id='demo-dropdown'),
              )
              ], className="banner"),

    html.Div([
        dcc.Graph(
            id="graph_close",
            figure=fig,
            config={
                'staticPlot': False,
                'scrollZoom': False,
                'showTips': False,
                'doubleClick': 'reset'
            }
        )
    ], className="six columns"),

    html.Div([
        dcc.Graph(
            id="graph_forecast",
            figure=fig2,
            config={
                'staticPlot': False,
                'scrollZoom': False,
                'showTips': False,
                'doubleClick': 'reset'
            }
        )
    ], className="six columns"),

])

# @app.callback(
#     Output('graph_close', 'figure'),
#     [Input('demo-dropdown', 'value')])
# def update_output(value):
#     if value == "History Price":
#
#     elif value == "Predicted Price":
#         return f'salom {value}'


# app.css.append_css({
#     "external_url":'http://"'
# })


if __name__ == "__main__":
    app.run_server(debug=True)
