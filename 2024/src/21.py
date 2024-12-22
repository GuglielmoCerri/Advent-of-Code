import typing
import functools
import itertools

from lib.aoc import aoc

_NUMERIC_KEYPAD = {
    "A": {"<": "0", "^": "3"},
    "0": {"^": "2", ">": "A"},
    "1": {"^": "4", ">": "2"},
    "2": {"<": "1", ">": "3", "^": "5", "v": "0"},
    "3": {"<": "2", "^": "6", "v": "A"},
    "4": {"^": "7", "v": "1", ">": "5"},
    "5": {"<": "4", ">": "6", "^": "8", "v": "2"},
    "6": {"<": "5", "^": "9", "v": "3"},
    "7": {"v": "4", ">": "8"},
    "8": {"<": "7", "v": "5", ">": "9"},
    "9": {"<": "8", "v": "6"},
}

_DIRECTIONAL_KEYPAD = {
    "^": {">": "A", "v": "v"},
    "A": {"<": "^", "v": ">"},
    "<": {">": "v"},
    "v": {"^": "^", ">": ">", "<": "<"},
    ">": {"^": "A", "<": "v"},
}

_NEGATE_DIR = {
    "<": ">",
    ">": "<",
    "v": "^",
    "^": "v",
}

def _does_make_sense(path: str) -> bool:
    moves = set(_ for _ in path)
    return all(_NEGATE_DIR[_] not in moves for _ in moves)

def _find_all_sequences(keypad: typing.Dict[str, typing.Dict[str, str]], start: str, end: str) -> set[str]:
    active = [(start, "")]
    visited = set()
    res: set[str] = set()
    while active:
        cur_key, cur_path = active.pop()
        if cur_key == end:
            res.add(cur_path)
            continue
        assert tuple(cur_path) not in visited
        visited.add(tuple(cur_path))
        for new_dir, new_key in keypad[cur_key].items():
            new_path = cur_path + new_dir
            if _does_make_sense(new_path):
                active.append((new_key, new_path))
    assert len({len(_) for _ in res}) == 1
    return res


@functools.cache
def numeric_keypad_sequences(start: str, end: str) -> set[str]:
    return _find_all_sequences(_NUMERIC_KEYPAD, start, end)

@functools.cache
def directional_keypad_sequences(start: str, end: str) -> set[str]:
    return _find_all_sequences(_DIRECTIONAL_KEYPAD, start, end)

def _combine_sequences(seq_a: set[str], seq_b: set[str]) -> set[str]:
    return {_a + _b for _a, _b in itertools.product(seq_a, seq_b)}

def _append_with_a(seq: set[str]) -> set[str]:
    return {_ + "A" for _ in seq}

def _get_keypad_press_sequence(keypad_sequences: typing.Callable[[str, str], set[str]]) -> typing.Callable[[str], set[str]]:
    def _keypad_press_sequence(keys: str) -> set[str]:
        res = {""}
        prev_key = "A"
        for _ in keys:
            res = _append_with_a(_combine_sequences(res, keypad_sequences(prev_key, _)))
            prev_key = _
        return res

    return _keypad_press_sequence

numeric_keypad_press_sequence = _get_keypad_press_sequence(numeric_keypad_sequences)
directional_keypad_press_sequence = _get_keypad_press_sequence(directional_keypad_sequences)

def _subproblems(code: str) -> list[str]:
    assert code.endswith("A")
    pieces = code[:-1].split("A")
    return [_ + "A" for _ in pieces]

@functools.cache
def _shortest(code: str, iterations: int) -> int:
    if iterations == 0:
        return len(code)
    return min(
        sum(_shortest(_, iterations - 1) for _ in _subproblems(cur_seq))
        for cur_seq in directional_keypad_press_sequence(code)
    )

def shortest_full_sequence_press(code: str, iter_size: int) -> int:
    res = numeric_keypad_press_sequence(code)
    return min(_shortest(_, iter_size) for _ in res)

def numeric_part(code: str) -> int:
    return int(code.replace("A", ""))

def _code_complexity(code: str, iter_size: int) -> int:
    return shortest_full_sequence_press(code, iter_size) * numeric_part(code)

def _parse_input(in_str: str) -> list[str]:
    return in_str.splitlines()

@aoc('21', 1)
def p1(indata, depth=2):
    return sum(_code_complexity(_, depth) for _ in _parse_input(indata))

@aoc('21', 2)
def p2(indata, depth=25):
    return sum(_code_complexity(_, depth) for _ in _parse_input(indata))

if __name__ == "__main__":   
    p1()
    p2()
