import random
from dirty_waters.game.fleet import Fleet
from dirty_waters.game.sea import Sea

class DefaultGame(Sea):
    fleet_a: Fleet
    fleet_b: Fleet
    def __init__(self):
        super().__init__(2, 1, (10, 10))

        for i in self.fleets:
            fleet = self.fleets[i]
            self.initialize_fleet(fleet)

    def initialize_fleet(self, fleet: Fleet):
        print(f"Initializing Fleet: '{fleet.id}'")
        grid = fleet.get_grid()
        for f in fleet.flotillas:
            for s in f.ships:
                random_cell = grid.get_random_cell()
                random_orientation = 'V' if random.randint(0, 1) == 0 else 'H'
                while not grid.does_ship_fit(s, random_cell.coordinate, random_orientation):
                    random_cell = grid.get_random_cell()
                grid.place_ship(s, random_cell.coordinate, random_orientation)