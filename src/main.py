import os
import io
import sys
import base64
import subprocess
import sqlite3

import folium
from folium.plugins import (
    MarkerCluster,
    MiniMap,
)
import requests
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from PySide6.QtGui import (
    QShortcut,
)

from design import (
    Ui_MainWindow,
)
from auth import (
    AuthWindow,
)


class Headesk(QMainWindow):
    def __init__(self):
        super(Headesk, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.path = os.path.abspath('./')

        self.internet = self.is_internet()

        self.conn = sqlite3.connect(
            'headesk.sqlite'
        )
        self.mow_latlon = self.conn.execute(
            """
            SELECT lat, lon
            FROM cities
            WHERE  name='Москва'
            """
        ).fetchone()
        self.kzn_latlon = self.conn.execute(
            """
            SELECT lat, lon
            FROM cities
            WHERE  name='Казань'
            """
        ).fetchone()
        self.ngk_latlon = self.conn.execute(
            """
            SELECT lat, lon
            FROM cities
            WHERE  name='Ногинск'
            """
        ).fetchone()

        self.ui.btn_app_bs.clicked.connect( # type: ignore
            self.app_bs
        )
        self.ui.btn_app_ec.clicked.connect( # type: ignore
            self.app_ec
        )
        self.ui.btn_app_chem.clicked.connect( # type: ignore
            self.app_chem
        )
        self.ui.btn_app_dam.clicked.connect( # type: ignore
            self.app_dam
        )
        self.ui.btn_app_emer.clicked.connect( # type: ignore
            self.app_emer
        )
        self.ui.btn_app_ind.clicked.connect( # type: ignore
            self.app_ind
        )
        self.ui.btn_app_ter.clicked.connect( # type: ignore
            self.app_ter
        )
        self.ui.btn_app_tmp.clicked.connect( # type: ignore
            self.app_tmp
        )
        self.ui.btn_app_toxi.clicked.connect( # type: ignore
            self.app_toxi
        )

        self.shortcut_f11 = QShortcut(
            'F11', self
        )
        self.shortcut_f11.activated.connect( # type: ignore
            self.full_screen,
        )

        # self.start_server()

        self.init_webview()
    
    def full_screen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
    
    def is_internet(self):
        try:
            status = requests.get(
                'https://example.com/',
                timeout=1
            ).status_code
            return True
        except:
            return False
    
    def init_webview(self):        
        self.map = folium.Map(
            location=[
                *self.kzn_latlon,
            ],
            zoom_start=12,
            tiles='None',
            attr=' ',
        )
        self.map.add_child(
            folium.LatLngPopup()
        )

        self.set_minimap()
        
        self.cluster_stuct = MarkerCluster(
            name='Инфраструктура',
        ).add_to(self.map)
        self.group_uni = folium.FeatureGroup(
            name='ВУЗы МЧС России'
        ).add_to(self.map)
        self.group_rc = folium.FeatureGroup(
            name='Спасцентры'
        ).add_to(self.map)
        self.cluster_etasks = MarkerCluster(
            name='Происшествия'
        ).add_to(self.map)

        if self.internet == True:
            folium.TileLayer(
                'OpenStreetMap',
                name='OSM Open Data',
            ).add_to(self.map)
            folium.TileLayer(
                tiles="http://mt1.google.com/vt/lyrs=m&h1=p1Z&x={x}&y={y}&z={z}",
                name="GMap Standart",
                attr="Google Map",
            ).add_to(self.map)
            folium.TileLayer(
                tiles="http://mt1.google.com/vt/lyrs=s&h1=p1Z&x={x}&y={y}&z={z}",
                name="GMap Satellite",
                attr="Google Map",
            ).add_to(self.map)
            folium.TileLayer(
                tiles="http://mt1.google.com/vt/lyrs=y&h1=p1Z&x={x}&y={y}&z={z}",
                name="GMap Hybrid",
                attr="Google Map",
            ).add_to(self.map)
        elif self.internet == False:
            folium.TileLayer(
                tiles='http://127.0.0.1:443/osmmow/?z={z}&x={x}&y={y}.png',
                name='Москва',
                attr='Mow',
                control=False
            ).add_to(self.map)
            folium.TileLayer(
                tiles='http://127.0.0.1:443/osmkzn/?z={z}&x={x}&y={y}.png',
                name='Казань',
                attr='Kzn',
                control=False
            ).add_to(self.map)
        else:
            return None

        self.point_objects()
        self.point_etasks()

        self.for_rc()
        self.for_uni()

        folium.LayerControl(
            'topright', collapsed=True
        ).add_to(self.map)

        self.data = io.BytesIO()
        self.map.save(
            self.data, close_file=False
        )
        self.ui.webview.setHtml(
            self.data.getvalue().decode()
        )
        self.ui.webview.show()
        return None

    def app_bs(self):
        subprocess.run(
            '',
            executable='./apps/passport.exe'
        )
        return None
    
    def app_ec(self):
        subprocess.run(
            '',
            executable='./apps/explosion.exe'
        )
        return None
    
    def app_chem(self):
        subprocess.run(
            '',
            executable='./apps/chem.exe'
        )
        return None
    
    def app_dam(self):
        subprocess.run(
            '',
            executable='./apps/dam.exe'
        )
        return None
    
    def app_emer(self):
        subprocess.run(
            '',
            executable='./apps/emer.exe'
        )
        return None
    
    def app_ind(self):
        subprocess.run(
            '',
            executable='./apps/ind.exe'
        )
        return None
    
    def app_ter(self):
        subprocess.run(
            '',
            executable='./apps/ter/MapTest.exe'
        )
        return None
    
    def start_server(self):
        subprocess.run(
            '',
            executable='./seadesk.exe'
        )
    
    def app_tmp(self):
        subprocess.run(
            '',
            executable='./apps/tmp.exe'
        )
        return None
    
    def app_toxi(self):
        subprocess.run(
            '',
            executable='./apps/toxi/Toxi.exe'
        )
        return None
    
    def for_rc(self):
        content = self.conn.execute(
            """
            SELECT
                name,
                lat,
                lon
            FROM rescue_centers
            """
        ).fetchall()
        for item in content:
            icon = folium.CustomIcon(
                (
                    f'http://127.0.0.1:443/rc.ico'
                ),
                icon_size=(
                    40,
                    40,
                )
            )
            folium.Marker(
                location=[
                    item[1],
                    item[2],
                ],
                tooltip=item[0],
                icon=icon,
            ).add_to(self.group_rc)
        return None
    
    def for_uni(self):
        content = self.conn.execute(
            """
            SELECT
                name,
                lat,
                lon,
                icon
            FROM universities
            """
        ).fetchall()
        for item in content:
            icon = folium.CustomIcon(
                (
                    f'http://127.0.0.1:443/'
                    f'uni/?icon={item[3]}'
                ),
                icon_size=(
                    40,
                    40,
                )
            )
            folium.Marker(
                location=[
                    item[1],
                    item[2],
                ],
                tooltip=item[0],
                icon=icon,
            ).add_to(self.group_uni)
        return None

    def point_objects(self):
        content = self.conn.execute(
            """
            SELECT
                name,
                lat,
                lon,
                category_id
            FROM objects
            """
        ).fetchall()
        for item in content:
            icon = folium.CustomIcon(
                (
                    f'http://127.0.0.1:443/'
                    f'categories/?i={item[3]}'
                ),
                icon_size=(
                    50,
                    60,
                )
            )
            folium.Marker(
                location=[
                    item[1],
                    item[2],
                ],
                tooltip=item[0],
                icon=icon,
            ).add_to(self.cluster_stuct)
        return None
    
    def point_etasks(self):
        content = self.conn.execute(
            """
            SELECT
                name,
                lat,
                lon,
                type,
                time,
                ext
            FROM emergency_tasks
            """
        ).fetchall()
        template = \
            """
            Время возникновения: {0}<hr>
            Подробности: {1}
            """
        for item in content:
            icon = folium.CustomIcon(
                (
                    f'http://127.0.0.1:443/'
                    f'etypes/?i={item[3]}'
                ),
                icon_size=(
                    50,
                    60,
                )
            )
            iframe = folium.IFrame(
                template.format(
                    item[4],
                    item[5],
                ),
                width=300,
                height=150,
            )
            popup = folium.Popup(
                iframe,
            )
            folium.Marker(
                location=[
                    item[1],
                    item[2],
                ],
                tooltip=item[0],
                icon=icon,
                popup=popup,
            ).add_to(self.cluster_etasks)
        return None
    
    def set_minimap(self):
        if self.internet == True:
            self.map.add_child(
                MiniMap(
                    width=200,
                    height=200,
                )
            )
        else:
            pass
        return None


if __name__ == "__main__":
    app = QApplication(
        sys.argv
    )

    auth_window = AuthWindow()
    auth_window.exec()

    if auth_window.is_wrong:
        sys.exit()
    else:
        pass

    window = Headesk()
    window.show()
    
    sys.exit(
        app.exec()
    )