

K = int(input())
L = int(input())
M = int(input())
N = int(input())

counter = 0

for i in range(K, 9, ):
    for j in range(L, 8, -2):
        for x in range(M, 9,):
            for y in range(N, 8, -2):
                if i == x and j == y:
                    print("Cannot change the same player.")
                    continue
                print(f"{i}{j} - {x}{y}")
                counter += 1
                if counter == 6:
                    break