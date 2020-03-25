import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np


def set_learning_rate(optimizer, lr):
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

# 策略网络模型
class Net(nn.Module):
    def __init__(self, board_width, board_height):
        super(Net,self).__init__()

        self.board_widht =board_width
        self.board_height = board_height
        # 通用层 common layers
        self.conv1 = nn.Conv2d(4, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        # 行动策略组 action policy layers
        self.act_conv = nn.Conv2d(128, 4, kernel_size=1)
        self.act_fc1 = nn.Linear(4 * board_width * board_height, board_width * board_height)
        # 状态值层 state value layers
        self.val_conv1 = nn.Conv2d(128, 2, kernel_size=1)
        self.val_fc1 = nn.Linear(2 * board_width * board_height, 64)
        self.val_fc2 = nn.Linear(64, 1)

    def forward(self, state_input):
        # 通用层 common layers
        x = F.relu(self.conv1(state_input))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        # 行动策略组
        x_act = F.relu(self.act_conv1(x))
        x_act = x_act.view(-1, 4 * self.board_widht * self.board_height)
        x_act = F.log_softmax(self.act_fc1(x_act))
        # 状态值层
        x_val= F.relu(self.val_conv1(x))
        x_val = x_val.view(-1, 2 * self.board_widht * self.board_height)
        x_val = F.relu(self.val_fc1(x_val))
        x_val = F.tanh(self.val_fc2(x_val))
        # 输出行动可能性 和 终局的预期状态值
        return x_act, x_val


class PolicyValueNet():
    def __init__(self, board_width, board_height, model_file=None, use_gpu=False):
        self.use_gpu = use_gpu
        self.board_width = board_width
        self.board_height = board_height
        self.l2_const = 1e-4
        # 设置策略网络参数
        if self.use_gpu:
            self.policy_value_net = Net(board_width, board_height).cuda()
        else:
            self.policy_value_net = Net(board_width, board_height)
        self.optimizer = optim.Adam(self.policy_value_net.parameters())

        if model_file:
            net_params = torch.load(model_file)
            self.policy_value_net.load_state_dict(net_params)

    def policy_value(self, state_batch):
        if self.use_gpu:
            state_batch = Variable(torch.FloatTensor(state_batch).cuda())
            log_act_probs, value = self.policy_value_net(state_batch)
            act_probs = np.exp(log_act_probs.data.cpu().numpy())
            return act_probs, value.data.numpy()

    def policy_value_fn(self, board):
        legal_positions = board.availables
        current_state =
