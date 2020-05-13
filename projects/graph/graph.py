import time
"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self,vertices = {}):
        self.vertices = vertices

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            if self.vertices[v1] or self.vertices[v2]: 
                # I just need the compiler to check that both exist before I modify either
                pass
            self.vertices[v1].add(v2)
        except KeyError:
            print('one of the vertexes does not exist')
        # TODO Make it print the exact vertex that doesn't exist

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q  = [starting_vertex]
        seen = [starting_vertex]
        while len(q)>=1:
            neighbors = self.get_neighbors(q[0])
            for i in neighbors:
                if i in seen:
                    pass
                else:
                    q.append(i)
                    seen.append(i)
            del q[0] # can I use pop instead? would it be more efficient?/ pythonic?
        print(seen)
        return seen
        # TODO 
        # right now this algorithm doesn't scale. A hash table would help it scale
        # (the seen wouldn't take as long to complete)
        # The other way to improve this algorithm would be to see
        # if you can use pointers instead of the pop(0) operation.
        # if you can then it won't take as long to perform the "pop" from the q

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = [starting_vertex]
        seen = [starting_vertex]
        current = starting_vertex
        output = []
        while len(stack)>0:
            current = stack.pop()
            output.append(current)
            neighbors = self.get_neighbors(current)
            for i in neighbors:
                if i in seen:
                    pass
                else:
                    stack.append(i)
                    seen.append(i)
        print(output)
        return output
         # TODO refactor/ go over logic again.

    def dft_recursive(self, starting_vertex, seen= None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if seen == None: # first loop?
            seen = set()


        neighbors = self.get_neighbors(starting_vertex)
        no_new_neighbors = True
        for i in neighbors:
            if i in seen:
                pass
            else:
                no_new_neighbors = False
                break


        if no_new_neighbors:
            return seen, [starting_vertex] # [seen] [output]
        # if there are no neighbors, or 
        # if all the neighbors have been seen
        # return a value to the function above

        # else return the result of calling the d
        # function on 
        
        stack = [starting_vertex]
        seen.add(starting_vertex)
        for i in neighbors:
            if i in seen:
                pass
            else:
                seen.add(i)
                sub_seen, out = self.dft_recursive(i,seen)
                seen | sub_seen
                stack.extend(out)

        print(seen,stack)
        return seen, stack
        # TODO second pass on this algorithm to better understand it
        # track the points in time when the tradeoff of information occurs
        # between specific calls of the algorithm both down and up.

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # every time you extend teh region of breadth first search
        # have each node point to a parent. When you hit the thing you are looking
        # for trace parents to generate sequence.

        nbrs = self.get_neighbors(starting_vertex)
        dv = destination_vertex
        q = list(nbrs)
        parents = {}
        for i in q:
            parents[i] = starting_vertex
        # index = 0
        while len(q) > 0:
            current = q.pop(0)
            children = self.get_neighbors(current)
            for child in children:
                if child == dv:
                    parents[child] = current
                    q = []
                    break
                try:
                    if parents[child]:
                        continue
                except KeyError:
                    parents[child] = current
                    q.append(child)            
            # print(index,q,parents)
            # index += 1
            # time.sleep(1)
        sequence = [dv]
        current = dv
        while current != starting_vertex:
            current = parents[current]
            sequence.append(current)
        sequence.reverse()
        return sequence


        # maybe while neighbors isn't empty instead
        # for i in nbrs:
            # add its neighbors to the q
            # for each neighbor make the parent i (in the dictionary)
            # if one of the neibors is the dv 
            #     add to parents and break
            # current = next in q
            # get rid of first item in q  
        
        # outside while
        # reverse sequence =[]
        
        # while parents[dv] != starting_vertex
        #   parent = parents[dv]
        #   reverse seq.append(parent)
            # dv = parent
        pass
          # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        nbrs = self.get_neighbors(starting_vertex)
        dv = destination_vertex
        q = list(nbrs)
        parents = {}
        for i in q:
            parents[i] = starting_vertex
        # index = 0
        while len(q) > 0:
            current = q.pop()
            children = self.get_neighbors(current)
            for child in children:
                if child == dv:
                    parents[child] = current
                    q = []
                    break
                try:
                    if parents[child]:
                        continue
                except KeyError:
                    parents[child] = current
                    q.append(child)            
            # print(index,q,parents)
            # index += 1
            # time.sleep(1)
        sequence = [dv]
        current = dv
        while current != starting_vertex:
            current = parents[current]
            sequence.append(current)
        sequence.reverse()
        return sequence

        # keep track of current sequence
        # stack = []
        # sequence = []
        # current = starting_vertex
        # while True:
        #     if current == destination_vertex:
                
        #         break
        #     nbrs = self.get_neighbors(current)
            
        #     stack.extend(nbrs)
            
        #     current = stack.pop()

        # 
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, sequence=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if sequence == None:
            sequence = [starting_vertex]

        if starting_vertex == destination_vertex:
            return sequence
        
        nbrs = self.get_neighbors(starting_vertex)
        for nbr in nbrs:
            if nbr in sequence:
                continue
            tmp = sequence + [nbr]
            val = self.dfs_recursive(nbr,destination_vertex,tmp)
            # When I finally get a value I need to break out of the 
            # recursion so my normal case has to recognize that it 
            # should return the answer upwards
            # until its out of the recursion.
            if val == 0:
                continue
            else:
                return val
        return 0
        # if current == destination
        # return the sequence
        # else
        # traverse the tree on the neighbors you haven't seen.

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    seen,stack  = graph.dft_recursive(1)
    print(stack)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print('DFS recursive:',graph.dfs_recursive(1, 6))
    print(list(graph.get_neighbors(1)))
