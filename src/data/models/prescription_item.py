class PrescriptionItem:
    def __init__(
            self,
            id: int,
            prescription_id: int,
            drug_id: int,
            quantity: int,
            dosage: str,
            instructions: str,
            picked_up: bool
    ):
        if id < 0 or prescription_id < 0 or drug_id < 0:
            raise ValueError("Id values cannot be negative!")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.id = id
        self.prescription_id = prescription_id
        self.drug_id = drug_id
        self.quantity = quantity
        self.dosage = dosage
        self.instructions = instructions
        self.picked_up = picked_up
