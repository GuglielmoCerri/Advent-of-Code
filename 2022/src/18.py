import lib.aoc as aoc
import numpy as np
import scipy.ndimage as ndi


#-----------------------------------------------------------------------------------------------    
@aoc.main('18', 1)
def main_p1(indata: str) -> str:
    cubes = np.array([x.split(',') for x in indata.split('\n')]).astype(np.int64)
    space = np.zeros(cubes.max(axis=0) + 1)
    space[tuple(cubes.T)] = 1

    return sum(np.count_nonzero(np.diff(space, 1, dim, 0, 0)) for dim in range(3))

#-----------------------------------------------------------------------------------------------    
@aoc.main('18', 2)
def main_p2(indata: str) -> str:
    cubes = np.array([x.split(',') for x in indata.split('\n')]).astype(np.int64)
    space = np.zeros(cubes.max(axis=0) + 1)
    space[tuple(cubes.T)] = 1
    space = ndi.binary_fill_holes(space)

    return sum(np.count_nonzero(np.diff(space, 1, dim, 0, 0)) for dim in range(3))


if __name__ == "__main__":
    main_p1()
    main_p2()