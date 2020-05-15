import time
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


def inv_direction(d):
    # returns n s opposites and e w opposites
    if d == 'n':
        return 's'
    elif d == 's':
        return 'n'
    elif d == 'w':
        return 'e'
    elif d == 'e':
        return 'w'
    else:
        print('error invalid direction')

def exits_to_dict(exits_list):
    # turns the list of exits to a dictionary of ?s
    out_dict = {}
    for i in exits_list:
        out_dict[i] = None
    return out_dict
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
import sys
import os
cwd = os.getcwd()
print(cwd)
os.chdir('G:\\Data\\Lambda\\CS\\Graphs\\projects\\adventure')
sys.path.append('G:\\Data\\Lambda\\CS\\Graphs\\projects\\adventure')
map_file = "main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# things to do in search loop
# move
# I have to add directions to traversal path
# get id
# update old room
# add current room (if not added yet) to the
# dictionary of rooms

# whenever you have ?s left in a room
# put it onto a stack of places to explore once you hit a dead end
# When you do hit a dead end aim towards one of the rooms
# with a question mark. (This way you are never aimless)
# If you hit a cycle and come back and fill out a question mark
# room then add it to a different list of completed rooms 
# whenever you pop an item off of the ?s stack then
# check to see if that room is in the 

# simpler strategy:
# backtrack on list (have a pointer to the sequence of instructions)
# until question. Then keep pointing to last question mark room
# keep a pointer to every question mark room.
total_rooms = len(world.rooms)
print("total rooms:",total_rooms)


my_room_graph = {}
traversal_stack = [] # point to the place on the movement list that contains last branch point
dead_ends = {} # add node + dead end direction
rmid = player.current_room.id
rmexits = player.current_room.get_exits()
rmexits_d = exits_to_dict(rmexits)

while len(my_room_graph) < total_rooms:
    # go down until you hit a dead eand
    # backtrack until you hit a room with ?s
    # go down till you hit doead end
    # backtrack
    # continue loop

    # if mode == down:
    #     while
    # else:
    #     while



    # if the room isn't in the room graph add it
    if my_room_graph.__contains__(rmid):
        pass
    else:
        my_room_graph[rmid] = rmexits_d

    # choose a direction to travel in:
    # choose the first direction that hasn't been explored yet.
    dead_end = True
    for i in my_room_graph[rmid]:
        if my_room_graph[rmid][i] == None:
            direction = i
            dead_end = False
            break

    # pointer = len(traversal_path)-1
    # if pointer < 0:
    #     pointer = 0

    while dead_end: # move in reverse direction
        # backtrack
        old_dir = traversal_stack.pop()
        direction = inv_direction(old_dir) 
        player.travel(direction)
        traversal_path.append(direction)
        rmid = player.current_room.id
        rmexits = player.current_room.get_exits()
        rmexits_d = exits_to_dict(rmexits)
        if dead_ends.__contains__(rmid):
            dead_ends[rmid][old_dir] = 1
        else:
            dead_ends[rmid] = rmexits_d
            dead_ends[rmid][old_dir] = 1
        for i in my_room_graph[rmid]:
            if my_room_graph[rmid][i] == None:
                direction = i
                dead_end = False
                break
        # once I start making different decisions between the pointers
        # and the dead end I flip a switch
        # and I ignore pointers. I just move along possible non-dead ends
        # till I hit something with none
        # if I hit something with no nones, and no possible places to explore
        # I get stuck. but I don't think this occurs unless you finish exploring, in which
        # case the outside while loop should take care of it/you shouldn't 
        # get stuck here forever
        # if dead_end: # if all of the directions were explored
        #     for i in dead_ends[rmid]:
        #         if dead_ends[rmid][i] == None:
        #             if # that direction matches the next pointer
        #             # then do nothing.
        #             else
        #             # set the new direction to explore
        #             direction = i
        #             player.travel(direction)
        #             traversal_path.append(direction)
        #             rmid = player.current_room.id
        #             rmexits = player.current_room.get_exits()
        #             rmexits_d = exits_to_dict(rmexits)

        #             if dead_ends.__contains__(rmid):
        #                 dead_ends[rmid][old_dir] = 1
        #             else:
        #                 dead_ends[rmid] = rmexits_d
        #                 dead_ends[rmid][old_dir] = 1
        #             dead_ends[rmid][i] = 1
        #             new_room = my_room_graph[rmid][i]
                    
        #             break
        # pointer -= 1

    

    player.travel(direction)
    traversal_path.append(direction)
    traversal_stack.append(direction)
    new_rmid = player.current_room.id
    my_room_graph[rmid][direction] = new_rmid
    if my_room_graph.__contains__(new_rmid):    
        my_room_graph[new_rmid][inv_direction(direction)] = rmid
    else:
        my_room_graph[new_rmid] = exits_to_dict(player.current_room.get_exits())
        my_room_graph[new_rmid][inv_direction(direction)] = rmid
    # print(len(all_visited))
    rmid = player.current_room.id
    rmexits = player.current_room.get_exits()
    rmexits_d = exits_to_dict(rmexits)
    # time.sleep(0.5)

# print(my_room_graph)
print(traversal_path)




#`player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)



# extension
# Keep a stack of "rooms with ?s" + a dictionary to get from here to that previous room
# so as you travel you "leave behind" a trail.

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
