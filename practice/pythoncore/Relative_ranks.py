# Relative Ranks
def ranks(score):
    # Create a sorted copy of the score list in descending order
    sorted_score = sorted(score, reverse=True)

    # Map each score to its rank
    rank_map = {}
    for i, s in enumerate(sorted_score):
        if i == 0:
            rank_map[s] = "Gold Medal"
        elif i == 1:
            rank_map[s] = "Silver Medal"
        elif i == 2:
            rank_map[s] = "Bronze Medal"
        else:
            rank_map[s] = str(i + 1)

    result = [rank_map[s] for s in score]
    return result


if __name__ == "__main__":
    score = [10,3,8,9,4]
    res = ranks(score)
    print(res)
