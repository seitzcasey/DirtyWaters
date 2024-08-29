
from typing import Optional
from dirty_waters.game.ship import Ship

class CellFlag:
    ship: bool
    hit: bool
    miss: bool

    def __init__(self):
        self.ship = False
        self.hit = False
        self.miss = False

class Cell:
    ship: Optional[Ship]

    def __init__(self, coordinate: tuple[int, int]):
        self.coordinate = coordinate
        self.ship = None
        self.flags = CellFlag()

    def place_ship(self, ship: Ship):
        self.ship = ship
        self.flags.ship = True
        print(f"Ship placed '{self.coordinate}'")

    def check_hit(self):
        print(f"checking hit '{self.coordinate}'")
        if self.ship and not self.flags.hit:
            self.flags.hit = True
            self.flags.miss = False
            self.ship.check_hit(self.coordinate)
        return self.flags.hit

    def hit(self):
        self.flags.hit = True
        self.flags.miss = False

    def miss(self):
        self.flags.miss = True
        self.flags.hit = False