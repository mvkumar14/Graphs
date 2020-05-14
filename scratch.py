try:
    #dictionary access
    if test_dict[val]:
        # do A
        pass
except KeyError:
    # else do B
    pass



hasattr(test_dict,val)

# if the entry exists in the dictionary
    # do A
# else 
    # do B