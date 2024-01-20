import os
import sqlite3

import sqlite_vss

from . import dbmigrator
from .configuration import appconfig


def create_db():
    if os.path.exists(appconfig.db_path):
        return

    uri = f"file:{appconfig.db_path}?mode=rwc"
    conn = sqlite3.connect(uri, uri=True)
    load_extensions(conn)


def migrate_db():
    db_connection = create_connection()
    dbmigrator.execute_migrations(db_connection)


def create_connection() -> sqlite3.Connection:
    uri = f"file:{appconfig.db_path}?mode=rw"
    conn = sqlite3.connect(uri, uri=True)
    load_extensions(conn)
    return conn


def load_extensions(conn: sqlite3.Connection):
    conn.enable_load_extension(True)
    sqlite_vss.load(conn)
