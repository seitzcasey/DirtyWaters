from dirty_waters.game.ship import Ship
from dirty_waters.game.ships.aircraft_carrier import AircraftCarrier
from dirty_waters.game.ships.battleship import Battleship
from dirty_waters.game.ships.destroyer import Destroyer
from dirty_waters.game.ships.patrol_boat import PatrolBoat
from dirty_waters.game.ships.submarine import Submarine

# this represents a single player
class Flotilla:
    _id_counter: int = 0

    id: int
    name: str
    ships: list[Ship]

    def __init__(self, name=''):
        self.id = Flotilla._id_counter
        Flotilla._id_counter += 1
        self.name = name
        self.ships = [
            AircraftCarrier(),
            Battleship(),
            Destroyer(),
            Submarine(),
            PatrolBoat()
        ]

    def get_ship(self, ship_id: int):
        for s in self.ships:
            if s.id == ship_id:
                return s
        raise ValueError("Invalid ship_id.")

    def has_placed_all_ships(self):
        for s in self.ships:
            if not s.placed:
                return False

    def place_ship(self, ship_id: int, coordinate: tuple[int, int], orientation: str):
        """
        Place a ship on the board.

        :param ship_id: id of the ship.
        :param coordinate: Tuple of (row, column) where the ship starts.
        :param orientation: 'H' for horizontal or 'V' for vertical.
        """
        try:
            ship = self.get_ship(ship_id)

            if ship.placed:
                return False

            ship.place(coordinate, orientation)
            return True
        except ValueError as e:
            print(f"Error placing ship '{self.name}': {e}")
            return False

    def is_defeated(self):
        for s in self.ships:
            if not s.sunk:
                return False
        return True