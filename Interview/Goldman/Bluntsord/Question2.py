import bisect


def count(teamA, teamB):
    teamA.sort()
    answer = []
    for score in teamB:
        curr = bisect.bisect_right(teamA, score)
        answer.append(curr)

    return answer