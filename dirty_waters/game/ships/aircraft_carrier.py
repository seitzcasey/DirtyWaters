from dirty_waters.game.ship import Ship

class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__("Aircraft Carrier", 5)