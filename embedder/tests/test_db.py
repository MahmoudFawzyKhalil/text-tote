import os
import sqlite3

import approvaltests

from text_tote_embedder.cli import db
from text_tote_embedder.configuration import config


def test_migrate_db():
    # Arrange
    delete_db()
    db.create_db()

    # Act
    db.migrate_db()

    # Assert
    metadata = get_table_metadata(db.create_connection())
    approvaltests.verify_as_json(metadata)


def delete_db() -> None:
    try:
        os.remove(config.db_path)
    except FileNotFoundError:
        pass


def get_table_metadata(connection: sqlite3.Connection):
    cursor = connection.cursor()

    # Get a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Dictionary to store table metadata
    table_metadata = {}

    # Loop through each table and retrieve metadata
    for table_name, in tables:
        table_metadata[table_name] = {}

        # Get table definition and metadata
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        # Store column names and definitions in the dictionary
        table_metadata[table_name]['columns'] = []
        for column in columns:
            column_name = column[1]
            column_type = column[2]
            is_primary_key = bool(column[5])
            table_metadata[table_name]['columns'].append({
                'name': column_name,
                'type': column_type,
                'is_primary_key': is_primary_key
            })

    return table_metadata
