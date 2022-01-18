def levenstein(firstString, secondString):
    n = len(firstString) + 1
    m = len(secondString) + 1
    matrix = [0] * n

    insertionCost = 1
    replaceCost = 1
    deletionCost = 1

    for i in range(0, n):
        matrix[i] = [0] * m
    for i in range(0, n):
        matrix[i][0] = i
    for j in range(0, m):
        matrix[0][j] = j   

    for i in range(1, n):
        for j in range(1, m):
            if firstString[i - 1] == secondString[j - 1]:
                replaceCost =  0
            else: 
                replaceCost =  1 
            matrix[i][j] = min(matrix[i][j - 1] + insertionCost,
                matrix[i - 1][j - 1] + replaceCost, matrix[i - 1][j] + deletionCost)

    return getDiffString(matrix, n, m, firstString, secondString)

def getDiffString(matrix, n, m, firstString, secondString):
    diffString = []
    currentValue = matrix[n - 1][m - 1]
    i = n - 1
    j = m - 1
    firstStringLen = len(firstString)
    secondStringLen = len(secondString)

    while (i > 0 and j > 0):
        prevStepInsert = matrix[i][j - 1] + 1
        prevStepDelete = matrix[i - 1][j] + 1
        prevStepReplace = matrix[i - 1][j - 1] + 1
        prevStep = min(prevStepInsert, prevStepDelete, prevStepReplace)

        # если предыдущее действие было заменой, берем соотв.символ второй строки
        if ((currentValue == prevStepReplace or currentValue < prevStepReplace) and prevStepReplace == prevStep):

            # проверяем, старый ли это символ или замена на новый, если старый, обозначаем его _, если новый, заключаем в *:
            if(currentValue == prevStepReplace - 1):
                diffString.insert(0, '_')
            else:
                newSymbol = "*" + secondString[j - 1] + "*"        
                diffString.insert(0, newSymbol)
            currentValue = matrix[i - 1][j - 1]
            i -= 1
            j -= 1

        # если предыдущее действие было удалением, ставим "-"
        elif (currentValue == prevStepDelete and prevStepDelete == prevStep):
            diffString.insert(0, "-")
            currentValue = matrix[i - 1][j]
            i -= 1

        # если предыдущее действие было вставкой нового символа, заключаем его в !
        elif (currentValue == prevStepInsert and prevStepInsert == prevStep):
            newSymbol = "!" + secondString[j - 1] + "!"
            diffString.insert(0, newSymbol)
            currentValue = matrix[i][j - 1]
            j -= 1

    # добавляем оставшийся текст
    if (i == 0):
        rest = secondString[:j]
        newString = []
        
        for i in rest:
            newString.append("!" + i + "!")

        if(len(rest)):
            diffString = newString + diffString

    return diffString, matrix[n - 1][m - 1]

print("Введите путь до первого файла")
path1 = input()

print("Введите путь до второго файла")
path2 = input()

firstFile = open(path1, 'r')
secondFile = open(path2, 'r')

firstString = firstFile.read()
secondString = secondFile.read()

diffString, diff = levenstein(firstString, secondString)

diffFile = open("diffFile.txt", "w+")
diffFile.write(''.join(diffString[:-1]))
diffFile.close() 
