from dirty_waters.game.ship import Ship

class Submarine(Ship):
    def __init__(self):
        super().__init__("Submarine", 3)