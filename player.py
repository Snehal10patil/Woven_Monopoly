class Player:
    def __init__(self, name: str):
        self.name = name
        self.money = 16
        self.position = 0
        self.properties = []

    def add_money(self, amount: int):
        self.money += amount

    def deduct_money(self, amount: int):
        self.money -= amount
        if self.money < 0:
            self.money = 0

    def is_bankrupt(self) -> bool:
        return self.money == 0

    def add_property(self, property_name: str):
        self.properties.append(property_name)

    def owns_property(self, property_name: str) -> bool:
        return property_name in self.properties