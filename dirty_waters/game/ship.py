
class Ship:
    _id_counter: int = 0

    name: str
    size: int
    hits: int
    coordinates: list[tuple[int, int]]
    sunk: bool
    placed: bool

    def __init__(self, name, size):
        """
        Initialize a Ship object.

        :param name: Name of the ship (e.g., "Battleship", "Destroyer").
        :param size: Size of the ship (number of grid spaces it occupies).
        """
        self.id = Ship._id_counter
        Ship._id_counter += 1
        self.name = name
        self.size = size
        self.hits = 0  # Track the number of hits
        self.coordinates = []  # List to store ship's coordinates (e.g., [(1, 1), (1, 2)])
        self.sunk = False
        self.placed = False

        print(f"Created Ship: {self.name} {self.id}")

    def place(self, coordinate, orientation):
        """
        Place the ship on the board.

        :param coordinate: Tuple of (row, column) where the ship starts.
        :param orientation: 'H' for horizontal or 'V' for vertical.
        """
        self.coordinates = self.get_coordinates(coordinate, orientation)
        self.placed = True

    def get_coordinates(self, coordinate, orientation) -> list[tuple[int, int]]:
        row, col = coordinate
        coordinates = [coordinate]

        for i in range(self.size):
            if orientation == 'H':
                coordinates.append((row, col + i))
            elif orientation == 'V':
                coordinates.append((row + i, col))
            else:
                raise ValueError("Invalid orientation. Use 'H' for horizontal or 'V' for vertical.")
        return coordinates

    def check_hit(self, coordinate) -> bool:
        """
        Check if the ship is hit.

        :param coordinate: Tuple of (row, column) of the shot.
        :return: True if the ship is hit, False otherwise.
        """
        if coordinate in self.coordinates:
            self.hits += 1
            print(f"{self.name} got hit at {coordinate}!")
            self.check_if_sunk()
            return True
        return False

    def check_if_sunk(self):
        """
        Check if the ship is sunk.
        """
        if self.hits >= self.size:
            self.sunk = True
            print(f"{self.name} is sunk!")

    def __repr__(self):
        return f"Ship(name={self.name}, size={self.size}, coordinates={self.coordinates}, hits={self.hits}, is_sunk={self.sunk})"
