from folium import (
    _default_js,
    _default_css,
)


def set_offline():
    """
    Change folium Map templating to look for required .js and .css locally.
    NOTE: These versions may change in time. You must manage/update them manually
    """

    # compare to _default_js[...] in folium.py
    # modified to look for required .js in ./offline/
    # change relative path to your offline files
    _default_js = [
         (
            "leaflet",
            'http://127.0.0.1:443/leaflet.js'),
         (
            "jquery",
            'http://127.0.0.1:443/jquery-1.12.4.min.js'),
        (
            "bootstrap",
            'http://127.0.0.1:443/bootstrap.bundle.min.js',
        ),
        (
            "awesome_markers",
            'http://127.0.0.1:443/leaflet.awesome-markers.js',
        ),
    ]

    # compare to _default_css[...] in folium.py
    # modified to look for required .css in ./offline/
    # change relative path to your offline files
    _default_css = [
        (
            "leaflet_css",
            'http://127.0.0.1:443/leaflet.css'
        ),
        (
            "bootstrap_css",
            'http://127.0.0.1:443/bootstrap_1.css',
        ),
        (
            "glyphicons_css",
            'http://127.0.0.1:443/bootstrap_2.css',
        ),
        (
            "awesome_markers_font_css",
            'http://127.0.0.1:443/all_min.css',
        ),
        (
            "awesome_markers_css",
            'http://127.0.0.1:443/leaflet.awesome-markers.css',
        ),
        (
            "awesome_rotate_css",
            'http://127.0.0.1:443/leaflet.awesome.rotate.min.css',
        ),
    ]