from src.data.db_manager import DatabaseManager
from src.data.models.insurance_company import InsuranceCompany
from src.data.repositories.base_repository import BaseRepository


class InsuranceCompanyRepo(BaseRepository):

    def __init__(self, db: DatabaseManager):
        super().__init__(db)

    def get_all(self):
        query = "SELECT * FROM insurance_company"
        result = self.db.fetch(query)
        return [InsuranceCompany(*row) for row in result]

    def get_by_id(self, id: int):
        query = "SELECT * FROM insurance_company WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return InsuranceCompany(*result)

    def add(self, insurance_company: InsuranceCompany):
        query = "INSERT INTO insurance_company (id, code, abbreviation, name, street, house, city, psc) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            insurance_company.id, insurance_company.code, insurance_company.abbreviation, insurance_company.name,
            insurance_company.street, insurance_company.house, insurance_company.city,
            insurance_company.psc)
        self.db.execute(query, values)

    def update(self, insurance_company: InsuranceCompany):
        if insurance_company.id is None:
            self.add(insurance_company)
            return

        query = "UPDATE insurance_company SET code = %s, abbreviation = %s, name = %s, street = %s, house = %s, " \
                "city = %s, psc = %s WHERE id = %s"
        values = (
            insurance_company.code, insurance_company.abbreviation, insurance_company.name, insurance_company.street,
            insurance_company.house, insurance_company.city, insurance_company.psc, insurance_company.id)
        self.db.execute(query, values)

    def delete(self, id: int):
        query = "DELETE FROM insurance_company WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
