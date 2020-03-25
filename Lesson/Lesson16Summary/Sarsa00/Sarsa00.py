import pandas as pd
import numpy as np
import sys
sys.path.append('../../..')
from Lesson.Lesson16Summary.QLearning01.Maze import Maze


class RL(object):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.e_greedy = e_greedy
        self.q_table = pd.DataFrame(dtype=np.float64, columns=self.actions)

    def choose_action(self, observation):
        self.check_state_exist(observation)
        if np.random.uniform() < self.e_greedy:
            state_action = self.q_table.loc[observation, :]
            action = np.random.choice(state_action[state_action == np.max(state_action)].index)
        else:
            action = np.random.choice(self.actions)
        return action

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series([0] * len(self.actions), index=self.q_table.columns, name=state)
            )

    def learn(self, *args):
        pass


class QLearningTable(RL):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(QLearningTable,self).__init__(actions, learning_rate, reward_decay, e_greedy)

    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc(s, a)
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max
        else:
            q_target = r
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)


class SarsaTable(RL):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(SarsaTable,self).__init__(actions, learning_rate, reward_decay, e_greedy)

    def learn(self, s, a, r, s_, a_):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, a_]
        else:
            q_target = r
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)


def update():
    for episode in range(100):
        observation = env.reset()
        action = RL.choose_action(str(observation))
        while True:
            env.render()
            observation_, reward, done = env.step(action)
            action_ = RL.choose_action(str(observation_))
            RL.learn(str(observation), action, reward, str(observation_), action_)
            observation = observation_
            action = action_
            if done:
                break
    print('game over')
    env.destroy()


if __name__ == '__main__':
    env = Maze()
    RL = SarsaTable(actions=list(range(env.n_actions)))
    env.after(100,update)
    env.mainloop()
