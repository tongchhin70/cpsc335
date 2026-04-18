def escape_maze(maze, start, end):
    # queue stores: ((row, col), distance_from_start)
    queue = [(start, 0)]
    
    # visited keeps track of cells we've already explored
    visited = set()
    visited.add(start)
    
    while queue:
        # get the next position to explore
        current_position, distance = queue.pop(0)
        if current_position == end:
            return distance
        
        x, y = current_position
        # possible moves: down, up, right, left
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        
        for (nx, ny) in neighbors:
            # check:
            # 1. inside maze
            # 2. not a wall
            # 3. not already visited
            if (0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and
                maze[nx][ny] == 0 and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append(((nx, ny), distance + 1))
    return -1


if __name__ == "__main__":
    maze1 = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    print(escape_maze(maze1, (0, 0), (3, 3)))  # Output: 6

    maze2 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    print(escape_maze(maze2, (0, 0), (2, 2)))  # Output: -1
    
    maze3 = [
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0]
    ]
    print(escape_maze(maze3, (0, 0), (5, 5))) # Output: 10
