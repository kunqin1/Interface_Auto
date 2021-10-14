def pipei(target):
    nums = [1, 2, 7, 10]
    list = []
    for i in nums:
        num1 = i
        num2= i+1
        num= num1 +num2
        if num == target:
            list.append(i)
        else:
            i = i + 2
    print(list)


if __name__ == '__main__':
    pipei(9)
