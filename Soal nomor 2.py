import time


def tsp(graph, start):
    num_cities = len(graph)
    unvisited_cities = [i for i in range(num_cities)]
    unvisited_cities.remove(start)

    current_city = start
    path = [current_city]
    total_distance = 0

    while unvisited_cities:
        next_city = None
        min_distance = float('inf')

        for city in unvisited_cities:
            if graph[current_city][city] < min_distance:
                next_city = city
                min_distance = graph[current_city][city]

        if next_city is None:
            return "Tidak ada jalur yang mungkin"

        path.append(next_city)
        total_distance += min_distance
        unvisited_cities.remove(next_city)
        current_city = next_city

    path.append(start)
    total_distance += graph[current_city][start]

    return path, total_distance


def dijkstra(graph, start, end):
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    distances[start] = 0

    shortest_paths = {start: [start]}
    unvisited_nodes = [i for i in range(num_nodes)]

    while unvisited_nodes:
        min_distance = float('inf')
        next_node = None

        for node in unvisited_nodes:
            if distances[node] < min_distance:
                min_distance = distances[node]
                next_node = node

        if next_node is None:
            break

        unvisited_nodes.remove(next_node)

        for neighbor in range(num_nodes):
            if graph[next_node][neighbor] != 0:
                distance = min_distance + graph[next_node][neighbor]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    shortest_paths[neighbor] = shortest_paths[next_node] + [neighbor]

    shortest_path = shortest_paths[end]
    total_distance = distances[end]

    return shortest_path, total_distance


def print_graph(graph):
    for row in graph:
        print(row)


def compute_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time

    return result, elapsed_time


def analyze_worst_case_tsp(num_cities):
    # Generate worst case graph for TSP
    graph = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                graph[i][j] = 1

    start_city = 0
    result, elapsed_time = compute_time(tsp, graph, start_city)

    print("Worst Case TSP:")
    print("Number of Cities:", num_cities)
    print("Path:", result[0])
    print("Total Distance:", result[1])
    print("Computation Time:", elapsed_time, "seconds")


def analyze_best_case_tsp(num_cities):
    # Generate best case graph for TSP
    graph = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(i+1, num_cities):
            graph[i][j] = j - i

    start_city = 0
    result, elapsed_time = compute_time(tsp, graph, start_city)

    print("Best Case TSP:")
    print("Number of Cities:", num_cities)
    print("Path:", result[0])
    print("Total Distance:", result[1])
    print("Computation Time:", elapsed_time, "seconds")


def analyze_average_case_tsp(num_cities):
    # Generate average case graph for TSP
    graph = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                graph[i][j] = abs(i - j) + 1

    start_city = 0
    result, elapsed_time = compute_time(tsp, graph, start_city)

    print("Average Case TSP:")
    print("Number of Cities:", num_cities)
    print("Path:", result[0])
    print("Total Distance:", result[1])
    print("Computation Time:", elapsed_time, "seconds")


if __name__ == '__main__':
    graph = [
        [0, 2, 9, 10, 5],
        [2, 0, 4, 8, 6],
        [9, 4, 0, 3, 7],
        [10, 8, 3, 0, 12],
        [5, 6, 7, 12, 0]
    ]

    print("Graph:")
    print_graph(graph)

    while True:
        print("\nOptions:")
        print("1. TSP (Traveling Salesman Problem)")
        print("2. Dijkstra (Shortest Path)")
        print("3. Analyze Worst Case TSP")
        print("4. Analyze Best Case TSP")
        print("5. Analyze Average Case TSP")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            start_city = int(input("Enter the starting city: "))

            result, elapsed_time = compute_time(tsp, graph, start_city)

            print("\nIterations:")
            for i in range(len(result[0]) - 1):
                print("Iteration", i+1)
                print("Path:", result[0][:i+1])
                print("Total Distance:", result[1])

            print("\nTSP Result:")
            print("Shortest Path:", result[0])
            print("Total Distance:", result[1])
            print("Computation Time:", elapsed_time, "seconds")

        elif choice == '2':
            start_city = int(input("Enter the starting city: "))
            end_city = int(input("Enter the destination city: "))

            result, elapsed_time = compute_time(dijkstra, graph, start_city, end_city)

            print("\nDijkstra Result:")
            print("Shortest Path:", result[0])
            print("Total Distance:", result[1])
            print("Computation Time:", elapsed_time, "seconds")

        elif choice == '3':
            num_cities = int(input("Enter the number of cities: "))
            analyze_worst_case_tsp(num_cities)

        elif choice == '4':
            num_cities = int(input("Enter the number of cities: "))
            analyze_best_case_tsp(num_cities)

        elif choice == '5':
            num_cities = int(input("Enter the number of cities: "))
            analyze_average_case_tsp(num_cities)

        elif choice == '0':
            break

        else:
            print("Invalid choice. Please try again.")
