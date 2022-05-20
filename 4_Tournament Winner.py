# Tournament Winner
# Given an array. Have to find the team having max point.
# Time O(n) Space O(k)

comp = [['HTML', 'C#'], ['C#', 'Python'], ['Python', 'HTML']]
results = [0, 0, 1]
scores = {}

for i in range(len(comp)):
    idx = results[i]
    if idx == 0:
        idx += 1
    else:
        idx -= 1
    temp = comp[i][idx]
    if temp not in scores:
        scores[temp] = 3
    else:
        scores[temp] += 3
print(max(scores))
