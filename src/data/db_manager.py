import mysql.connector

from src.logic.settings.config_data import Settings


class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        settings = Settings.get_database_settings()
        self.connection = mysql.connector.connect(
            host=settings.host,
            user=settings.user,
            password=settings.password,
            database=settings.schema
        )

    def disconnect(self):
        self.connection.close()

    def execute(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        cursor.close()

    def fetch(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetch_one(self, query, params=None) -> object:
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result
