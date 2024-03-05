import unittest

class Elevator:
    def __init__(self, num_floors):
        self.current_floor = 1
        self.num_floors = num_floors
        self.direction = 1 # 1 for up, -1 for down
        self.stops = set()

    def go_up(self):
        if self.current_floor < self.num_floors:
            self.current_floor += 1
            self.stops.discard(self.current_floor)

    def go_down(self):
        if self.current_floor > 1:
            self.current_floor -= 1
            self.stops.discard(self.current_floor)

    def add_stop(self, floor):
        if 1 <= floor <= self.num_floors:
            self.stops.add(floor)

    def get_stops(self):
        return self.stops

class TestElevator(unittest.TestCase):
    def test_go_up(self):
        e = Elevator(5)
        e.current_floor = 2
        e.go_up()
        self.assertEqual(e.current_floor, 3)

    def test_go_down(self):
        e = Elevator(5)
        e.current_floor = 3
        e.go_down()
        self.assertEqual(e.current_floor, 2)

    def test_add_stop(self):
        e = Elevator(5)
        e.add_stop(3)
        self.assertIn(3, e.stops)

    def test_has_stop(self):
        e = Elevator(5)
        e.add_stop(3)
        self.assertIn(3, e.get_stops())

if __name__ == '__main__':
    unittest.main()
