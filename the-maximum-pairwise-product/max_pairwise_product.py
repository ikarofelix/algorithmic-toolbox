def max_pairwise_product(numbers):
    n = len(numbers)
    first = 0
    second = 1

    for i in range(n):
        if numbers[i] > numbers[first] and i != second:
            first = i
        
    for i in range(n):
        if numbers[i] > numbers[second] and i != first:
            second = i

    return numbers[first] * numbers[second]

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))