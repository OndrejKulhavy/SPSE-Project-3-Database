import json

from src.data.db_manager import DatabaseManager


class DbImporter:
    def __init__(self, db_connection: DatabaseManager):
        self.db = db_connection

    def import_json_data(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            NotImplementedError('Implement this method')
