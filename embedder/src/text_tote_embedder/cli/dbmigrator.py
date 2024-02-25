import os
import re
import sqlite3
from os import path


def migrate_db(db_connection: sqlite3.Connection):
    cursor = db_connection.cursor()

    try:
        script_directory = path.dirname(path.abspath(__file__))
        migrations_directory = path.join(script_directory, 'migrations')

        sql_scripts = sorted(os.listdir(migrations_directory))

        create_schema_version_table_if_not_exist(cursor)

        # Fetch the current schema version
        current_version = get_current_schema_version(cursor)
        print(f"Current Schema Version: {current_version}")

        for sql_script in sql_scripts:
            if sql_script.endswith('.sql'):
                file_path = path.join(migrations_directory, sql_script)

                version = extract_version(sql_script)
                if version > current_version:
                    execute_sql_file(cursor, file_path)
                    update_schema_version(cursor, version)
                    print(f"Schema version updated to: {version}")

        db_connection.commit()
        print("Database migrated successfully.")

    except Exception as e:
        print(f"Error executing SQL scripts: {e}")

    finally:
        db_connection.close()


def create_schema_version_table_if_not_exist(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS schema_version (version integer PRIMARY KEY)")
    cursor.execute("SELECT * FROM schema_version")
    single_row_already_exists = cursor.fetchone() is not None
    if single_row_already_exists:
        return
    else:
        cursor.execute("INSERT INTO schema_version (version) VALUES (0)")


def extract_version(file_name: str) -> int:
    match = re.match(r'V(\d+)', file_name)
    if match:
        return int(match.group(1))
    else:
        raise Exception(f"Invalid file name: {file_name}")


def execute_sql_file(cursor, file_path: str):
    with open(file_path, 'r') as sql_file:
        print(f"Executing SQL script: {file_path}")
        sql_script = sql_file.read()
        cursor.executescript(sql_script)


def get_current_schema_version(cursor):
    # Fetch the current schema version from the database or return a default value if the table is not present
    cursor.execute("SELECT version FROM schema_version")
    result = cursor.fetchone()
    return result[0] if result else 0


def update_schema_version(cursor, version):
    # Update the schema_version table with the new version
    cursor.execute("UPDATE schema_version SET version = ?", (version,))
