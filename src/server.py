import os

import flask


app = flask.Flask(__name__)

app_path = os.path.abspath('./')
data_path = os.path.join(
    os.path.abspath('./'), 'data/osm'
)
mow_path = os.path.join(
    data_path, 'mow'
)
kzn_path = os.path.join(
    data_path, 'kzn'
)
script_path = os.path.join(
    os.path.abspath('./'), 'offline'
)

@app.route('/osmmow/')
def get_tilemow():
    x, y, z = (
        flask.request.args.get('x'),
        flask.request.args.get('y'),
        flask.request.args.get('z'),
    )
    fp = os.path.join(
        mow_path, f'{z}/{x}/{y}'
    )
    return flask.send_file(fp)


@app.route('/osmkzn/')
def get_tilekzn():
    x, y, z = (
        flask.request.args.get('x'),
        flask.request.args.get('y'),
        flask.request.args.get('z'),
    )
    fp = os.path.join(
        kzn_path, f'{z}/{x}/{y}'
    )
    return flask.send_file(fp)


@app.route('/categories/')
def get_categories():
    i = flask.request.args.get('i')
    fp = os.path.join(
        app_path, f'icon/categories/{i}.ico'
    )
    return flask.send_file(fp)


@app.route('/etypes/')
def get_etypes():
    i = flask.request.args.get('i')
    fp = os.path.join(
        app_path, f'icon/etypes/{i}.ico'
    )
    return flask.send_file(fp)


@app.route('/rc.ico')
def get_12():
    fp = os.path.join(
        app_path, 'icon/rc.ico'
    )
    return flask.send_file(fp)


@app.route('/uni/')
def get_13():
    fp_1 = flask.request.args.get('icon')
    fp_2 = os.path.join(
        app_path, str(fp_1)
    )
    return flask.send_file(fp_2)


@app.route('/pdf')
def get_pdf():
    fp_2 = os.path.join(
        app_path, 'docs/ГОСТ 19433-88.pdf'
    )
    return flask.send_file(fp_2)


@app.route('/jquery-1.12.4.min.js')
def get_1():
    fp = os.path.join(
        script_path, 'jquery-1.12.4.min.js'
    )
    return flask.send_file(fp)


@app.route('/leaflet.js')
def get_2():
    fp = os.path.join(
        script_path, 'leaflet.js'
    )
    return flask.send_file(fp)


@app.route('/bootstrap.bundle.min.js')
def get_3():
    fp = os.path.join(
        script_path, 'bootstrap.bundle.min.js'
    )
    return flask.send_file(fp)


@app.route('/leaflet.awesome-markers.js')
def get_4():
    fp = os.path.join(
        script_path, 'leaflet.awesome-markers.js'
    )
    return flask.send_file(fp)


@app.route('/leaflet.css')
def get_5():
    fp = os.path.join(
        script_path, 'leaflet.css'
    )
    return flask.send_file(fp)


@app.route('/bootstrap_1.css')
def get_6():
    fp = os.path.join(
        script_path, 'bootstrap_1.css'
    )
    return flask.send_file(fp)


@app.route('/bootstrap_2.css')
def get_7():
    fp = os.path.join(
        script_path, 'bootstrap_2.css'
    )
    return flask.send_file(fp)


@app.route('/all_min.css')
def get_8():
    fp = os.path.join(
        script_path, 'all_min.css'
    )
    return flask.send_file(fp)


@app.route('/leaflet.awesome-markers.css')
def get_9():
    fp = os.path.join(
        script_path, 'leaflet.awesome-markers.css'
    )
    return flask.send_file(fp)


@app.route('/leaflet.awesome.rotate.min.css')
def get_10():
    fp = os.path.join(
        script_path, 'leaflet.awesome.rotate.min.css'
    )
    return flask.send_file(fp)


@app.route('/leaflet.markercluster.js')
def get_21():
    fp = os.path.join(
        script_path, 'leaflet.markercluster.js'
    )
    return flask.send_file(fp)


@app.route('/MarkerCluster.css')
def get_22():
    fp = os.path.join(
        script_path, 'MarkerCluster.css'
    )
    return flask.send_file(fp)


@app.route('/MarkerCluster.Default.css')
def get_23():
    fp = os.path.join(
        script_path, 'MarkerCluster.Default.css'
    )
    return flask.send_file(fp)


@app.route('/Control.MiniMap.js')
def get_24():
    fp = os.path.join(
        script_path, 'Control.MiniMap.js'
    )
    return flask.send_file(fp)


@app.route('/Control.MiniMap.css')
def get_25():
    fp = os.path.join(
        script_path, 'Control.MiniMap.css'
    )
    return flask.send_file(fp)


# Для запроса вида: .../osm/mow/z/x/y.png
# @app.route('/<city>/<z>/<x>/<y>')
# def get_tile(city, z, x, y):
#     fp = os.path.join(
#         data_path, city, f'{z}/{x}/{y}'
#     )
#     return flask.send_file(fp)


if __name__ == "__main__":
    app.run(
        host='0.0.0.0', port=443,
    )