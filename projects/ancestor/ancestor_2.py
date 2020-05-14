import sys
sys.path.append('G:\Data\Lambda\CS\Graphs\projects\graph')

from graph import Graph

a = Graph()

# for every node do a dfs where you start at start 
# and end at node
# take the longest sequence and the last value from the longest sequence
# that is the oldest ancestor



# or expose api interface to all sub sequences for a complete
# breadth first search of the graph starting from a specific node.
# take the longest sequence of the sequences and the end node is
# the oldest ancestor

# ^ would this api interface be useful for other graph operations?
# what do I think is valuable when traversing a graph?
# are sequences valuable or are lengths valuable, For sequences
# sometimes I want to collect a specific piece of information 
# from within the structure

# ex : a graph where every node has a value which itself is a object
# sometimes I want to move through the graph (dft or bft or dfs or bfs) 
# and collect a value from the object as I move through
# what if its a complex object
# how do I make the syntax at the high level easy for accessing the complex object?

# Treat an individual value and an object the same ( route individual values to a dummy object )
    # this way you don't have to do an if condition check for when you have a value as opposed
    # to an object containing a value?
    # all values are themselves objects in python so can I use . notation to get the value of a value?
# When you have multiple layers you can use dot notation/ chaining to specify
# if you need an algorithm that composes a result from the object create a function 
# on the object that returns this value
# if this value is accessed a lot then find out when to call the function (on what state changes 
# does the function need to be called) and call it internally and set the result as part of the 
# state of the object.

