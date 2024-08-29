import random
from dirty_waters.game.grid.cell import Cell
from dirty_waters.game.ship import Ship


class Grid:
    dimensions: tuple[int, int]
    fleet_id: int
    cells: list[Cell]

    def __init__(self, dimensions: tuple[int, int], fleet_id: int):
        self.dimensions = dimensions
        self.fleet_id = fleet_id
        self.cells = []

        self.initialize_cells()

    def initialize_cells(self):
        width, height = self.dimensions
        self.cells = []
        for r in range(height):
            for c in range(width):
                self.cells.append(Cell((r, c)))

    def get_cell_index(self, coordinate: tuple[int, int]) -> int:
        row, col = coordinate
        width, height = self.dimensions
        if 0 <= row < height and 0 <= col < width:
            return row * height + col
        raise ValueError(f"Invalid coordinate '{coordinate}'")

    def get_cell(self, coordinate: tuple[int, int]):
        index = self.get_cell_index(coordinate)
        return self.cells[index]

    def get_random_cell(self):
        return self.cells[random.randint(0, len(self.cells) - 1)]

    def does_ship_fit(self, ship: Ship, coordinate: tuple[int, int], orientation: str):
        try:
            for coord in ship.get_coordinates(coordinate, orientation):
                cell = self.get_cell(coord)
                if cell.flags.ship:
                    return False
            return True
        except ValueError as e:
            print(f"Error checking ship fit '{e}'")
            return False

    def place_ship(self, ship: Ship, coordinate: tuple[int, int], orientation: str) -> bool:
        try:
            if self.does_ship_fit(ship, coordinate, orientation):
                ship.place(coordinate, orientation)
                for coord in ship.coordinates:
                    cell = self.get_cell(coord)
                    cell.place_ship(ship)
                return True
        except ValueError as e:
            print(f"Error checking ship fit '{e}'")
            return False

    def check_hit(self, coordinate: tuple[int, int]):
        try:
            cell = self.get_cell(coordinate)
            return cell.check_hit()
        except ValueError as e:
            print(f"Error checking hit '{e}'")

    def confirm_hit(self, coordinate: tuple[int, int]):
        try:
            cell = self.get_cell(coordinate)
            cell.hit()
        except ValueError as e:
            print(f"Error confirming hit '{e}'")

    def confirm_miss(self, coordinate: tuple[int, int]):
        try:
            cell = self.get_cell(coordinate)
            cell.miss()
        except ValueError as e:
            print(f"Error confirming miss '{e}'")

    def to_html(self, include_style: bool = True) -> str:
        # Determine the smallest dimension to create a perfect square grid
        min_dimension = min(self.dimensions)

        # Start the HTML table with embedded CSS for square cells
        html = '''<table border="1" cellpadding="5" cellspacing="0">'''

        # Create a perfect square grid
        for r in range(min_dimension):
            html += '  <tr>\n'
            for c in range(min_dimension):
                cell = self.cells[r * self.dimensions[0] + c]  # Calculate correct cell index

                # Determine cell content based on its flags
                if cell.flags.hit:
                    cell_content = "X" if cell.ship else "O"  # 'X' for hit, 'O' for miss
                else:
                    cell_content = "S" if cell.ship else "&nbsp;"  # 'S' for a ship, blank otherwise

                # Create a button for each cell with an onclick event to send the payload
                html += f'''
                    <td>
                        <button onclick="sendPayload('{self.fleet_id}', '{(r, c)}')">
                            {cell_content}
                        </button>
                    </td>
                '''
            html += '  </tr>\n'

        # Close the HTML table
        html += '</table>'
        return html
