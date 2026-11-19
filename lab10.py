def eval_rpn(tokens):
    """ 
    Create a empty stack, 
    put each number in the stack in order of how they have been typed in, 
    then then you see an oparator then "pop" from the stack twice and use that operater on the stack, 
    then store tha number back into the stack, the stack can be implimented as a list. """

    stack = []

    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)

            stack.append(result)

        else:
            stack.append(int(token))

    return stack.pop()


def decode_string(s):
    """
    Create an empty stack, an empty current_string and set current_number to 0,
    loop through each character in the string, if the character is a number store
    it in current_number, if the character is "[" push the current number and
    string onto the stack then reset them, if the character is a letter add it
    to current_string, if the character is "]" pop the previous number and string
    from the stack, repeat current_string by the popped number and add it to the
    previous string, once the loop is finished return current_string.
    """

    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)

        elif char == "[":
            stack.append((current_number, current_string))
            current_number = 0
            current_string = ""

        elif char == "]":
            previous_number, previous_string = stack.pop()
            current_string = previous_string + current_string * previous_number

        else:
            current_string += char

    return current_string


def daily_temperatures(temps):
    """
    Create an empty stack and a results list filled with zeros,
    loop through each temperature using its index, while the stack
    is not empty and the current temperature is warmer than the
    temperature at the index on top of the stack, pop that index
    from the stack, calculate the number of days waited by
    subtracting the previous index from the current index,
    store that number in the results list at the previous index,
    then push the current index onto the stack, once the loop
    is finished return the results list.
    """

    stack = []
    result = [0] * len(temps)

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            previous_index = stack.pop()
            result[previous_index] = i - previous_index

        stack.append(i)

    return result


def num_islands(grid):
    """
    Create an empty set to keep track of visited land cells and set the
    island count to 0, loop through each row and column in the grid,
    if the current cell is land ("1") and has not been visited,
    increase the island count by 1, create a stack containing the
    current cell and mark it as visited, while the stack is not empty
    pop a cell from the stack, check the cells above, below, left
    and right of it, if a neighbouring cell is inside the grid,
    contains land and has not been visited, add it to the stack
    and mark it as visited, once all connected land has been
    explored continue checking the grid, return the island count.
    """

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    island_count = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == "1" and (r, c) not in visited:
                island_count += 1

                stack = [(r, c)]
                visited.add((r, c))

                while stack:
                    row, col = stack.pop()

                    directions = [
                        (1, 0),
                        (-1, 0),
                        (0, 1),
                        (0, -1)
                    ]

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if (0 <= new_row < rows and
                            0 <= new_col < cols and
                            grid[new_row][new_col] == "1" and
                            (new_row, new_col) not in visited):

                            stack.append((new_row, new_col))
                            visited.add((new_row, new_col))

    return island_count


def main():
    pass


if __name__ == "__main__":
    main()
