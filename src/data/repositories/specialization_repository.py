from src.data.models.specialization import Specialization
from src.data.repositories.base_repository import BaseRepository


class SpecializationRepo(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

    def get_all(self):
        query = "SELECT * FROM specialization"
        result = self.db.fetch(query)
        return [Specialization(*row) for row in result]

    def get_by_id(self, id: int):
        query = "SELECT * FROM specialization WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Specialization(*result)

    def add(self, specialization: Specialization):
        query = "INSERT INTO specialization (name) VALUES (%s)"
        params = (specialization.name,)
        self.db.execute(query, params)

    def update(self, entity):
        if entity.id is None:
            self.add(entity)
            return

        query = "UPDATE specialization SET name = %s WHERE id = %s"
        params = (entity.name, entity.id)
        self.db.execute(query, params)

    def delete(self, id: int):
        query = "DELETE FROM specialization WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
