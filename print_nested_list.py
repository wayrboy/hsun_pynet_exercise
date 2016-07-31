def print_lol(the_list, indent=False, level=0):
# the default value of indent is False

    for each_item in the_list:
        if isinstance(each_item, list):
                print_lol(each_item, indent, level+1) # level = level + 1
        else:
            if indent: # if indent is needed
                for tab_cursor in range (0, level):
                    print " "*level,
            print (each_item)
            
test_list = ["Game of Thrones", 2016, ["David Benioff", "D.B. Weisss", ["Emelia Clarke", "Peter Dinklage", "Kit Harington"]]]

print_lol(test_list, True, 0)
