def sort(input):
    for i in range(len(input)):
        min_index = i
        for j in range(i + 1, len(input)):
            if input[j] < input[min_index]:
                min_index = j
        input[i], input[min_index] = input[min_index], input[i]
