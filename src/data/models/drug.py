class Drug:
    def __init__(
            self,
            id: int,
            name: str,
            price: float,
            active_substance: str,
            form: int,
            description: str,
            side_effects: str,
            storage_conditions: str
    ):
        if id < 0 or form < 0:
            raise ValueError("Id value cannot be negative!")

        self.id = id
        self.name = name
        self.price = price
        self.active_substance = active_substance
        self.form = form
        self.description = description
        self.side_effects = side_effects
        self.storage_conditions = storage_conditions
