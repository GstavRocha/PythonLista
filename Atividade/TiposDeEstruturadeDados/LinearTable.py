# Linear Table, relationship  one by one.

# Exemple:
from array import array

def main():
    arrays = array('i',[90,70,80,60,85]) # Crie uma matriz do tipo inteiro

    length = len(arrays) #comprimento

    for i in range (0,length):
        print(arrays[i], ",", end="")
if __name__ == "__main__":
    main()

#pg 5