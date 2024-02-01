from src.data.models.prescription import Prescription
from src.data.repositories.base_repository import BaseRepository


class PrescriptionRepo(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

    def get_all(self):
        query = "SELECT * FROM prescription"
        result = self.db.fetch(query)
        return [Prescription(*row) for row in result]

    def get_by_id(self, id: int):
        query = "SELECT * FROM prescription WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Prescription(*result)

    def add(self, prescription: Prescription):
        query = "INSERT INTO prescription (patient_id, issued_by_doctor_id, issued_date, valid_until, status, type) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            prescription.patient_id, prescription.issued_by_doctor_id, prescription.issued_date,
            prescription.valid_until,
            prescription.status,
            prescription.type)
        self.db.execute(query, params)

    def update(self, prescription: Prescription):
        if prescription.id is None:
            self.add(prescription)
            return

        query = "UPDATE prescription SET patient_id = %s, issued_by_doctor_id = %s, issued_date = %s, " \
                "valid_until = %s, status = %s, type = %s WHERE id = %s"
        params = (prescription.patient_id, prescription.issued_by_doctor_id, prescription.issued_date,
                  prescription.valid_until, prescription.status, prescription.type, prescription.id)
        self.db.execute(query, params)

    def delete(self, id: int):
        query = "DELETE FROM prescription WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
