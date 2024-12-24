def print_door_mat(N, M):
    for i in range(1, N, 2):
        pattern = (".|." * i).center(M, "-")
        print(pattern)

    print("WELCOME".center(M, "-"))

    for i in range(N - 2, 0, -2):
        pattern = (".|." * i).center(M, "-")
        print(pattern)


N, M = map(int, input("enter numbers :").split())

if 5 < N < 101 and 15 < M < 303 and M == 3 * N:
    print_door_mat(N, M)
else:
    print("Invalid input. Please ensure N is odd, M = 3*N, and constraints are satisfied.")