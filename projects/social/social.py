from random import shuffle

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        tmp = []
        for i in range(num_users):
            tmp.append(self.last_id)
            name = 'user ' + str(i)
            self.add_user(name)
        
        # Create friendships
        # figure out how to get a better distribution later
        shuffle(tmp)
        for i in self.users:
            shuffle(tmp)
            for j in tmp[:avg_friendships]:
                if i<j:
                    self.add_friendship(i,j)
            # print(i)
        


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # the dictionary has the format {'friend':'path'} with friend = user id
        # and path = list with path.
        # !!!! IMPLEMENT ME
        # a bfs guarantees shortest
        # if the friend is in visited ( aka if visited.__contains__(id))
        # then I don't have to travel to that particular place
        # else travel there, and add path

        # I need a list or a dictionary of branches that lists current pathways?
        # you can look up your parent, and your parent in the dictionary will 
        # have the sequence that you have to add to.
        # this is actually the visited dictionary
        nbrs = [user_id]
        nbrs.extend(self.friendships[user_id])
        current_path = []
        print(nbrs)
        visited[user_id] = user_id
        while len(nbrs)>0: 
            current = nbrs.pop(0)
            # if current in visited:# neighbor (current) in seen
            #    pass
            # else:
            current_friends = self.friendships[current]
            for i in current_friends:
                if i in visited:
                    pass
                else:
                    if type(visited[current]) is int:
                        visited[i] = [visited[current]] + [i]
                    else: # if list:
                        visited[i] = visited[current] + [i]
                    nbrs.extend(self.friendships[i])
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
