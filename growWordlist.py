import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 growWordlist.py wordlist")
        sys.exit(1)
    
    printStrings = {}

    with open(sys.argv[1], 'r') as f:
        for l in f.readlines():
            split = l.strip().split(' ')
            if len(split) == 0:
                continue

            fragments = {}
            fragments['full'] = l.strip()
            fragments['first'] = "".join(split[0])
            fragments['all but first'] = " ".join(split[1:])
            fragments['last'] = " ".join(split[-1:])

            if len(split) > 2:
                fragments['all but first two'] = " ".join(split[2:])

            scache = {}

            for key in fragments.keys():
                if fragments[key] not in printStrings:
                    printStrings[fragments[key]] = True
                    printStrings[fragments[key].upper()] = True
                    printStrings[fragments[key].lower()] = True

    for s in printStrings.keys():
        print(s)
    
