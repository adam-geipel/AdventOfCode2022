import sys, logging, re

def main(filename):
    instructions = []
    rows = []
    stacks = []

    with open(filename) as assignment_file:

        box_mode = True
        init_flag = True

        for line in assignment_file:
            # stack mode: regex doesn't match ^{\d\s}+$
            if (box_mode):
                boxes = re.findall("(\[[A-Z]{1}\]|\s{3})\s{0,1}", line)
                
                if (init_flag):
                    stacks = [[] for i in range(len(boxes))]
                    init_flag = False

                for idx,box in enumerate(boxes):
                    if (box.strip() != ""):
                        stacks[idx].append(box)

                if (len(re.findall("\s\d\s", line)) > 0):
                   box_mode = False
                   continue
                else:
                    rows += boxes
                        
            # move mode: regex matches ^move+$
            if "move" in line:
                instruction = re.findall("\d", line) 
                instructions.append(instruction)

    for instruction in instructions:
        i = 0
        move_count = int(instruction[0])
        home_col = int(instruction[1])
        dest_col = int(instruction[2])

        while (i < move_count):
            if(len(stacks[home_col - 1]) > 0):
                val = stacks[home_col - 1].pop()
                stacks[dest_col - 1].append(val)
                i += 1
            else: 
                break
    
    print_crates(stacks)

    
def print_crates(stacks):
    
    max_length = max(len(x) for x in stacks )
    idx = 0
    
    while idx <= max_length:
        for stack in stacks:
            
            if len(stack) <= (max_length - idx - 1) or len(stack) == 0:
                print("   ", end = " ")
            else:
                print(stack[(max_length - idx) - 1], end = " ")
        
        print("")
        idx += 1

    for x in range(len(stacks)):
        print(" " + str(x + 1), end = "  ")

if __name__ == "__main__":
    main(sys.argv[1])