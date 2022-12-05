import sys, logging

def main(filename):

    overlaps = []

    with open(filename) as assignment_file:
        i = 0 

        for line in assignment_file:
            assignments = line.split(',')
            
            first = resolve_assignment(assignments[0])
            second = resolve_assignment(assignments[1])

            
            
            if (all(elem in range(first[0], first[1] + 1) for elem in range(second[0], second[1] + 1)) or all(elem in range(second[0], second[1] + 1) for elem in range(first[0], first[1] + 1))):
                overlaps.append(i)
                logging.debug("Match found!")
            
            i += 1
            
            if (logging.getLogger().level == logging.DEBUG):
                logging.debug("-----------")
                print_sections(first)
                print_sections(second)
                logging.debug("-----------\n")

    logging.info("Number of total overlapping assignments: %d", len(overlaps))
    logging.info(overlaps)


def resolve_assignment(s):
    bounds = s.split('-')
    return(int(bounds[0]), int(bounds[1]))
    
def print_sections(sections):
    logstr = ""
    for x in range(10):
        if (x >= sections[0] and x <= sections[1]):
            logstr += str(x)
        else: 
            logstr += '.'

    logging.debug(logstr)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[1])