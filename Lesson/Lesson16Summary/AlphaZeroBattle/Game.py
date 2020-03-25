from __future__ import print_function
import numpy as np


class Board(object):
    def __init__(self, **kwargs):
        self.width = int(kwargs.get('width', default=8))
        self.height = int(kwargs.get('height', default=8))
        self.states = {}
        self.n_in_row = int(kwargs.get('n_in_row'), 5)
        self.players = [1, 2]

    # 初始化所有可落子位置，初始化最初落子选手，初始化states，将last_move更新为-1
    def init_board(self, start_player=0):
        if self.width < self.n_in_row or self.height < self.n_in_row:
            raise Exception('board width and height can not be less than {0}'.format(self.n_in_row))
        self.current_player = self.players[start_player]
        self.availables = list(range(self.width * self.height))
        self.states = {}
        self.last_move = -1

    # 将数值型move转换为h，w location
    def move_to_location(self, move):
        h = move
        w = move % self.width
        return [h, w]

    # 将数组型数据location (3,5) 转换为数值型位置29
    def location_to_move(self, location):
        if len(location) != 2:
            return -1
        h = location[0]
        w = location[1]
        move = h * self.width + w
        if move not in range(self.width * self.height):
            return -1
        return move

    # 根据self.states，返回当前player的所有落子，返回对手player的所有落子，返回最后一步落子的位置
    def current_state(self):
        square_state = np.zeros((4, self.width, self.height))
        if self.states:
            moves, players = np.array(list(zip(*self.states.items())))
            move_curr = moves[players == self.current_player]
            move_oppo = moves[players != self.current_player]
            # 当前player状态
            square_state[0][move_curr // self.width, move_curr % self.height] = 1.0
            # 对手player状态
            square_state[1][move_oppo // self.width, move_oppo % self.height] = 1.0
            # 记录最后一步（落子）的位置
            square_state[2][self.last_move // self.width, self.last_move % self.height] = 1.0
        if len(self.states) % 2 == 0:
            square_state[3][:, :] = 1.0
        return square_state[:, ::-1, :]

    # 将self.states中move属性更新为当前选手id，将move从availables中移除，更新self.current_player, 更新self.last_move
    def do_move(self, move):
        self.states[move] = self.current_player
        self.availables.remove(move)
        self.current_player = (self.players[0] if self.current_player == self.players[1] else self.players[1])
        self.last_move = move

    # 单方下棋步数小于n时，认定无获胜方，
    def has_a_winner(self):
        width = self.width
        height = self.height
        states = self.states
        n = self.n_in_row

        moved = list(set(range(width * height)) - set(self.availables))

        if len(moved) < self.n_in_row * 2 - 1:
            return False, -1
        for m in moved:
            h = m // width
            w = m % width
            # 当前步是哪个棋手下的
            player = states[m]

            # 水平形成5子连环，获胜
            if (w in range(width - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n))) == 1):
                return True, player
            # 竖线形成5子连环，获胜
            if (h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * width, width))) == 1):
                return True, player
            # -45度斜线形成5子连环，获胜
            if (w in range(width - n + 1) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width + 1), width + 1))) == 1):
                return True, player
            # +45度斜线形成5子连环，获胜
            if (w in range(n - 1, width) and h in range(height - n + 1) and
                    len(set(states.get(i, -1) for i in range(m, m + n * (width - 1), width - 1))) == 1):
                return True, player

            return False, -1

    # 判断游戏是否结束，如有获胜者，游戏结束；没有可走位置，游戏结束；否则游戏没有结束
    def game_end(self):
        win, winner = self.has_a_winner()
        if win:  # 有获胜者，游戏结束
            return True, winner
        elif not len(self.availables):  # 没有可走的位置，游戏结束
            return True, -1
        return False, -1  # 游戏没有结束


class Game(object):
    def __init__(self, board, **kwargs):
        self.board = board

    # 绘制棋盘和棋子信息
    def graphic(self, board, player1, player2):
        width = board.width
        height = board.height
        print("Player", player1, "with X".rjust(3))
        print("Player", player2, "with O".rjust(3))
        print()
        for x in range(width):
            print("{0:8}".format(x), end='')
        print('\r\n')
        for i in range(height - 1, -1, -1):
            print("{0:4d}".format(i), end='')
            for j in range(width):
                loc = i * width + j
                p = board.states.get(loc, -1)
                if p == player1:
                    print('X'.center(8), end='')
                elif p == player2:
                    print('O'.center(8), end='')
                else:
                    print('_'.center(8), end='')
            print('\r\n\r\n')

    def start_play(self, player1, player2, start_player=0, is_shown=1):
        if start_player not in (0, 1):
            raise Exception('start_player should be either 0(player1 first) or 1 (player2 first')
        self.board.init_board(start_player)
        p1, p2 = self.board.players
        player1.set_player_ind(p1)
        player2.set_player_ind(p2)
        players = {p1: player1, p2: player2}
        if is_shown:
            self.graphic(self.board, player1.player, player2.player)
        while True:
            current_player = self.board.get_current_player()
            player_in_turn = players[current_player]
            move = player_in_turn.get_action(self.board)
            self.board.do_move(move)
            if is_shown:
                self.graphic(self.board, player1.player, player2.player)
            end, winner = self.board.game_end()
            if end:
                if is_shown:
                    if winner != -1:
                        print("game over, winner is ", players[winner])
                    else:
                        print("game over, equals")
                return winner

    def start_self_play(self, player, is_shown=0, temp=1e-3):
        self.board.init_board()
        p1, p2 = self.board.players
        states, mcts_probs, current_players = [], [], []
        while True:
            move, move_probs = player.get_action(self.board, temp, return_prob=1)
            states.append(self.board.current_state())
            mcts_probs.append(move_probs)
            current_players.append(self.board.current_player)
            self.board.do_move(move)
            if is_shown:
                self.graphic(self.board, p1, p2)
            end, winner = self.board.game_end()
            if end:
                winners_z = np.zeros(len(current_players))
                if winner != -1:
                    winners_z[np.array(current_players) == winner] = 1.0
                    winners_z[np.array(current_players) != winner] = -1.0
                player.reset_palyer()
                if is_shown:
                    if winner != -1:
                        print("game over, winner is ", winner)
                    else:
                        print("game over, equals")
                return winner, zip(states, mcts_probs, winners_z)
