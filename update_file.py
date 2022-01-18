# обновляем старый файл до новой версии с помощью diff файла

print("Введите путь до первого файла")
path = input()

print("Введите путь до diff файла")
diffPath = input()   

oldFile = open(path, 'r')
oldVerion = oldFile.read()
oldFile.close()

diffFile = open(diffPath, 'r')
lastVerion = diffFile.read()
diffFile.close()

updatedData = list(oldVerion)

newLen = len(lastVerion)

# индекс в diff версии 
i = 0

# индекс в старой версии 
j = 0

while i < newLen:
    # замена
    if lastVerion[i] == '!' and i + 1 < newLen:
        updatedData.insert(j, lastVerion[i + 1])
        j += 1
        i += 3

    # вставка
    elif lastVerion[i] == '*' and i + 1 < newLen:
        updatedData[j] = lastVerion[i + 1]
        j += 1
        i += 3

    # удаление
    elif lastVerion[i] == '-':
        updatedData.pop(j)
        i += 1  

    # если просто буква, значит, она не изменялась
    else:
        j += 1
        i += 1
        continue    

diffFile = open("/home/darya/python-progs/diffFile.txt", "w+")        
        
oldFile = open(path, 'w')
oldFile.write(str(updatedData))
oldFile.close()
