import sys
sys.path.append("../../..")
from Lesson.Lesson16Summary.AlphaZeroBattle.Game import Board,Game


class Human(object):
    def __init__(self):
        self.player = None

    def set_player_ind(self,p):
        self.player = p

    def get_action(self, board):
        try:
            location = input("请输入你下棋的位置 x,y: ")
            print(location)
            if isinstance(location, str):
                location = [int(n, 10) for n in location.split(",")]
            move = board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in board.availables:
            print("输入位置非法")
            move = self.get_action(board)
        return move

    def __str__(self):
        return "Human {}".format(self.player)


def run():
    n = 5
    width, height = 6, 6
    model_file = 'best_policy.model'
    try:
        board = Board(width, height, n_in_row=n)
        game = Game(board)

        best_policy = PolicyValueNet(width)

