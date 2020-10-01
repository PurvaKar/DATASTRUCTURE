# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

from collections import deque
queue = deque([])

while(True):
    print("\nChoose 1.To Enqueue.")
    print("2.To dequeue.")
    print("3.Search an element in a queue.")
    print("4.View queue.")
    print("5.View queue and exit.")
    
    K = int(input("Choose an option between 1 to 5: "))
    
    if K==1:
        val = int(input("Enter value to be enqueued: "))
        queue.append(val)
        
    elif K==2:
        if len(queue)==0:
            print("Nothing to dequeue. Add something to queue!\n")
        else:
            queue.popleft()
        
    elif K==3:
        val = 0
        L = []
        search = int(input("Enter the value of element you want to search: "))
        for i in range(len(queue)):
            if queue[i] == search:
                if val==0:
                    val = val+1 
                    print("The element searched is present at positions:")
                L.append(i+1)
        print(*L)
                    
        if val == 0:
            print("Element you searched isn't present in the following queue!")
            
    elif K==4:
        print(*queue)
    
    elif K==5: 
        print(*queue)
        break
        
    else:
        print("Wrong input! Choose an input between 1 to 5.")