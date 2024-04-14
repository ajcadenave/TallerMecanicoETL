import sqlalchemy as db

def connect_taller_db():
    engine = db.create_engine("mysql://root:root@127.0.0.1:3310/taller_db")
    conn = engine.connect()

    return conn

def connect_taller_dw():
    engine = db.create_engine("mysql://root:root@127.0.0.1:3310/taller_dw")
    conn = engine.connect()

    return conn

