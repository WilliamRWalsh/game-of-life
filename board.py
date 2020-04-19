from random import randrange


class Board():

    def __init__(self, width: int = 100, height: int = 100):
        self.width = width
        self.height = height
        self._generate_board()

    def update(self):
        x = y = 0
        new_board = self._new_board()
        self.board = new_board

    def _new_board(self):
        new_board = []
        for x, row in enumerate(self.board):
            new_row = []
            for y, is_alive in enumerate(row):
                is_alive = self._dead_or_alive(x, y, is_alive)
                new_row.append(is_alive)
            new_board.append(new_row)
        return new_board

    def _is_cell_alive(self, x , y):
        if x < 0 or y < 0 or x > self.width - 1 or y > self.height - 1:
            return None
        return self.board[x][y]

    def _dead_or_alive(self, x, y, is_alive):
        num_neighbors = self._number_of_neighbors(x, y)
        if is_alive and (num_neighbors == 2 or num_neighbors == 3):
            return True
        if not is_alive and num_neighbors == 3:
            return True
        return False

    def _number_of_neighbors(self, x, y):
        shift = [-1, 0, 1]
        num_neighbors = 0
        for x_shift in shift:
            for y_shift in shift:
                if x_shift == 0 and y_shift == 0:
                    continue
                if self._is_cell_alive(x + x_shift, y + y_shift) == True:
                    num_neighbors += 1
        return num_neighbors

    def _generate_board(self, chance_per_cell=40):
        board = []
        for x in range(0, self.width):
            new_row = []
            for y in range(0, self.height):
                is_alive = True if randrange(0, 99) < chance_per_cell else False
                new_row.append(is_alive)
            board.append(new_row)
        self.board = board

    def __str__(self):
        board_str = ""
        for x, row in enumerate(self.board):
            row_str = ""
            for y, is_alive in enumerate(row):
                row_str += str(is_alive) + "\t"
            board_str += row_str + "\n"
        return board_str
