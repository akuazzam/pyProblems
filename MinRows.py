def minRows (hs):
    rowMins = [-1 for i in range (len (hs))] 
    rowCount = 0
    for num in hs:
        for i in range (len (rowMins)):
            if (rowMins[i] == -1):
                rowMins[i] = num
                rowCount +=1
                break
            elif (rowMins[i] > num):
                rowMins[i] = num
                break
    return rowCount
