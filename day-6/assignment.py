import sys

def main(filename):
    with open(filename) as assignment_file:
        stream = list(assignment_file.read())
        sequence_length = 4
        i = sequence_length
        while i < len(stream):
            buffer = stream[i - sequence_length: i]
            
            if len(set(buffer)) == len(buffer): 
                break
            i += 1

        print("first marker after character {0}".format(i))

if __name__ == "__main__":
    main(sys.argv[1])