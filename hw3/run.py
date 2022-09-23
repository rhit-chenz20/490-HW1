import argparse
from Model.model import Model

parser = argparse.ArgumentParser(description='Start female mating simulation')
parser.add_argument('-width', '--width', type=int)
parser.add_argument('-percentageAlive', '--percentage', type = float, default=10, required=False)
parser.add_argument('-heightFor2D', '--height', type=int)
parser.add_argument('-state', '--state', type=str, default="-1", required=False)
parser.add_argument('-duration', '--duration', type=int)
parser.add_argument('-rule', '--rule', type=int)
parser.add_argument('-fn', '--filename', type=str)
parser.add_argument('-d', '--debug', type = bool, default=False, required=False)
parser.add_argument('-seed', '--seed', type = float, default=-1, required=False)
parser.add_argument('-dimen', '--dimension', type = int, default = 1, required=False)
args = parser.parse_args()

model = Model(
    args=args
)

model.start()

