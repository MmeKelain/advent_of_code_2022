def create_crates_set():
    '''
    The crates for the test input:
        [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3 
    '''
    #all_col = {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}
    '''
    The crates for the actual input:
        [P]                 [C] [C]    
        [W]         [B]     [G] [V] [V]
        [V]         [T] [Z] [J] [T] [S]
        [D] [L]     [Q] [F] [Z] [W] [R]
        [C] [N] [R] [H] [L] [Q] [F] [G]
    [F] [M] [Z] [H] [G] [W] [L] [R] [H]
    [R] [H] [M] [C] [P] [C] [V] [N] [W]
    [W] [T] [P] [J] [C] [G] [W] [P] [J]
     1   2   3   4   5   6   7   8   9 
    '''
    all_col = {1: ['W', 'R', 'F'], 2: ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'], \
    3: ['P','M','Z','N','L'], 4: ['J','C','H','R'], 5: ['C','P','G','H','Q','T','B'], \
    6: ['G','C','W','L','F','Z'], 7: ['W','V','L','Q','Z','J','G','C'], \
    8: ['P','N','R','F','W','T','V','C'], 9: ['J','W','H','G','R','S','V']}
    return all_col
   
def day5_puzzle1(file, all_col):
    move_list = []
    num_col = 9
    # Part 1; use pop() to get the top crate
    for line in file.readlines():
        if "move" in line:
            move_list.append([int(i) for i in line.split() if i.isdigit()])
        else:
            continue
    #print(move_list)
    for direction in move_list:
        # format move [0] (number to move) from [1] (column) to [2] (column)
        from_col = direction[1]
        to_col = direction[2]
        num_to_move = direction[0]
        for i in range(num_to_move):
            curr_crate = all_col[from_col].pop()
            all_col[to_col].append(curr_crate)

    solution_list = ""
    for i in range(1, num_col+1):
        solution_list += all_col[i].pop()
    print(solution_list)

def day5_puzzle2(file, all_col):
    # Part 2; use slices to move crates from list to list
    for direction in move_list:
        # format move [0] (number to move) from [1] (column) to [2] (column)
        from_col = direction[1]
        to_col = direction[2]
        num_to_move = direction[0]
        end_len = len(all_col[from_col])
        s = slice(end_len-num_to_move, end_len)
        all_col[to_col].extend(all_col[from_col][s])
        for i in range(num_to_move):
            all_col[from_col].pop()
    #print(all_col)
    solution_list = ""
    for i in range(1, num_col+1):
        solution_list += all_col[i].pop()
    print(solution_list)

def main():
    file = open("input.txt", 'r')
    # 9 stacks of crates in puzzle, 3 in sample data
    all_col = create_crates_set()
    day5_puzzle1(file, all_col)
    day5_puzzle2(file, all_col)


if __name__ == "__main__":
    main()