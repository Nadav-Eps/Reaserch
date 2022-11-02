import inspect


def f(x: int, y: float, z, k: int):
    return x + y + z + k

"""
checks that all the arguemnts that i got matches the arguemnts that the function i got demand
"""
def safe_call(f, **kwargs):
    f_params_dict = inspect.signature(f).parameters
    for arg in kwargs:
        if str(f_params_dict[arg].annotation) == "<class 'inspect._empty'>":
            continue
        if type(kwargs[arg]) != f_params_dict[arg].annotation:
            raise Exception("Sorry, the parameter  does not fit to his annotation. parameter: " + arg)
    return f(**kwargs)
print(safe_call(f, x=5, y=7.0, z=7 , k=1))


def breadth_first_search(start, end, f):
    """

    In this function we needed to use the four neighbors function we got to find a a poath from start to end without knowing what
    arguments we are going to get.
    unfurtennetly i didnt had time to finish this question so its just gets al the nodes that connects the wnd and start point
    but not the exactly path
    """
    visit = []
    prev = []
    visit.append(start)
    prev.append(start)
    while prev:
        tmp = prev.pop()
        neighbors = f(tmp)
        for nei in neighbors:
            if nei == end:
                visit.append(end)
                return visit
            if nei not in visit:
                visit.append(nei)
                prev.append(nei)

#didint had time for this question i am sorry hope there will be a chance to fix it
def print_sorted(data):
    print(sorted(data))
