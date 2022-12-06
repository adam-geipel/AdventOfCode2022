import sys, logging, re

def main(filename):

    with open(filename) as assignment_file:
        
        for line in assignment_file:
        # stack mode: regex doesn't match ^{\d\s}+$
            boxes = re.findall("[\w{1}]", line)
            while(len(line) > 0): 
        # move mode: regex matches ^move+$

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[1])