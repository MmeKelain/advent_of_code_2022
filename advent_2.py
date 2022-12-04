def day2_puzzle1(all_lines):
    score = 0
    rock = 1
    paper = 2
    scissors = 3
    for i in range(0, len(all_lines)):
        line = [y for y in all_lines[i]]
    if line[2] == 'X':
        score += 1
        if line[0] == 'A':
            score += 3
        elif line[0] == 'C':
            score += 6
    elif line[2] == 'Y':
        score += 2
        if line[0] == 'B':
            score += 3
        elif line[0] == 'A':
            score += 6
    elif line[2] == 'Z':
        score += 3
        if line[0] == 'C':
            score += 3
        elif line[0] == 'B':
            score += 6
    print(score)

def day2_puzzle2(all_lines):
    score = 0
    rock = 1
    paper = 2
    scissors = 3
    for i in range(0, len(all_lines)):
        line = [y for y in all_lines[i]]
    #print(line)
    # A is rock
    if line[0] == 'A':
        if line[2] == 'X':
            score += scissors
        elif line[2] == 'Y':
            score += (rock + 3)
        else:
            score += (paper + 6)
    elif line[0] == 'B': #B is paper
        if line[2] == 'X':
            score += rock
        elif line[2] == 'Y':
            score += (paper + 3)
        else:
            score += (scissors + 6)  
    elif line[0] == 'C': #C is scissors
        if line[2] == 'X':
            score += paper
        elif line[2] == 'Y':
            score += (scissors + 3)
        else:
            score += (rock + 6) 
    print(score)

def main():
    file = open("input.txt", 'r')
    all_lines = [line.strip() for line in file.readlines()]
    day2_puzzle1(all_lines)

if __name__ == "__main__":
    main()