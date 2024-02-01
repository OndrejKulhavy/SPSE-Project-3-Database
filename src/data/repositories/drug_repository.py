from typing import override

from src.data.models.drug import Drug
from src.data.repositories.base_repository import BaseRepository


class DrugRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

    @override
    def get_all(self):
        query = "SELECT * FROM drug"
        result = self.db.fetch(query)
        return [Drug(*row) for row in result]

    @override
    def get_by_id(self, id: int):
        query = "SELECT * FROM drug WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Drug(*result)

    @override
    def add(self, drug: Drug):
        query = "INSERT INTO drug (name, price, active_substance, form, description, side_effects, storage_conditions) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (drug.name, drug.price, drug.active_substance, drug.form, drug.description,
                  drug.side_effects, drug.storage_conditions)
        self.db.execute(query, params)

    @override
    def update(self, drug: Drug):
        if drug.id is None:
            self.add(drug)

        query = "UPDATE drug SET name = %s, price = %s, active_substance = %s, form = %s, description = %s, " \
                "side_effects = %s, storage_conditions = %s WHERE id = %s"
        params = (drug.name, drug.price, drug.active_substance, drug.form, drug.description,
                  drug.side_effects, drug.storage_conditions, drug.id)
        self.db.execute(query, params)

    @override
    def delete(self, id: int):
        query = "DELETE FROM drug WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
