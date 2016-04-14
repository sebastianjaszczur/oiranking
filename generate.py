from scipy.stats.stats import pearsonr
import json
from pprint import pprint
import matplotlib.pyplot as plt

from settings import EDITIONS


def get_data():
    with open('data.json') as data:
        d = json.load(data)
        return d


def get_chart_points(edition, stage1, stage2):
    oi = get_data()[edition]
    rank1 = oi[stage1]
    rank2 = oi[stage2]
    # We'd better do deduplication.
    rank1 = [name for name in rank1 if rank1.count(name) == 1]
    rank2 = [name for name in rank2 if rank2.count(name) == 1]

    rank1 = [name for name in rank1 if name in rank2]
    rank2 = [name for name in rank2 if name in rank1]

    assert len(rank1) == len(rank2)
    size = len(rank1)
    points = []
    for pos, name in enumerate(rank1):
        no1 = float(size - pos) / size
        no2 = float(size - rank2.index(name)) / size
        points.append((no1, no2))
    return points


def gen_chart(points, stage1, stage2):
    p0 = [p[0] for p in points]
    p1 = [p[1] for p in points]
    plt.scatter(p0, p1)
    plt.xlabel("Miejsce w {} etapie".format(stage1))
    plt.ylabel("Miejsce w {} etapie".format(stage2))
    plt.title("{}->{} etap; ".format(stage1, stage2) + "korelacja: " + str(pearsonr(p0, p1)[0]))
    plt.grid(True)
    plt.show()


def main():
    points = []
    stage1 = "2"
    stage2 = "3"
    for edition in EDITIONS:
        points.extend(get_chart_points(str(edition), stage1, stage2))
    gen_chart(points, stage1, stage2)


if __name__ == "__main__":
    main()
