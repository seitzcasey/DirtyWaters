from dirty_waters.game.ship import Ship

class Destroyer(Ship):
    def __init__(self):
        super().__init__("Destroyer", 3)