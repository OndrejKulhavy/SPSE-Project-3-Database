from abc import ABC, abstractmethod

from src.data.db_manager import DatabaseManager


class BaseRepository(ABC):
    def __init__(self, db: DatabaseManager):
        self.db = db

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
