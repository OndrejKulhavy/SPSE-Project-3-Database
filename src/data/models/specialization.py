class Specialization:
    def __init__(
            self,
            id: int,
            name: str
    ):
        if id < 0:
            raise ValueError("Id cannot be negative!")

        self.id = id
        self.name = name
