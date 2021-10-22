graph = {}
def add_v(v):
    if v in graph:
        print("V exists")
    else:
        graph.update({v:[]})


add_v(5)
print(graph)


