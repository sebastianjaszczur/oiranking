import random
import urllib2
import time

from settings import BASE_FILENAME, BASE_URL, EDITIONS, STAGES


def get_ranking(edition, stage):
    response = urllib2.urlopen(BASE_URL.format(edition, stage))
    html = response.read()
    return html


def save_ranking(edition, stage, html):
    filename = BASE_FILENAME.format(edition, stage)
    with open(filename, "w") as output:
        output.write(html)


def download_ranking(edition, stage):
    html = get_ranking(edition, stage)
    save_ranking(edition, stage, html)


def main():
    for edition in EDITIONS:
        for stage in STAGES:
            print "EDITION", edition, "STAGE", stage, "...",
            download_ranking(edition, stage)
            print "OK"
            time.sleep(random.uniform(0.0, 0.2))


if __name__ == "__main__":
    main()