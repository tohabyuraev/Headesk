# Headesk (PySide2 -> PySide6)

## Стек

* **python** - интерпритируемый язык программирования. Выбран как наиболее гибкий для создания программ и обработки файлов различных форматов, а также как один из самых легких при старте в программировании. Не требует установки доп сред программирования. Имеет богатую стандартную библиотеку.

* **PySide6** - framework для GUI с широким функционалом

* **pyinstaller** - для сборки исполняемого файла сервера и приложения

* **SimplyIcon** - для создания icon файлов из файлов png

* **folium** - библиотека (наподобие обертки над leaflet.js) для создания интерактивных карт. Имеет встроенный функционал по подключению к серверам открытых карт, позволяет по ссылке определенного типа подключаться к собстенному серверу. Позволяет отображать несколько слоев карт

* **geocoder** - библиотека для обработки координат, названий местности

* **Flask** - фреймворк для создания локального tile-сервера 

## Источники

* fontawesome - изображения для маркеров инфраструктуры (больниц, полицейских участков, спасательных формирований)

## Разработка

1. Использование QtDesigner для создания design.ui - файла настройки виджетов, а также стиля приложения. Там же создается файла ресурсов.

2. Конвертация design.ui > design.py и files.qrc > files.py. Конвертация с помощью команд в командной строке:
   
   ```powershell
   pyside6-rcc src\files.qrc > src\files.py
   ```
   
   ```powershell
   pyside6-uic src\design.ui > src\design.py
   ```

3. Создание main.py для описания логики работы приложения.

4. Сборка приложения с помощью PyInstaller:
   
   ```powershell
   pyinstaller -w -F -n Headesk --icon="./icon/nic.ico" src/main.py
   ```
   
   Сборка локального сервера:
   
   ```powershell
   pyinstaller -w -F -n Seadesk --icon="./icon/nic.ico" src/server.py
   ```
   
   NOTE: при сборке сервера может быть ошибка при его запуске. Необходимо закоментировать строки 299, 300 в файле click/util.py.
   
   Добавить в сгенерированный файл `Headesk.spec` в раздел `EXE` поле:
   
   ```
   icon='./icon/user.ico',
   ```
   
   в раздел Analysis поле:
   
   ```
   datas=[
       ('icon', 'icon'),
       ('font', 'font'),
       ('img', 'img',)
   ],
   ```

   Сборка приложения в папку `build (1)` и `dist (1)`. Сборка сервера в папки `biuld` и `dist`. Название испольняемого файла приложения `Headesk`, сервера `seadesk`. 

Флаги при сборке приложения:

- -w - отсутсвие консоли при работе приложения

- -F - сборка в один исполняемый файл

Сборка приложения в папки build(1) и dist(1).