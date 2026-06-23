n = [1,2,3,4,5,6]  #Initial list
n.append(10) # adds 10 to the end
n.insert(2,15) # insert 15 at index 2
n.extend([20,25,30]) # add multiple elemets at the end
n.remove(5) # remove the first occurance of 5
Popped_item = n.pop() # removes and stores the element at index 3
Index = n.index(5) #finds the index of 6
Count_5 = n.count(5) #counts occurrences of 5
n.sort() #sort the list in assending order
n.reverse() #reverse the list order
New_n = n.copy() #creates a copy of the list
n.clear() #remove all the elements from the list
n.index(3)
#lists skower but more powerful than tuple