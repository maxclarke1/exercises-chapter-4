from life import Game, Pattern, glider
import numpy as np
A = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

g = Game(8)
g.insert(Pattern(A), [2, 5])
g.play()