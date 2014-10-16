# lst.append(item) returns None! (adds in place)
# use lst + [item] instead

def show_list(lst):
    print(lst)

def append_one_to_lst(lst):
    show_list(lst.append(1))

append_one_to_lst([1,2,3])

def add_one_to_lst(lst):
    show_list(lst + [1])

add_one_to_lst([10, 20, 30])
