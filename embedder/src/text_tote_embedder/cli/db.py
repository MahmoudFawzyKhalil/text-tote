import os
import sqlite3

import sqlite_vss

from text_tote_embedder.cli import dbmigrator
from text_tote_embedder.configuration import config


def create_db() -> None:
    """
    Create the database if it doesn't exist.
    """
    if os.path.exists(config.db_path):
        return

    uri = f"file:{config.db_path}?mode=rwc"
    conn = sqlite3.connect(uri, uri=True)
    _load_extensions(conn)


def migrate_db() -> None:
    """
    Migrate the database objects to the latest version. This will create the database if it doesn't exist.
    """
    create_db()
    db_connection = _create_connection()
    dbmigrator.migrate_db(db_connection)


def _create_connection() -> sqlite3.Connection:
    uri = f"file:{config.db_path}?mode=rw"
    db_connection = sqlite3.connect(uri, uri=True)
    _load_extensions(db_connection)
    return db_connection


def _load_extensions(db_connection: sqlite3.Connection) -> None:
    db_connection.enable_load_extension(True)
    sqlite_vss.load(db_connection)
