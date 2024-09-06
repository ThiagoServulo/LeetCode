from collections import Counter

def judgeCircle(moves):
    c = Counter(moves)
    return c['U'] == c['D'] and c['R'] == c['L']

print(judgeCircle('UD')) # True