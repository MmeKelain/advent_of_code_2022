def create_elf_task_lists(x, y):
    elf1 = x.split('-')
    elf2 = y.split('-')
    elf1_tasks = list(range(int(elf1[0]), int(elf1[1])+1))
    elf2_tasks = list(range(int(elf2[0]), int(elf2[1])+1))
    return(elf1_tasks, elf2_tasks)

def day4_puzzle1(assig):
    count = 0
    for x,y in assig:
        elf1_tasks, elf2_tasks = create_elf_task_lists(x, y)
        elf1_tasks = set(elf1_tasks)
        elf2_tasks = set(elf2_tasks)
        if elf1_tasks >= elf2_tasks:
            count+= 1
        elif elf2_tasks >= elf1_tasks:
            count+=1
    print(count)
    return None

def day4_puzzle2(assig):
    count = 0
    for x,y in assig:
        elf1_tasks, elf2_tasks = create_elf_task_lists(x, y)
        temp_count = False
        for i in elf1_tasks:
            for j in elf2_tasks:
                if i == j:
                    temp_count = True
                    break
                else:
                    continue
        if temp_count:
            count += 1
    print(count) 
    return None

def main():
    file = open("input.txt", 'r')
    assig = [tuple(line.strip().split(',')) for line in file.readlines()]
    day4_puzzle1(assig)
    day4_puzzle2(assig)

if __name__ == "__main__":
    main()
