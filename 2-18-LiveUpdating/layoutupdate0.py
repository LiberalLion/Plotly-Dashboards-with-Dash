#######
# This page doesn't update.
######
import dash
import dash_html_components as html

app = dash.Dash()

crash_free = 0 + 1
app.layout = html.H1(f'Crash free for {crash_free} refreshes')

if __name__ == '__main__':
    app.run_server()
