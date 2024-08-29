from dirty_waters.game.grid.grid import Grid


class GridManager:

    grids: dict[int, Grid]
    def __init__(self, dimensions: tuple[int, int]):
        self.dimensions = dimensions
        self.grids = {}

    def create_grid(self, fleet_id: int) -> Grid:
        grid = Grid(self.dimensions, fleet_id)
        self.grids[fleet_id] = grid
        return grid

    def get_grid(self, fleet_id: int) -> Grid:
        return self.grids[fleet_id]

    def to_html(self) -> str:
        grid_html = ""
        style = True
        for i in self.grids:
            grid_html += self.grids[i].to_html(style)
            style = False
        return grid_html