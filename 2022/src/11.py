import lib.aoc as aoc
import re 
import operator

ROUNDS_P1 = 20
ROUNDS_P2 = 10000

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
} 

#-------------------------------------------------------------------------------
class Monkey:
    
    def __init__(self, items, expression, divisible, true_choice, false_choice):
        self.items        = items
        self.operation    = expression[0]
        self.operand      = int(expression[1]) if expression[1].isdigit() else expression[1]
        self.divisible    = divisible
        self.true_choice  = true_choice
        self.false_choice = false_choice
        self.__activity   = 0
        
    def _reduce_size(self, item, lcd):
        return item % lcd #if self.part_2 else item
    
    def _computing_new_value(self, item, lcd):
        if isinstance(self.operand, int):
            new_item = operators.get(self.operation)(item, self.operand)
        else:
            new_item = operators.get(self.operation)(item, item)
    
        return self._reduce_size(new_item, lcd)
        
    def _compute_choice(self, val):
        return self.true_choice if val % self.divisible == 0 else self.false_choice
    
    def inspecting(self, lcd):
        self._calculate_activity()
        tmp_list   = self.items[:]
        self.items = []
        return \
            [(self._compute_choice(self._computing_new_value(item, lcd)),self._computing_new_value(item, lcd)) for item in tmp_list]
    
    def add_item(self, item):
        self.items.append(item)
    
    def _calculate_activity(self):
        self.__activity += len(self.items) 
    
    def get_activity(self):
        return self.__activity

#-------------------------------------------------------------------------------
def parser(l:list):
    name         = int(re.findall(r'\d+', l[0])[0])
    items        = [int(x) for x in re.findall(r'\d+', l[1])]
    expression   = l[2].split('new = old ')[1].split()
    divisible    = int(re.findall(r'\d+', l[3])[0])
    true_choice  = int(re.findall(r'\d+' , l[4])[0])
    false_choice = int(re.findall(r'\d+', l[5])[0])
    
    return name, items, expression, divisible, true_choice, false_choice

#-------------------------------------------------------------------------------
def monkey_initialization(indata):
    monkeys = dict()
    lcd = 1  # lowest common denominator
    for i in range(0, len(indata), 6):
        name, items, expression, divisible, true_choice, false_choice = parser(indata[i:i+6])
        monkey = Monkey(items, expression, divisible, true_choice, false_choice)
        monkeys[name] = monkey
        lcd *= monkey.divisible
        
    return monkeys, lcd
    
#-------------------------------------------------------------------------------    
@aoc.main('11', 1)
def main_p1(indata: str) -> int:
    indata = indata.split('\n')
    indata = [i for i in indata if i]

    monkeys, lcd = monkey_initialization(indata)
   
    _ = [ [ [monkeys[new_item[0]].add_item(new_item[1]) 
            for new_item in monkeys[monkey].inspecting(lcd) ] \
            for monkey in monkeys] \
            for _ in range(ROUNDS_P1)]

    business = [monkeys[monkey].get_activity() for monkey in monkeys]
    business.sort(reverse=True)
    
    return business[0] * business[1]

#-------------------------------------------------------------------------------    
@aoc.main('11', 2)
def main_p2(indata: str) -> str:
    indata = indata.split('\n')
    indata = [i for i in indata if i]

    monkeys, lcd = monkey_initialization(indata)

    _ = [ [ [monkeys[new_item[0]].add_item(new_item[1]) 
            for new_item in monkeys[monkey].inspecting(lcd) ] \
            for monkey in monkeys] \
            for _ in range(ROUNDS_P2)]

    business = [monkeys[monkey].get_activity() for monkey in monkeys]
    business.sort(reverse=True)

    return business[0] * business[1]

if __name__ == "__main__":
    main_p1()
    main_p2()