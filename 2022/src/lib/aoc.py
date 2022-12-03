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
def log_solution(day:str, p1:Any, p2:Any, elapsed:int) -> None:
    """ Write on the log file the results for the two parts for each day

    Args:
        day (str): day
        p1 (Any): part 1 solution
        p2 (Any): part 2 solutions
        elapsed (int): elapsed time in ms for part 1 and 2

    Returns:
        None
    """
    logger.info(f"DAY {day}") 
    logger.info(f"Part 1: {p1}")
    logger.info(f"Part 2: {p2}")
    logger.info(f"Time: {elapsed}ms \n")

    return None

#------------------------------------------------------------------------------
def main(day: str) -> Callable[[AocSolution], Callable[[],None]]:
  def decorator(solver: AocSolution) -> Callable[[],None]:
    def timer() -> None:
      indata = (INPUT_PATH / f'{day}.in').read_text()
      start = time.time()
      p1, p2 = solver(indata.rstrip('\n'))
      elapsed = int((time.time() - start) * 1000)
      _ = log_solution(day, p1, p2, elapsed)
    return timer
  return decorator