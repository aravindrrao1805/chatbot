from requests import post
from dash import Dash, dcc, html, callback, State, Output, Input

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H3("Chatbot App"),
        dcc.Textarea(
            id = "input-textarea",
            value="",
            placeholder="Type your query here",
            style={'width': '90%', 'height': '100px'},
        ),
        html.Br(),
        html.Button("Submit", id = "input-submit", n_clicks=0),
        html.Div(id = "output-response")
    ]
)

@callback(
    [
        Output("input-textarea", "value"),
        Output("output-response", "children"),
        Input("input-submit", "n_clicks"),
        State("input-textarea", "value")
    ]
)

def update_output(n_clicks, value):
    if n_clicks > 0:
        result = post(url = "http://localhost:8000/",
                      json ={"question": value})

        if result.status_code == 200:
            response = result.json()["response"]
        else:
            response = f"Error {result.status_code}"

        textarea = ""
        message = html.Div([
            html.Div("Question: " + value),
            html.Br(),
            html.Div("Answer: " + response)]
        )
        return textarea, message
    else:
        return None, None

if __name__ == "__main__":
    app.run(port = 5000, debug = True)

