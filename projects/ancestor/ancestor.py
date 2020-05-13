
def earliest_ancestor(ancestors, starting_node):
    # ancestors is a list of tuples
    # create the graph internally, and then
    # run an algorithm to 
    parents = {}
    for tup in ancestors:
        # child has parents __ 
        try:
            if parents[tup[1]]:
                parents[tup[1]].append(tup[0])
        except KeyError:
            parents[tup[1]] = []
            parents[tup[1]].append(tup[0])
    # print(parents)
    # this seems to be a common pattern
    # I want to check if a dictionary entry exists,
    # if it does do something
    # if it doesn't then do something else
    # the syntax is a bit wonky though.
    def _search(starting,max_depth=None):
        if max_depth == None:
            max_depth = 0

        try:
            curr_parents = parents[starting]
        except KeyError:
            max_depth += 1
            return max_depth, starting

        for i in curr_parents:
            longest,ancestor = _search(i,0)
            if longest < max_depth:
                continue
            elif longest == max_depth:
                # add to the list of possible ancestors 
                # we are going to select the min id from this
                # list at the end
                oldest_ancestors.append(ancestor)
            else: # longest > max_depth
                max_depth = longest
                oldest_ancestors = [ancestor]
        
        return max_depth+1, min(oldest_ancestors)

    try:
        if parents[starting_node]:
            longest, ancestor = _search(starting_node)
            return ancestor
    except KeyError:
        return -1

    
        # I've made a judgement on the longest sequence
        # from here + its ancestor
        # I want to return those two values for this branch
        # 
    # we might be able to do an internally recursive function?
    pass
    # TODO:
    # most efficient would be to have the algorithm embedded into the graph creation

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors,7))