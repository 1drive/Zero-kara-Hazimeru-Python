N, M = map(int, input().split())
DNA, distance, res = [], 0, ""
def most_frequent(data):
    return max(data, key=data.count)
for i in range(N):
    DNA.append(input().strip())
for j in range(M):
    tmp = []
    for k in range(N):
        tmp.append(DNA[k][j])
    tmp.sort()
    most_frequent_dna = most_frequent(tmp)
    distance += (N - tmp.count(most_frequent_dna))
    res = res + most_frequent_dna
print(res)
print(distance)