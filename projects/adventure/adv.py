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
map_file = "test_loop_fork.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

#depth first tree.
stack = [player.current_room]
seen = [player.current_room.id]
current = player.current_room.id

while len(stack)>0:
    current = stack.pop()
    nbrs = current.get_exits()
    print(nbrs)
    for i in nbrs
    for i in nbrs:
        if i in seen:
            pass
        else:
            stack.append(current.get_room_in_direction(i))
            seen[current.id] = 





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