import os

import approvaltests

from src.text_tote_embedder import db
from src.text_tote_embedder.configuration import appconfig


def test_migrate_db():
    try:
        # Arrange
        db.create_db()

        # Act
        db.migrate_db()

        # Assert
        db_connection = db.create_connection()
        metadata = get_table_metadata(db_connection)
        approvaltests.verify_as_json(metadata)
    finally:
        # Cleanup
        # os.remove(appconfig.db_path)
        pass


def get_table_metadata(connection):
    cursor = connection.cursor()

    # Get a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Dictionary to store table metadata
    table_metadata = {}

    # Loop through each table and retrieve metadata
    for table in tables:
        table_name = table[0]
        table_metadata[table_name] = {}

        # Get table definition and metadata
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        # Store column names and definitions in the dictionary
        table_metadata[table_name]['columns'] = []
        for column in columns:
            column_name = column[1]
            column_type = column[2]
            is_primary_key = column[5]
            table_metadata[table_name]['columns'].append({
                'name': column_name,
                'type': column_type,
                'is_primary_key': bool(is_primary_key)
            })

    return table_metadata
