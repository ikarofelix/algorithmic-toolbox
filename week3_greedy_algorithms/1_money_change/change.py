def change(money):
    # write your code here
    result = 0

    ten = int(money / 10)
    result += ten
    money -= 10 * ten

    five = int(money / 5)
    result += five
    money -= 5 * five

    result += int(money / 1)

    return result


if __name__ == '__main__':
    m = int(input())
    print(change(m))
