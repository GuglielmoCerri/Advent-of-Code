import lib.aoc as aoc

DIC = { "=" : -2 , '-' : -1 }
SYM = "=-012"

#-----------------------------------------------------------------------------------------------
def to_decimal(snafu):
    vals = [ int(DIC[x]) if x in DIC.keys() else int(x) for x in snafu ]
    return sum([x * pow(5,i) for x,i in list(zip(vals, range(len(vals)-1,-1,-1)))])

#-----------------------------------------------------------------------------------------------
def to_snafu(decimal):
    snafu = ''
    while decimal:
        decimal, idx = divmod(decimal + 2, 5)
        snafu += SYM[idx]
        
    return snafu[::-1]

#-----------------------------------------------------------------------------------------------    
@aoc.main('25', 1)
def main(indata: str) -> str:
    indata = indata.split('\n')

    return to_snafu( sum([ to_decimal(val) for val in indata]) )


if __name__ == "__main__":
    main()