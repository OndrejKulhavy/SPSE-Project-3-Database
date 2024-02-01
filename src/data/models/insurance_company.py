class InsuranceCompany:
    def __init__(
            self,
            id: int,
            code: int,
            abbreviation: str,
            name: str,
            street: str,
            house: int,
            city: str,
            psc: int
    ):

        if id < 0:
            raise ValueError("Id value cannot be negative!")
        if code < 0:
            raise ValueError("Code value cannot be negative!")
        if house < 0:
            raise ValueError("House value cannot be negative!")
        if psc < 0:
            raise ValueError("PSC value cannot be negative!")

        self.id = id
        self.code = code
        self.abbreviation = abbreviation
        self.name = name
        self.street = street
        self.house = house
        self.city = city
        self.psc = psc
