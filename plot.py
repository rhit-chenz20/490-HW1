import argparse
from Model.plot import Plot

parser = argparse.ArgumentParser(description='Plot CSV result')
parser.add_argument('-out', '--outputFilename', type=str)
parser.add_argument('-files', '--filenames', type=str, nargs='*')
parser.add_argument('-d', '--debug', type = bool, default=False, required=False)
args = parser.parse_args()

model = Plot(
    filenames = args.filenames,
    output = args.outputFilename,
    debug = args.debug
)
