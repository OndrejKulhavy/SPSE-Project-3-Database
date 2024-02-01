from typing import override

from src.data.db_manager import DatabaseManager
from src.data.models.doctor import Doctor
from src.data.repositories.base_repository import BaseRepository


class DoctorRepo(BaseRepository):

    def __init__(self, db: DatabaseManager):
        super().__init__(db)

    @override
    def get_all(self):
        query = "SELECT * FROM doctor"
        result = self.db.fetch(query)
        return [Doctor(*row) for row in result]

    @override
    def get_by_id(self, id):
        query = "SELECT * FROM doctor WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return Doctor(*result)

    @override
    def add(self, doctor: Doctor):
        query = "INSERT INTO doctor (title, first_name, middle_name, last_name, phone, email, specialization_id) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        params = (doctor.title, doctor.first_name, doctor.middle_name, doctor.last_name, doctor.phone, doctor.email,
                  doctor.specialization_id)
        self.db.execute(query, params)

    @override
    def update(self, doctor: Doctor):
        if doctor.id is None:
            self.add(doctor)
            return

        query = "UPDATE doctor SET title = %s, first_name = %s, middle_name = %s, last_name = %s, phone = %s, " \
                "email = %s, specialization_id = %s WHERE id = %s"
        params = (doctor.title, doctor.first_name, doctor.middle_name, doctor.last_name, doctor.phone, doctor.email,
                  doctor.specialization_id, doctor.id)
        self.db.execute(query, params)

    @override
    def delete(self, id):
        query = "DELETE FROM doctor WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
