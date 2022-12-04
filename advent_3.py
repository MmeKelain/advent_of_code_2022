import string
global all_priority

def merge_two_dicts(x, y):
    z = x.copy()   
    z.update(y)    
    return z
    
def compare(a, b):
    return_str = ""
    for x in a:
        for y in b:
            if x == y:
                if x not in return_str:
                    return_str += x
    return return_str

def day3_puzzle_1(sacks):
    total_val = 0
    for line_sack in sacks:
        firstpart, secondpart = line_sack[:len(line_sack)//2], line_sack[len(line_sack)//2:]
        #print(firstpart)
        #print(secondpart)
        same_items = compare(firstpart, secondpart)
        for l_i in same_items:
            total_val += all_priority[l_i]
            #print(all_priority[l_i])
    return total_val

def day3_puzzle_2(sacks):
    total_val = 0
    list_of_elves = zip(*(iter(sacks),) * 3)

    for i in list_of_elves:
        #print(i)
        elves1n2 = compare(i[0], i[1])
        elves1n3 = compare(i[0], i[2])
        final_elf = compare(elves1n2, elves1n3)
        total_val += all_priority[final_elf]
    print(total_val)

def main():
    letter_count = dict(zip(string.ascii_lowercase, range(1,27)))
    upper_count = dict(zip(string.ascii_uppercase, range(27,53)))

    all_priority = merge_two_dicts(letter_count, upper_count)

    file = open("input.txt", 'r')
    sacks = [line.strip() for line in file.readlines()]
    day3_puzzle_1(sacks)
    day3_puzzle_2(sacks)

if __name__ == "__main__":
    main()

    
        