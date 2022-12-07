import sys

def main(filename):

    with open(filename) as assignment_file:
        priority_total = 0
        priority_badge_total = 0

        badge_set = [[],[],[]]

        for idx,line in enumerate(assignment_file):
            # remove newline character added to enumeration
            line = line[:-1]
            priority_total += bag_priority(line)

            badge_set[idx%3] = list(line)

            if (idx != 0 and (idx + 1) % 3 == 0):
                priority_badge_total += badge_priority(badge_set)
                

            
    print("Priority total: ", priority_total)
    print("Badge priority total: ", priority_badge_total)


def bag_priority(line):
    pouches = split(list(line), int(len(line)/2))
           
    common = list(set(pouches[0]) & set(pouches[1]))[0]
    return calculate_priority(common)

def badge_priority(elf_set):
    common = list(set(elf_set[0]) & set(elf_set[1]) & set(elf_set[2]))[0]
    return calculate_priority(common)

def calculate_priority(item):
    return ord(item) - 96 if ord(item) - 96 > 0 else ord(item) - 38

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

if __name__ == "__main__":
    main(sys.argv[1])