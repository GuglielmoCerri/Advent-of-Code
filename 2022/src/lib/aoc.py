import time
from typing import Any, Callable, Iterable
from pathlib import Path
import lib._logging as log


INPUT_PATH  = ( Path(__file__).parents[2] / 'input' ).resolve()
AocSolution = Callable[[str], Iterable[Any]]

logger = log.config_log(Path(__file__).parents[2]  / 'log.log')


#=============================================================================#
# FUNCTIONS
#=============================================================================#

#------------------------------------------------------------------------------
def log_solution(day:str, part, res:Any, elapsed:int) -> None:
    """ Write on the log file the results for the two parts for each day

    Args:
        day (str): day
        p1 (Any): part 1 solution
        p2 (Any): part 2 solutions
        elapsed (int): elapsed time in ms for part 1 and 2

    Returns:
        None
    """
    logger.info(f"DAY {day} - {part}") 
    logger.info(f"Solution: {res}")
    logger.info(f"Time: {elapsed}ms \n")

    return None

#------------------------------------------------------------------------------
def main(day: str, part) -> Callable[[AocSolution], Callable[[],None]]:
  def decorator(solver: AocSolution) -> Callable[[],None]:
    def timer() -> None:
      indata = (INPUT_PATH / f'{day}.in').read_text()
      start = time.time()
      res = solver(indata.rstrip('\n'))
      elapsed = int((time.time() - start) * 1000)
      _ = log_solution(day, part, res, elapsed)
    return timer
  return decorator