class Patient:
    def __init__(
            self,
            id: int,
            name: str,
            phone: str,
            email: str,
            street: str,
            house: int,
            city: str,
            psc: int,
            insurance_company_id: int
    ):
        if id < 0 or insurance_company_id < 0:
            raise ValueError("Id value cannot be negative!")
        if house < 0:
            raise ValueError("House value cannot be negative!")
        if psc < 0:
            raise ValueError("PSC value cannot be negative!")

        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.street = street
        self.house = house
        self.city = city
        self.psc = psc
        self.insurance_company_id = insurance_company_id
