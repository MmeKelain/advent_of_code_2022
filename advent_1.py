def day1_puzzle1(cals):
    current_sack = 0
    all_sacks = []
    for i in cals:
        if i != '/n':
            current_sack += i
        else:
            all_sacks.append(current_sack)
            current_sack = 0
    all_sacks.sort(reverse=True)
    print(all_sacks[0])
    return(all_sacks)

def day1_puzzle2(all_sacks):
    print(sum(all_sacks[:2]))

def main():
    file = open("input.txt", 'r')
    cals = [line.strip() for line in file.readlines()]
    all_sacks = day1_puzzle1(cals)
    day1_puzzle2(all_sacks)

if __name__ == "__main__":
    main()
