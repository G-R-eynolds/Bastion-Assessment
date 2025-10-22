from chessLib.position import Position


class KnightMove:
    __moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

    def valid_moves(self, pos: Position) -> list:
        result = []
        for m in self.__moves:
            p = Position(pos.x + m[0], pos.y + m[1])
            if 8 >= p.x > 0 and 8 >= p.y > 0:
                result.append(p)
        return result


class RayMove:
    @staticmethod
    def _rays(pos: Position, dirs: list) -> list:
        """Generate all valid positions along rays in given directions."""
        res = []
        for dx, dy in dirs:
            x, y = pos.x + dx, pos.y + dy
            while 1 <= x <= 8 and 1 <= y <= 8:
                res.append(Position(x, y))
                x += dx
                y += dy
        return res


class BishopMove(RayMove):
    __diag_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def valid_moves(self, pos: Position) -> list:
        return self._rays(pos, self.__diag_dirs)


class QueenMove(RayMove):
    __all_dirs = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    def valid_moves(self, pos: Position) -> list:
        return self._rays(pos, self.__all_dirs)
