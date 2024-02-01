from datetime import date


class Prescription:
    def __init__(
            self,
            id: int,
            patient_id: int,
            issued_by_doctor_id: int,
            issued_date: date,
            valid_until: date,
            status: str,
            type: str
    ):
        if id < 0 or patient_id < 0 or issued_by_doctor_id < 0:
            raise ValueError("Id values cannot be negative!")

        self.id = id
        self.patient_id = patient_id
        self.issued_by_doctor_id = issued_by_doctor_id
        self.issued_date = issued_date
        self.valid_until = valid_until
        self.status = status
        self.type = type
