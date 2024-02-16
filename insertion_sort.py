def sort(input):
    for i in range(1, len(input)):
        key = input[i]
        j = i - 1
        while j >= 0 and key < input[j]:
            input[j + 1] = input[j]
            j -= 1
        input[j + 1] = key
