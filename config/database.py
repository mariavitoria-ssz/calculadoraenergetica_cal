

from peewee import SqliteDatabase

database = SqliteDatabase('database-v5.db')

def startup_db():
    from models.bandeira import BandeiraDB
    from models.dependencia import DependenciaDB
    from models.dispositivo import DispositivoDB
    from models.tipos_consumidor import TipoConsumidorDB
    from models.tipos_dspositivo import TipoDispositivoDB
    from models.unidade_consumidora import UnidadeConsumidoraDB

    database.connect()
    database.create_tables([
        UnidadeConsumidoraDB,
        BandeiraDB,
        DependenciaDB,
        DispositivoDB,
        TipoConsumidorDB,
        TipoDispositivoDB
    ])

def shutdown_db():
    database.close()
