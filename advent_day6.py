def is_unique_code(buffer):
    return (len(buffer) == len(set(buffer)))

def day6_puzzle(signal, sig_len):
    curr_buffer = []
    i = 0
    for char in signal:
        i += 1
        curr_buffer.append(char)
        if len(curr_buffer) > sig_len:
            curr_buffer.pop(0) #remove oldest character from buffer
        elif len(curr_buffer) < sig_len:
            continue
        #print(curr_buffer)
        if is_unique_code(curr_buffer):
            print(i)
            return i

def main():
    with open("input.txt", "r") as file:
        signal = file.read().rstrip()
    day6_puzzle(signal, 4)
    day6_puzzle(signal, 14)

if __name__ == "__main__":
    main()