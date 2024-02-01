class Doctor:
    def __init__(
            self,
            id: int,
            title: str,
            first_name: str,
            middle_name: str,
            last_name: str,
            phone: str,
            email: str,
            specialization_id: int
    ):
        if id < 0 or specialization_id < 0:
            raise ValueError("Id value and specialization_id cannot be negative!")

        self.id = id
        self.title = title
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.specialization_id = specialization_id
