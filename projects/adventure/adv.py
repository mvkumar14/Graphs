import time
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


def inv_direction(direction):
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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
total_rooms = len(world.rooms)
print("total rooms:",total_rooms)

all_visited  = []
my_room_graph = {}
while len(all_visited) < 500:
    rmid = player.current_room.id
    rmexits = player.current_room.get_exits()

    # I have to change rmexits into dictionary format
    # and have all the keys be ? if its a brand new room

    # move the starting to before the loop starts. 
    if my_room_graph.__contains__(rmid):
        pass
    else:
        my_room_graph[rmid] = rmexits
    
    print(my_room_graph)
    
    if rmid in all_visited:
        pass
    else:
        all_visited.append(rmid)

    # choose a direction to travel in:
    random.sample()

    player.travel(direction)
    traversal_path.append(direction)
    new_rmid = player.current_room.id
    my_room_graph[rmid][direction] = new_rmid
    if my_room_graph.__contains__(new_rmid):    
        my_room_graph[new_rmid][inv_direction(direction)] = rmid
    else:
        my_room_graph[new_rmid] = player.current_room.get_exits()
        my_room_graph[new_rmid][inv_direction(direction)] = rmid
    time.sleep(0.5)




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
