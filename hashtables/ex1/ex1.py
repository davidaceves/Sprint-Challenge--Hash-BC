#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

weights = [4, 6, 10, 15, 16]
answerArray = []

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    firstIndex = None
    secondIndex = None

    for i, key in enumerate(weights):
        hash_table_insert(ht, key, i)
    
    for i, key in enumerate(weights):
        diff = limit - key
     
        if hash_table_retrieve(ht, diff):
            firstIndex = i
            secondIndex = hash_table_retrieve(ht, diff)

    if firstIndex and secondIndex is not None and firstIndex >= secondIndex:
        answerArray.append(str(firstIndex))
        answerArray.append(str(secondIndex))
        
    elif firstIndex <= secondIndex: 
        answerArray.append(str(secondIndex))
        answerArray.append(str(firstIndex))
    else:
       return None
          
        

    


def print_answer(answer):
    if answerArray == []:
        print("None")
    elif answer is not None:
        print(str(answer[0] + " " + answer[1]))
    
get_indices_of_item_weights(weights, 5, 21)
print_answer(answerArray)