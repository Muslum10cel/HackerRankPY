def solve(n):
    return (n*(n+1)) // 2
  

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        number_of_person = int(input())
        print(solve(number_of_person - 1))
