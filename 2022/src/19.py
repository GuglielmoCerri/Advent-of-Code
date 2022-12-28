import lib.aoc as aoc
import re
import math

#-----------------------------------------------------------------------------------------------
def dfs(recipes, time_left, resources=(0,0,0,0), robots=(1,0,0,0), best=0):
    for (robot,recipe) in [x for x in enumerate(recipes) if all([robots[i]>0 for i,quantity in enumerate(x[1]) if quantity>0])]:
        if robot==3 or (robots[robot] < (max_spend:=max(r[robot] for r in recipes)) and max_spend*time_left>resources[robot]):
            if (wait:=1+max(0,max(math.ceil((qty-resources[i])/robots[i]) for i,qty in enumerate(recipe) if qty>0))) <= time_left:
                new_res = tuple(resources[i] + robots[i]*wait - qty for i,qty in enumerate(recipe))
                best = dfs(recipes,time_left-wait,new_res,tuple(robots[i]+1 if robot==i else robots[i] for i in range(4)), max(best,new_res[3]))
    resources = tuple(resources[i] + robots[i]*(time_left+1) for i in range(4)); return max(best, resources[3])

#-----------------------------------------------------------------------------------------------    
@aoc.main('19', 1)
def main_p1(indata: str) -> str:
    data = indata.split('.\n')
    blueprints = [[(a,0,0,0),(b,0,0,0),(c,d,0,0),(e,0,f,0)] for a,b,c,d,e,f in 
                  [map(int,re.findall(r'\d+',line)[1:]) for line in data]]

    return sum( i*dfs(bp, 23) for i,bp in enumerate(blueprints,1) )
    
#-----------------------------------------------------------------------------------------------    
@aoc.main('19', 2)
def main_p2(indata: str) -> str:
    data = indata.split('.\n')
    blueprints = [[(a,0,0,0),(b,0,0,0),(c,d,0,0),(e,0,f,0)] for a,b,c,d,e,f in 
                  [map(int,re.findall(r'\d+',line)[1:]) for line in data]]

    return math.prod( dfs(bp, 31) for bp in blueprints[0:3] )


if __name__ == "__main__":
    main_p1()
    main_p2()