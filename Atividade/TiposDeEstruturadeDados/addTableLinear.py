# add in the last position
from array import array

from numpy import array

def add (arrays, value):
    length = len(arrays)
    tempArray = array('i',[0 for _  in range(length+1)]) #Array maior que o array inicial

    for i in range(0,length):
        tempArray[i] = array[i] #copiando o valor da matriz

    tempArray[length] = value
    return tempArray

def main():
    arrays = array ('i',[90,70,50,80,60,85])

    arrays = add(arrays,75)

    #imprimir
    length = len(arrays)
    for i in range(0,length):
        print(arrays[i], ',',end='')
if __name__ == '__main__':
    main()