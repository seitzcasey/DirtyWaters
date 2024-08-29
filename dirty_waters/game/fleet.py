from dirty_waters.game.flotilla import Flotilla
from dirty_waters.game.grid.grid import Grid
from dirty_waters.game.grid.grid_manager import GridManager
from dirty_waters.game.ship import Ship


# this class represents a "team" of 1 or more players.
# these players share the same play area
class Fleet:
    _id_counter = 0

    id: int
    grid_manager: GridManager
    flotillas: list[Flotilla]

    def __init__(self, grid_manager: GridManager, num_flotillas: int):
        self.id = Fleet._id_counter
        Fleet._id_counter += 1
        self.grid_manager = grid_manager
        self.grid_manager.create_grid(self.id)
        self.flotillas = []
        for i in range(num_flotillas):
            self.flotillas.append(Flotilla())

    def get_flotilla(self, flotilla_id) -> Flotilla:
        for f in self.flotillas:
            if f.id == flotilla_id:
                return f
        raise ValueError("Invalid flotilla_id.")

    def get_grid(self) -> Grid:
        return self.grid_manager.get_grid(self.id)

    def get_ship(self, flotilla_id, ship_id) -> Ship:
        try:
            flotilla = self.get_flotilla(flotilla_id)
            return flotilla.get_ship(ship_id)
        except ValueError as e:
            print(f"Error getting ship '{e}'")

    def place_ship(self, flotilla_id: int, ship_id: int, coordinate: tuple[int, int], orientation: str) -> bool:
        try:
            flotilla = self.get_flotilla(flotilla_id)
            flotilla.place_ship(ship_id, coordinate, orientation)
        except ValueError as e:
            print(f"Error placing ship '{ship_id}': {e}")
            return False

    def has_placed_all_ships(self) -> bool:
        for f in self.flotillas:
            if not f.has_placed_all_ships():
                return False
        return True

    def check_hit(self, coordinate) -> bool:
        """
        check if the given coordinate hits a ship that belongs to this fleet
        :param coordinate:
        :return: True if a hit occurs
        """
        return self.get_grid().check_hit(coordinate)

    def confirm_hit(self, fleet_id: int, coordinate: tuple[int, int]) -> None:
        try:
            grid = self.grid_manager.get_grid(fleet_id)
            grid.confirm_hit(coordinate)
        except ValueError as e:
            print(f"Error confirming hit '{e}'")

    def confirm_miss(self, fleet_id: int, coordinate: tuple[int, int]) -> None:
        try:
            grid = self.grid_manager.get_grid(fleet_id)
            grid.confirm_miss(coordinate)
        except ValueError as e:
            print(f"Error confirming hit '{e}'")

    def is_defeated(self) -> bool:
        for f in self.flotillas:
            if not f.is_defeated():
                return False
        return True