An explanation of the code. 


# Node

Pretty standard data structure to manage data in linked lists. 

# DoubleLinkedList

Pretty standard just followed the expected logic for it. 

# division_hash

This hash determines where to put the new value by taking the key and dividing by the size. The issue with this is that certain key/size pairs can casue issues where there's too much data clustering

# Data Clustering

When 2+ nodes have the same position assigned to them, it creates a list of items at that node. This is fine if it's more uniform but becomes a tragedy when there's a huge cluster on accident.


# multiplication_hash

multiplication hash on the other hand is moreso using a constant A which we get from a math formula we determine to get an irrational number. Then you take just the int value (flooring it effectively) of the calculation we make to then determine the spot. 

This being more random helps with the hashtable being more uniformly distributed. 

# HashTable

### init

Takes in the initial capacity and hashfunc that the user wants 
- defaults to 8 and multiplication_hash respectively

creates "buckets" of Nodes which is a list of DoublyLinkedList

### resize

what it seems like. 
takes in the new capacity
takes the old items to a temp
creates a new bucket space 
puts the temp bucket items into the new bucket


### delete

find the index we're looking for 
get the bucket we're looking for
delete the key and if the operation works, 
then reduce the size 
sometimes reducing the size by half if needed.


### insert

find the index
find the bucket
if the item doesn't already exist in the bucket,
increase current size by 1
else, delete the existing key and keep the size the same
insert the key into the doublylinkedlist 
multiply the capacity by 2 if the current size is greater than our current expected capacity

### search

gets the index we need
returns the exact value in the bucket we're looking for if it exists 

### display

Just listing out the buckets, their position and the value in them. 

