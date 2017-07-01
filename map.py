from Levels import levels

class Map:
    def __init__(self, size_x, size_y, level):
        self.size_x = size_x
        self.size_y = size_y

        self.level = levels[level]
        self.blocks = self.level.blocks
        self.win_images = self.level.win_images
        self.sound_path = self.level.sound_path

        self.dx = 65
        self.dy = 35
        self.level_no = level
        self.move = 0

    def get_block(self, x, y):
        found_block = None
        for row in (self.blocks):
            for block in row:
                if block is not None and block.x == x and block.y == y:
                    found_block = block
                    return found_block
        return found_block