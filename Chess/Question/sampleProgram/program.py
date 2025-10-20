from sample import SimpleGame
from answer import ComplexGame

if __name__ == '__main__':
    # game = SimpleGame()
    # OPTIONAL: pass True to see board after every move, False for no board
    # This is an extra visualizer, not part of the core answer
    game = ComplexGame(show_board=True)
    game.setup()
    game.play(15)
