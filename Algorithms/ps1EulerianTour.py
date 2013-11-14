# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    tour = []
    for start_node in graph:
        start = start_node[0]
        i = start_node[1]
        tour.append(start)
        while i < len(graph) and (graph[i][1] not in tour or graph[i][1] == start):
            if graph[i][1] == start:
                tour.append(start)
                return tour
            else:
                tour.append(graph[i][1])
                i = graph[i][1] -1
        if len(tour) > 1:
            return tour
            
print find_eulerian_tour([(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)])