def getData():
    with open("day4/input.txt", "r") as f:
        return [list(line) for line in f.read().splitlines()]


def part1(data):
    result = 0

    directions = [
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
    ]

    colomn_len = len(data)
    row_len = len(data[0])
    for y in range(colomn_len):
        for x in range(row_len):
            if data[y][x] != "@":
                continue

            roll_count = 0
            for direction in directions:
                dx, dy = direction
                nx, ny = x + dx, y + dy
                if 0 <= ny < colomn_len and 0 <= nx < row_len and data[ny][nx] == "@":
                    roll_count += 1

                if roll_count >= 4:
                    break

            if roll_count < 4:
                result += 1

    return result


def part2(data):
return 0                                                         
    grid = [list(line) for line in data]                             
    rows = len(grid)                                                 
    cols = len(grid[0]) if rows > 0 else 0                           
                                                                     
    total_removed = 0                                                
                                                                     
    while True:                                                      
        accessible = []                                              
                                                                     
        for r in range(rows):                                        
            for c in range(cols):                                    
                if grid[r][c] == '@':                                
                    adjacent_rolls = 0                               
                    for dr in [-1, 0, 1]:                            
                        for dc in [-1, 0, 1]:                        
                            if dr == 0 and dc == 0:                  
                                continue                             
                            nr, nc = r + dr, c + dc                  
                            if 0 <= nr < rows and 0 <= nc < cols:    
                                if grid[nr][nc] == '@':              
                                    adjacent_rolls += 1              
                                                                     
                    if adjacent_rolls < 4:                           
                        accessible.append((r, c))                    
                                                                     
        if not accessible:                                           
            break                                                    
                                                                     
        for r, c in accessible:                                      
            grid[r][c] = '.'                                         
                                                                     
        total_removed += len(accessible)                             
                                                                     
    return total_removed

def main():
    data = getData()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
