def twocharacter(s):
    distinct_chars = set(s)
    max_length = 0
    for x in distinct_chars:
        for y in distinct_chars:
            if x != y:
                filtered = [z for z in s if z == x or z == y]
                if all(filtered[i] != filtered[i+1] for i in range(len(filtered)-1)):
                    max_length = max(max_length, len(filtered))
    return max_length