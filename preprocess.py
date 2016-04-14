from time import sleep

import json

from settings import BASE_FILENAME, EDITIONS, STAGES


def get_html(edition, stage):
    filename = BASE_FILENAME.format(edition, stage)
    with open(filename) as input:
        return input.read()


def make_participant(html):
    props = html.split("<td>")
    props = [x.replace("<td>", "") for x in props]
    props = [x.replace("</td>", "") for x in props]
    props = [x.strip() for x in props]
    if "<th" in props[0]:
        return None
    # props[0] is garbage
    pos = int(props[1])
    if "a href" in props[2]:
        name = props[2][props[2].find('>')+1: props[2].rfind('<')]
    else:
        name = props[2] + " " + props[3]
    # We're trying to receive point in order to make sure it's correct order.
    points = int(props[-1])
    return name


def get_participant(html):
    assert isinstance(html, str)
    startindex = html.find("<tr")  # tag could have attributes
    if startindex == -1:
        raise ValueError("I should name errors better")
    startindex += 4
    endindex = html.find("</tr>", startindex)
    participant_html = html[startindex:endindex]
    rest_html = html[endindex:]
    try:
        result = make_participant(participant_html)
    except ValueError:
        return None, rest_html
    except IndexError:
        return None, rest_html
    return result, rest_html


def get_all_participants(html):
    for i in xrange(1000):
        try:
            result, html = get_participant(html)
            if result is not None:
                yield result
        except ValueError:
            pass


def main():
    res = {}
    for edition in EDITIONS:
        res[edition] = {}
        participant_results = {}
        for stage in STAGES:
            html = get_html(edition, stage)
            print edition, stage, "...",
            ranking = []
            for participant in get_all_participants(html):
                ranking.append(participant)
            res[edition][stage] = ranking
            print len(ranking)
    with open('data.json', 'w') as outfile:
        json.dump(res, outfile, indent=2)


if __name__ == "__main__":
    main()
