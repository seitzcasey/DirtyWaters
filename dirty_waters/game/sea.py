from dirty_waters.game.fleet import Fleet
from dirty_waters.game.grid.grid_manager import GridManager
from dirty_waters.game.ship import Ship


# this class represents an individual game
class Sea:
    fleets: dict[int, Fleet]
    grid_manager: GridManager

    def __init__(self, num_fleets: int, players_per_fleet: int, dimensions: tuple[int, int]):
        self.fleets = {}
        self.grid_manager = GridManager(dimensions)

        for i in range(num_fleets):
            fleet = Fleet(self.grid_manager, players_per_fleet)
            self.fleets[fleet.id] = fleet

    def is_ready_to_start(self) -> bool:
        for i in self.fleets:
            fleet = self.fleets[i]
            if not fleet.has_placed_all_ships():
                return False
        return True

    def does_ship_fit(self, fleet_id: int, flotilla_id: int, ship_id: int, coordinate: tuple[int, int], orientation: str) -> bool:
        try:
            fleet = self._get_fleet(fleet_id)
            ship = fleet.get_ship(flotilla_id, ship_id)
            return fleet.get_grid().does_ship_fit(ship, coordinate, orientation)
        except ValueError as e:
            print(f"Error checking ship fit '{e}'")
            return False

    def place_ship(self, fleet_id: int, flotilla_id: int, ship_id: int, coordinate: tuple[int, int], orientation: str) -> bool:
        try:
            fleet = self._get_fleet(fleet_id)
            return fleet.place_ship(flotilla_id, ship_id, coordinate, orientation)
        except ValueError as e:
            print(f"Error placing ship '{ship_id}': {e}")
            return False

    def check_hit(self, source_fleet_id: int, target_fleet_id: int, coordinate: tuple[int, int]) -> bool:
        try:
            source = self._get_fleet(source_fleet_id)
            target = self._get_fleet(target_fleet_id)
            if target.check_hit(coordinate):
                source.confirm_hit(target_fleet_id, coordinate)
                return True
            else:
                source.confirm_miss(target_fleet_id, coordinate)
                return False
        except ValueError as e:
            print(f"Error checking hit '{e}'")

    def try_begin_game(self) -> bool:
        if self.is_ready_to_start():
            self._begin_game()
            return True
        return False

    def _begin_game(self) -> None:
        print(f"Begin Game!")

    def _get_fleet(self, fleet_id: int) -> Fleet:
        return self.fleets[fleet_id]

    def _get_ship(self, fleet_id: int, flotilla_id: int, ship_id: int) -> Ship | None:
        try:
            fleet = self._get_fleet(fleet_id)
            return fleet.get_ship(flotilla_id, ship_id)
        except ValueError as e:
            print(f"Error getting ship '{e}'")
            return None
