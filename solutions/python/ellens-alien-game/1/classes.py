"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int, health: int = 3) -> None:
       self.x_coordinate = x_coordinate 
       self.y_coordinate = y_coordinate
       self.health = health
       Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1 if self.health > 0 else 0

    def is_alive(self):
        return self.health > 0
    
    def teleport(self, x: int, y: int):
        self.x_coordinate = x
        self.y_coordinate = y

    def collision_detection(self, other):
        ...

def new_aliens_collection(positions: list[tuple[int, int]]) ->  list[Alien]:
    return [Alien(x,y) for x, y in positions]