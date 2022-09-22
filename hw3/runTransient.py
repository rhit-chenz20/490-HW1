import argparse
from Model.model import Model

parser = argparse.ArgumentParser(description='Start female mating simulation')
parser.add_argument('-width', '--width', type=int)
parser.add_argument('-state', '--state', type=str, default="-1", required=False)
parser.add_argument('-duration', '--duration', type=int)
parser.add_argument('-rule', '--rule', type=int)
parser.add_argument('-fn', '--filename', type=str)
parser.add_argument('-d', '--debug', type = bool, default=False, required=False)
parser.add_argument('-seed', '--seed', type = float, default=-1, required=False)
args = parser.parse_args()

model = Model(
    args=args
)
averageTrans = 0.0
for k in range(100):
    model.start()
    if (model.transientDurFound):
        averageTrans += float(model.transientDur)
    else:
        averageTrans += 1000.0
    model = Model(
        args=args
        )
averageTrans = averageTrans/100.0
print(averageTrans)
