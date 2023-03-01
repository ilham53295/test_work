def alternatingcharacter(a):
    deletion = 0
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            deletion += 1
    return deletion