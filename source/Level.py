class Level :
    def __init__(self, ships, music) :
        self.ships = ships
        self.ship_count = len(self.ships)
        self.finished = False
        self.music = music
