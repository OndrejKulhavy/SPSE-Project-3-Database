class DrugForm:
    def __init__(
            self,
            id: int,
            name: str
    ):
        if id < 0:
            raise ValueError("Id value cannot be negative!")

        self.id = id
        self.name = name
