from data.file import File
from problem.knapsack import Knapsack


def main():
    k = Knapsack("./data/datos.txt")
    l = [0] * 10
    l[3] = 1
    l[5] = 1
    print(l)
    print(k.get_weight(3))


if __name__ == "__main__":
    main()
