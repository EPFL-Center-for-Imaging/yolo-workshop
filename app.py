import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

from flask import Flask, Response
import cv2
import skimage.filters
from skimage.exposure import rescale_intensity

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(4)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()

        frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_processed = skimage.filters.sobel(frame)
        frame_processed = rescale_intensity(frame_processed, out_range=(0, 255))

        ret, jpeg = cv2.imencode('.jpg', frame_processed)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

server = Flask(__name__)
app = dash.Dash(__name__, server=server, title='Image processing demo', 
                external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.CYBORG],
                meta_tags=[{'name': 'viewport', 
                            'content': 'width=device.width, initial_scale=1.0'}])

@server.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def serve_layout():
    layout = html.Div([
        html.Img(src="/video_feed", id='videofeed')
    ], id='main')
    return layout

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)