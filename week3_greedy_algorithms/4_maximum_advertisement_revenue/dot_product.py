def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    
    for i in range(len(first_sequence)):
        maxFirstIndex = first_sequence.index(max(first_sequence))
        maxSecondIndex = second_sequence.index(max(second_sequence))

        max_product += first_sequence[maxFirstIndex] * second_sequence[maxSecondIndex]

        del first_sequence[maxFirstIndex]
        del second_sequence[maxSecondIndex]
    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
