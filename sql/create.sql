-- Таблицы с вспомогательной инфой
DROP TABLE IF EXISTS modules;
DROP TABLE IF EXISTS marks;
DROP TABLE IF EXISTS users;

-- Таблицы с основными данными
DROP TABLE IF EXISTS objects;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS emergency_types;
DROP TABLE IF EXISTS emergency_tasks;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS universities;
DROP TABLE IF EXISTS rescue_centers;


-- Таблица категорий объектов инфраструктуры
CREATE TABLE categories(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL
);

-- Таблица объектов инфраструктуры
CREATE TABLE objects(
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id     INTEGER NOT NULL,
    name            TEXT    NOT NULL,
    organization    TEXT,
    subordination   TEXT,    
    readiness       TEXT,
    staff           TEXT,
    address         TEXT,
    phone           TEXT,
    lat             FLOAT,
    lon             FLOAT
);

-- Таблица названий и расположения расчетных программ
CREATE TABLE modules(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    file    TEXT    NOT NULL
);

-- Таблица названий и расположения изображений меток
CREATE TABLE marks(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    file    TEXT    NOT NULL
);

-- Таблица типов чрезвычайных происществий
CREATE TABLE emergency_types(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    type    TEXT    NOT NULL,
    name    TEXT    NOT NULL
);

-- Таблица произошедших чрезвычайных происшествий
CREATE TABLE emergency_tasks(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    type    INTEGER NOT NULL,
    name    TEXT    NOT NULL,
    time    FLOAT   NOT NULL,
    lat     FLOAT   NOT NULL,
    lon     FLOAT   NOT NULL,
    ext     TEXT
);

-- Таблица пользователей программы
CREATE TABLE users(
    id  INTEGER PRIMARY KEY AUTOINCREMENT,
    l   TEXT    NOT NULL,
    p   TEXT    NOT NULL
);

-- Таблица городов России
CREATE TABLE cities(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    lat     FLOAT   NOT NULL,
    lon     FLOAT   NOT NULL
);

-- Таблица ВУЗов МЧС России
CREATE TABLE universities(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    lat     FLOAT   NOT NULL,
    lon     FLOAT   NOT NULL,
    address TEXT,
    phone   TEXT,
    email   TEXT,
    icon    TEXT
);

-- Таблица спасательных центров
CREATE TABLE rescue_centers(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT    NOT NULL,
    lat     FLOAT   NOT NULL,
    lon     FLOAT   NOT NULL,
    address TEXT,
    phone   TEXT,
    email   TEXT
);
