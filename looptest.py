N = 3
for i in range(N):
    for j in range(N):
        if j == N - 1:
            print("Prins", end=" ")
        else:
            print("Markó", end=" ")

        if i == N - 1:
            print("Antóníus")
        else:
            print("Póló")
