from logic import *

# Axioms for wumpus worlds
wumpus_kb = FolKB(
    list(map(expr,
             ['TurnLeft(x, y) ==> TurnRight(x, y)',
              'TurnRight(N, E)',
              'TurnRight(E, S)',
              'TurnRight(S, W)',
              'TurnRight(W, N)',
              'Increasing(1, 2)',
              'Increasing(2, 3)',
              'Increasing(3, 4)',
             ]))
)


