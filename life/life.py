import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0],
                   [0, 0, 1],
                   [1, 1, 1]])

blinker = np.array([
 [0, 0, 0],
 [1, 1, 1],
 [0, 0, 0]])

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    """
    A class used to represent the game of life.

    Attributes
    ----------
    board: a Size x Size board for the game.
    """

    def __init__(self, Size):
        """
        Parameters
        ----------
        Size : int
            The dimension of the board in the game of life.
        """

        self.board = np.zeros((Size, Size))

    def play(self):
        """
        Starts the game and keeps it running.
        """

        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move(), self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """
        Decides if a cell live or dies.
        """

        STENCIL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        NeighbourCount = convolve2d(self.board, STENCIL, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 if (NeighbourCount[i, j] == 3 or
                                         (NeighbourCount[i, j] == 2 and
                                         self.board[i, j])) else 0

    def __setitem__(self, key, value):
        """
        Sets specific value to square on board.
        """

        self.board[key] = value

    def show(self):
        """
        Outputs the moves from the game of life.
        """

        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()

    def insert(self, pattern, squareCoord):
        numOfRows, numOfCols = len(pattern.grid), len(pattern.grid[0])
        startX = int(squareCoord[0] - np.floor(numOfCols/2))
        startY = int(squareCoord[1] - np.floor(numOfRows/2))
        print(startX, startY, numOfRows, numOfCols)

        for i in range(0, numOfCols):
            for j in range(0, numOfRows):
                self.board[i+startX][j+startY] = pattern.grid[i][j]


class Pattern:

    def __init__(self, pattern):
        self.grid = pattern

    def flip_vertical(self):
        return Pattern(np.flipud(self.grid))

    def flip_horizontal(self):
        return Pattern(np.fliplr(self.grid))

    def flip_diag(self):
        return Pattern(np.transpose(self.grid))

    def rotate(self, n):
        B = self.grid
        for i in range(n):
            A = np.transpose(B)
            B = np.flipud(A)
        return Pattern(B)
