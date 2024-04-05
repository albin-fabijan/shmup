class Level :
    def __init__(self, ships) :
        self.ships = ships
        self.ship_count = len(self.ships)
        self.finished = False
