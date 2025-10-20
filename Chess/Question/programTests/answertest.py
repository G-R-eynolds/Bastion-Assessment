import math
import unittest

from chessLib.move import BishopMove, QueenMove
from chessLib.position import Position


class BishopTests(unittest.TestCase):
	def test_bishop_move_from_inside_board(self):
		pos = Position(4, 4)
		bishop = BishopMove()
		moves = bishop.valid_moves(pos)
		self.assertIsNotNone(moves)

		self.assertEqual(13, len(moves))
		for move in moves:
			self.assertTrue(1 <= move.x <= 8 and 1 <= move.y <= 8)
			self.assertEqual(math.fabs(move.x - pos.x), math.fabs(move.y - pos.y))
			self.assertNotEqual(move, pos)

	def test_bishop_move_from_corner(self):
		pos = Position(1, 1)
		bishop = BishopMove()
		moves = bishop.valid_moves(pos)
		self.assertIsNotNone(moves)

		self.assertEqual(7, len(moves))
		for i in range(2, 9):
			self.assertIn(Position(i, i), moves)


class QueenTests(unittest.TestCase):
	def test_queen_move_from_inside_board(self):
		pos = Position(4, 4)
		queen = QueenMove()
		moves = queen.valid_moves(pos)
		self.assertIsNotNone(moves)

		self.assertEqual(27, len(moves))
		for move in moves:
			self.assertTrue(1 <= move.x <= 8 and 1 <= move.y <= 8)
			dx = move.x - pos.x
			dy = move.y - pos.y
			is_rook_like = (dx == 0) != (dy == 0)
			is_bishop_like = math.fabs(dx) == math.fabs(dy) and dx != 0
			self.assertTrue(is_rook_like or is_bishop_like)
			self.assertNotEqual(move, pos)

	def test_queen_move_from_corner(self):
		pos = Position(1, 1)
		queen = QueenMove()
		moves = queen.valid_moves(pos)
		self.assertIsNotNone(moves)

		self.assertEqual(21, len(moves))
		horizontals = [Position(i, 1) for i in range(2, 9)]
		verticals = [Position(1, j) for j in range(2, 9)]
		diagonals = [Position(k, k) for k in range(2, 9)]
		for m in horizontals + verticals + diagonals:
			self.assertIn(m, moves)


if __name__ == '__main__':
	unittest.main()