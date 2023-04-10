from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker


def get_inspect_database_uri():
    username = "mev"
    password = "inspector"
    host = "localhost"
    db_name = "arb_inspect"
    return f"postgresql+psycopg2://{username}:{password}@{host}/{db_name}"


def get_engine(uri: str):
    return create_engine(
        uri,
        use_insertmanyvalues=True,
        insertmanyvalues_page_size=10000,
    )


def _get_sessionmaker(uri: str):
    return sessionmaker(bind=get_engine(uri))


def get_inspect_sessionmaker():
    uri = get_inspect_database_uri()
    return _get_sessionmaker(uri)


def get_inspect_session() -> orm.Session:
    session = get_inspect_sessionmaker()
    return session()
