import lib.aoc as aoc
from collections import defaultdict

TOTAL_SIZE          = 100_000
DISK_SPACE_AVAIABLE = 70_000_000
UNUSED_SPACE        = 30_000_000

#-------------------------------------------------------------------------------
def get_disk_structure(indata:str) -> defaultdict:
    dirs = defaultdict(int)
    cwd = []
    for cmd in indata.split('\n'):
        if "$ cd" in cmd:
            folder = cmd.split()[2]
            if folder == "..":
                cwd.pop()
            else:
                cwd.append(folder)
        elif "$ ls" in cmd:
            continue
        else:
            try:
                dirs["/".join(cwd)] += int(cmd.split()[0])
            except ValueError:
                pass

    for d in sorted(dirs.keys(), key=lambda x: x.count("/"), reverse=True):
        dirs["/".join(d.split("/")[:-1])] += dirs[d]

    return dirs

#-------------------------------------------------------------------------------    
@aoc.main('07', 1)
def main_p1(indata: str) -> str:
    dirs = get_disk_structure(indata)
    return sum(s for s in dirs.values() if s <= TOTAL_SIZE)

#-------------------------------------------------------------------------------    
@aoc.main('07', 2)
def main_p2(indata: str) -> str:
   dirs   = get_disk_structure(indata)
   free_space   = DISK_SPACE_AVAIABLE - dirs["/"]
   needed_space = UNUSED_SPACE - free_space
   return min(v for v in dirs.values() if v > needed_space)

if __name__ == "__main__":
    main_p1()
    main_p2()