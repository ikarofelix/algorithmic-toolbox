def Fibonnacci(n):
    F = [0] * n

    if n != 1 and n != 0:
        F[1] = 1
        for i in range(2, n):
            F[i] = F[i - 1] + F[i - 2]
    
    return F[:n]

if __name__ == "__main__":
    number = 3
    result = Fibonnacci(number)
    print(result)