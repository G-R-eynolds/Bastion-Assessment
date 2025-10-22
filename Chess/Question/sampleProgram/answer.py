from dataclasses import dataclass
import random

from sample import BaseGame
from chessLib.position import Position
from chessLib.move import KnightMove, BishopMove, QueenMove


@dataclass
class Piece:
    n: str
    mv: object
    pos: Position

    def valid_moves(self, b: "Board") -> list[Position]:
        # generate moves then drop ones landing on occupied squares
        ms = self.mv.valid_moves(self.pos)
        return [p for p in ms if not b.is_occupied(p)]


############################################################
# OPTIONAL EXTRA: ASCII board visualizer (not core answer) #
# I thought this would be a nice touch given the context of the "game", and it wasn't too hard to add #
############################################################
class Board:
    def __init__(self, size: int = 8):
        self.size = size
        self._ps: list[Piece] = []
        self._show = False  # ascii toggle
        self._history: list[tuple] = []  # track all moves

    def set_show(self, v: bool):
        self._show = v
    
    @property
    def history(self) -> list[tuple]:
        return self._history

    def ascii(self):
        # make empty
        g = [['.' for _ in range(self.size)] for _ in range(self.size)]
        # put pieces
        for p in self._ps:
            c = p.n[0].upper()
            g[p.pos.y-1][p.pos.x-1] = c
        # print top to bottom
        for row in reversed(g):
            print(' '.join(row))
############################################################

    @property
    def pieces(self) -> list[Piece]:
        return self._ps

    def add_piece(self, pc: Piece):
        if self.is_occupied(pc.pos):
            raise ValueError("occ: " + pc.pos.to_string())
        self._ps.append(pc)

    def is_occupied(self, p: Position) -> bool:
        for x in self._ps:
            if x.pos == p:
                return True
        return False

    def move_piece(self, pc: Piece, np: Position):
        if self.is_occupied(np):
            raise ValueError("occ: " + np.to_string())
        op = pc.pos
        pc.pos = np
        self._history.append((pc.n, op.to_string(), np.to_string()))



class ComplexGame(BaseGame):
    def __init__(self, show_board=False):
        self._b: Board | None = None
        self._show = show_board

    def setup(self):
        b = Board(8)
        b.add_piece(Piece("Knight", KnightMove(), Position(3, 3)))
        b.add_piece(Piece("Bishop", BishopMove(), Position(6, 6)))
        b.add_piece(Piece("Queen", QueenMove(), Position(4, 1)))
        b.set_show(self._show)
        self._b = b
        for p in self._b.pieces:
            print(f"Setup: {p.n} at {p.pos.to_string()}")
        if self._show:
            print("init:")
            self._b.ascii()

    def play(self, moves: int):
        if not self._b:
            raise RuntimeError("setup")
        for i in range(moves):
            mp = [p for p in self._b.pieces if p.valid_moves(self._b)]
            if not mp:
                print(f"{i}: no-moves")
                break
            pc = random.choice(mp)
            ops = pc.valid_moves(self._b)
            np = random.choice(ops)
            o = pc.pos
            self._b.move_piece(pc, np)
            print(f"{i}: {pc.n} {o.to_string()}->{np.to_string()}")
            if self._show:
                self._b.ascii()
    
    def print_history(self):
        """Print all moves made during the game."""
        if not self._b:
            raise RuntimeError("setup")
        print("\n=== Game History ===")
        for i, (piece, from_pos, to_pos) in enumerate(self._b.history):
            print(f"{i}: {piece} {from_pos} -> {to_pos}")
        print(f"Total moves: {len(self._b.history)}")
