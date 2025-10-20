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


class BishopMove:
    def valid_moves(self, pos: Position) -> list:
        # diag rays
        res = []
        dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in dirs:
            x, y = pos.x + dx, pos.y + dy
            while 1 <= x <= 8 and 1 <= y <= 8:
                res.append(Position(x, y))
                x += dx
                y += dy
        return res


class QueenMove:
    def valid_moves(self, pos: Position) -> list:
        # rook + bishop rays
        res = []
        dirs = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for dx, dy in dirs:
            x, y = pos.x + dx, pos.y + dy
            while 1 <= x <= 8 and 1 <= y <= 8:
                res.append(Position(x, y))
                x += dx
                y += dy
        return res
