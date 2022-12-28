import lib.aoc as aoc

#-----------------------------------------------------------------------------------------------
def calc(monkeys, monke): 
    return int(x if type(x:=monkeys[monke])==int else eval(str(calc(monkeys, x[0])) + x[1] + str(calc(monkeys, x[2]))))

#-----------------------------------------------------------------------------------------------
def part2(monkeys, parent_of, monke):
  (left,op,right) = monkeys[(parent_name := parent_of[monke])]
  peer = calc(monkeys, left if right==monke else right)
  if parent_name == 'root': return peer
  parent = part2(monkeys, parent_of, parent_name)
  order=(parent,peer) if op in '+*' else (peer,parent)
  return eval(str(order[0]) + ({'+':'-', '-':'+', '*':'/', '/':'*'}[op] if op in '+*' or left==monke else op) + str(order[1]))


#-----------------------------------------------------------------------------------------------    
@aoc.main('21', 1)
def main_p1(indata: str) -> str:
    monkeys = {m:int(x) if x.isdigit() else tuple(x.split(' ')) for m,x in 
               [l.split(': ') for l in indata.split('\n')]}   
     
    return calc(monkeys, 'root')

#-----------------------------------------------------------------------------------------------    
@aoc.main('21', 2)
def main_p2(indata: str) -> str:
    monkeys = {m:int(x) if x.isdigit() else tuple(x.split(' ')) for m,x in 
               [l.split(': ') for l in indata.split('\n')]}
    parent_of = {monke: next((p for p,x in monkeys.items() if type(x)==tuple and monke in x), None) for monke in monkeys.keys()}
    
    return int( part2(monkeys, parent_of, 'humn') )

if __name__ == "__main__":
    main_p1()
    main_p2()