from typing import Union


def direction(facing: str, turn: Union[int, float]) -> str:
    """Return the direction you will face after the turn."""
    # verify types
    if not isinstance(facing, str):
        raise ValueError(f'"facing" arg must be str, not {type(facing).__name__}')
    if not isinstance(turn, (int, float)):
        raise ValueError(f'"turn" arg must be [int, float], not {type(turn).__name__}')

    MAX_LEFT_TURN = -1800
    MAX_RIGHT_TURN = 1800
    TURN_DEGREE = 45
    FULL_CIRCLE = 360
    DIRECTIONS = {
        'N': 0,
        'NE': 45,
        'E': 90,
        'SE': 135,
        'S': 180,
        'SW': 225,
        'W': 270,
        'NW': 315
    }
    INVERT_DIRECTIONS = {value: key for key, value in DIRECTIONS.items()}

    # check is facing correct
    _facing = facing.upper()
    if _facing not in DIRECTIONS:
        raise ValueError(f'"facing" arg must be in {list(DIRECTIONS)}')

    # check is turn in range
    if not MAX_LEFT_TURN <= turn <= MAX_RIGHT_TURN:
        raise ValueError(f'"turn" arg must be in range[{MAX_LEFT_TURN}, {MAX_RIGHT_TURN}]')
    if turn % TURN_DEGREE != 0:
        raise ValueError(f'"turn" arg must be comparable with min step: {TURN_DEGREE}, not {turn}')

    # getting new direction
    clockwise = 1 if turn >= 0 else -1
    flat_turn = int(abs(turn) % FULL_CIRCLE * clockwise)
    current_direcrion_degree = DIRECTIONS[_facing]
    new_direction_degree = (FULL_CIRCLE + current_direcrion_degree + flat_turn) % FULL_CIRCLE
    new_direction = INVERT_DIRECTIONS[new_direction_degree]

    return new_direction


if __name__ == "__main__":
    print(direction('S', 0))
    print(direction('S', 180))
    print(direction('se', -45))
    print(direction('W', 495))