from src.data.models.patient import Patient
from src.data.repositories.base_repository import BaseRepository


class PatientRepo(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

    def get_all(self):
        query = "SELECT * FROM patient"
        result = self.db.fetch(query)
        return [Patient(*row) for row in result]

    def get_by_id(self, id: int):
        query = "SELECT * FROM patient WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Patient(*result)

    def add(self, entity):
        query = "INSERT INTO patient (name, phone, email, street, house, city, psc, insurance_company_id) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (entity.name, entity.phone, entity.email, entity.street, entity.house, entity.city, entity.psc,
                  entity.insurance_company_id)
        self.db.execute(query, params)

    def update(self, patient: Patient):
        if patient.id is None:
            self.add(patient)
            return

        query = "UPDATE patient SET name = %s, phone = %s, email = %s, street = %s, house = %s, city = %s, psc = %s, " \
                "insurance_company_id = %s WHERE id = %s"
        params = (
            patient.name, patient.phone, patient.email, patient.street, patient.house, patient.city, patient.psc,
            patient.insurance_company_id, patient.id)
        self.db.execute(query, params)

    def delete(self, id: int):
        query = "DELETE FROM patient WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
