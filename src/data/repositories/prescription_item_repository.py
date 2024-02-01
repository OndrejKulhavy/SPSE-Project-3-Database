from src.data.models.prescription_item import PrescriptionItem
from src.data.repositories.base_repository import BaseRepository


class PrescriptionItemRepo(BaseRepository):
    def __init__(self, db):
        super().__init__(db)

    def get_all(self):
        query = "SELECT * FROM prescription_item"
        result = self.db.fetch(query)
        return [PrescriptionItem(*row) for row in result]

    def get_by_id(self, id: int):
        query = "SELECT * FROM prescription_item WHERE id = %s"
        params = (id,)
        result = self.db.fetch_one(query, params)
        if result is None:
            return None
        return PrescriptionItem(*result)

    def add(self, prescription_item: PrescriptionItem):
        query = "INSERT INTO prescription_item (prescription_id, drug_id, quantity, dosage, instructions, picked_up) " \
                "VALUES (%s, %s, %s, %s, %s, %s)"
        params = (prescription_item.prescription_id, prescription_item.drug_id, prescription_item.quantity,
                  prescription_item.dosage, prescription_item.instructions, prescription_item.picked_up)
        self.db.execute(query, params)

    def update(self, prescription_item: PrescriptionItem):
        if prescription_item.id is None:
            self.add(prescription_item)
            return
        query = "UPDATE prescription_item SET prescription_id = %s, drug_id = %s, quantity = %s, dosage = %s, " \
                "instructions = %s, picked_up = %s WHERE id = %s"
        params = (prescription_item.prescription_id, prescription_item.drug_id, prescription_item.quantity,
                  prescription_item.dosage, prescription_item.instructions,
                  prescription_item.picked_up, prescription_item.id)
        self.db.execute(query, params)

    def delete(self, id: int):
        query = "DELETE FROM prescription_item WHERE id = %s"
        params = (id,)
        self.db.execute(query, params)
