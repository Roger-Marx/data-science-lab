import argparse

parser = argparse.ArgumentParser("Meaw like a cat n times")
parser.add_argument("-n", default = 1, help = "number of times to meow", type = int)
args = parser.parse_args()


for _ in range(int(args.n)):
    print("meows parsed")