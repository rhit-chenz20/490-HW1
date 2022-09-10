import argparse
from Model.model import Model

parser = argparse.ArgumentParser(description='Start female mating simulation')
parser.add_argument('-size', '--size', type=int, default=100, required=False)
parser.add_argument('-length', '--genomeLength', type=int)
parser.add_argument('-mutateR', '--mutationRate', type=float)
parser.add_argument('-points', '--pointSize', type=int)
parser.add_argument('-prange', '--pointRange', type=int)
parser.add_argument('-max', '--maxGeneration', type=int, default=200, required=False)
parser.add_argument('-e', '--elitism', type=int, default=0, required=False)
parser.add_argument('-sel', '--selection', type=int, default=0, required=False)
parser.add_argument('-fit', '--fitnessFunction', type=int, default=0, required=False)
parser.add_argument('-fn', '--filename', type=str)
parser.add_argument('-per', '--topPercent', type = float, default=0.5, required=False)
parser.add_argument('-c', '--crossover', type = int, default=0, required=False)
parser.add_argument('-d', '--debug', type = bool, default=False, required=False)
parser.add_argument('-seed', '--seed', type = float, default=-1, required=False)
parser.add_argument('-n', '--num_parent', type = int, default=2, required=False)
args = parser.parse_args()

model = Model(
    args=args
)

model.start()
