from src.data.models.drug_form import DrugForm
from src.data.repositories.base_repository import BaseRepository


class DrugFormRepo(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

    def get_all(self):
        query = "SELECT * FROM drug_form"
        result = self.db.fetch(query)
        return [DrugForm(*row) for row in result]

    def get_by_id(self, id: int):
        query = "SELECT * FROM drug_form WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return DrugForm(*result)

    def add(self, drug_form: DrugForm):
        query = "INSERT INTO drug_form (name) VALUES (%s)"
        params = (drug_form.name,)
        self.db.execute(query, params)

    def update(self, drug_form: DrugForm):
        if drug_form.id is None:
            self.add(drug_form)

        query = "UPDATE drug_form SET name = %s WHERE id = %s"
        params = (drug_form.name, drug_form.id)
        self.db.execute(query, params)

    def delete(self, id: int):
        query = "DELETE FROM drug_form WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
