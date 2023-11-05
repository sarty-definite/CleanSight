# for plotly
from taipy.gui import Html, Markdown
import requests
import json
import pandas as pd
import plotly.express as px
import webbrowser


def showfig():
    url = "https://ap-south-1.aws.data.mongodb-api.com/app/triggers-lvqxp/endpoint/TrashTrack"
# url = "https://data.mongodb-api.com/app/triggers-oiqrx/endpoint/trashLocation"
    response = requests.request("GET", url=url)

    a = json.loads(response.text)
    df = pd.DataFrame.from_records(a)
    fig = px.density_mapbox(df, lat = 'lat', lon = 'long', 
                        radius = 10,
                        center = dict(lat =28.718411, lon = 77.063736),
                        zoom = 10,
                        mapbox_style = 'stamen-terrain')
    fig.show()
def button_pressed(state):
    url="https://negativediscretetraining.sarthakgoelart.repl.co/"
    webbrowser.open(url, new=2)

map_md = Html('''
<html lang="en">
<head>
    <meta charset="utf-8"></meta>
    <meta name="viewport" content="width=device-width, initial-scale=1"></meta>
    <title></title>
    <style>
    </style>
</head>
<body>
    <div class="container text-center">
    <h1>GeoLocation Heatmap</h1>
    <taipy:button style on_action="showfig">Show Heatmap</taipy:button>
    <taipy:button  on_action="button_pressed" >Deploy the Scan</taipy:button>
    </div>
</body>
</html>
''')
# map_md = Html('''
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="utf-8"></meta>
#     <meta name="viewport" content="width=device-width, initial-scale=1"></meta>
#     <title></title>
#     <style>
#     </style>
# </head>
# <body>
#     <div class="container text-center">
#     <h1>GeoLocation Heatmap</h1>
#     {fig.show()}

#     <taipy:button  on_action="submit_login">Deploy the Scan</taipy:button>
#     </div>
#     <div class="position-fixed bottom-0 end-0 p-3 ">
#     </div>
#     <div></div>
# </body>
# </html>
# ''')

