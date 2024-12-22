import time
from dotenv import load_dotenv
from typing import Any, Callable, Iterable
from pathlib import Path
from aocd import get_data, submit
import lib._logging as log

load_dotenv()

INPUT_PATH = (Path(__file__).parents[2] / 'input').resolve()
AocSolution = Callable[[str], Iterable[Any]]

logger = log.config_log(Path(__file__).parents[2] / 'log.log')


# =============================================================================
# FUNCTIONS
# =============================================================================

# -----------------------------------------------------------------------------
def log_solution(day: str, part: int, res: Any, elapsed: int) -> None:
    """Write on the log file the results for the two parts for each day

    Args:
        day (str): day
        part (int): part number
        res (Any): solution for the part
        elapsed (int): elapsed time in ms for part 1 and 2

    Returns:
        None
    """
    logger.info(f"DAY {day} - {part}")
    logger.info(f"Solution: {res}")
    logger.info(f"Time: {elapsed}ms \n")

    return None


# -----------------------------------------------------------------------------
def aoc(
    day: int,
    year: int,
    part: int,
    submit_res: bool = True
) -> Callable[[AocSolution], Callable[[], None]]:
    def decorator(solver: AocSolution) -> Callable[[], None]:
        def timer() -> None:
            indata = get_data(day=day, year=year)
            start = time.time()
            res = solver(indata)
            elapsed = int((time.time() - start) * 1000)
            if submit_res:
                submit(res, part=part, day=day, year=year)
            _ = log_solution(day, part, res, elapsed)
        return timer
    return decorator