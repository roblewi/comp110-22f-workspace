"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730571332"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Calculates the distance between two points using the Pythagorean theorem."""
        diff_x: float = self.x - other.x
        diff_y: float = self.y - other.y
        dist: float = sqrt(diff_x * diff_x + diff_y * diff_y)
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self):
        """Updates location and keeps track of recovery."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.sickness = constants.IMMUNE
        
    def color(self) -> str:
        """Determines the color of the cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "crimson"
        if self.is_immune():
            return "magenta"

    def contract_disease(self) -> None:
        """Cell becomes infected."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Checks if cell is vulnerable."""
        return self.sickness == constants.VULNERABLE
    
    def is_infected(self) -> bool:
        """Checks if cell is infected."""
        return self.sickness >= constants.INFECTED

    def contact_with(self, other) -> None:
        """Causes cells to become infected if they come into contact with an infected cell."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        elif self.is_vulnerable() and other.is_infected():
            self.contract_disease()
    
    def immunize(self):
        """Cell becomes immune."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self):
        """Checks if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, num_infected: int, num_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if num_infected >= cells or num_infected <= 0:
            raise ValueError('\'num_infected\' cannot be bigger than the population or less than 1.')
        if num_immune >= cells or num_immune < 0:
            raise ValueError('\'num_immune\' cannot be bigger than the population or less than 1.')
        self.population = []
        
        # Initializing the healthy and infected cells.
        i: int = 0
        for _ in range(cells):
            start_loc: Point = self.random_location()
            start_dir: Point = self.random_direction(speed)
            cell: Cell = Cell(start_loc, start_dir)
            if i < num_infected:
                cell.sickness = constants.INFECTED
                i += 1
            elif i < num_infected + num_immune:
                cell.sickness = constants.IMMUNE
                i += 1
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        y: float = random() * constants.BOUNDS_WIDTH - constants.MAX_Y
        return Point(x, y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        dx: float = cos(random_angle) * speed
        dy: float = sin(random_angle) * speed
        return Point(dx, dy)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
    
    def check_contacts(self) -> None:
        """Checks if any two cells are in contact with each other."""
        # TODO - MAKE MORE EFFICIENT (every cell pair getting checked multiple times and against itself)
        for i in self.population:
            for j in self.population:
                if i.location.distance(j.location) <= constants.CELL_RADIUS:
                    i.contact_with(j)

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        j = 0
        for i in self.population:
            if i.is_infected():
                j += 1
        if j == 0:
            return True
        return False