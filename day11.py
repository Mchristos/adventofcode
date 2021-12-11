from helpers import read_input, begin_part_one, begin_part_two, solution

# exclude "i", "o", "l"
ALPHABET = "abcdefghjkmnpqrstuvwxyz"


def increment_at(password, i):
    new_letter = ALPHABET[(ALPHABET.index(password[i]) + 1) % len(ALPHABET)]
    new_password = password[:i] + new_letter + password[i + 1 :]
    if new_letter == "a":
        return increment_at(new_password, i - 1)
    else:
        return new_password


def increment(password):
    return increment_at(password, len(password) - 1)


def includes_straight(password: str):
    straight = [password[0]]
    for i in range(1, len(password)):
        if ALPHABET.index(password[i]) == ALPHABET.index(password[i - 1]) + 1:
            straight.append(password[i])
        else:
            straight = [password[i]]
        if len(straight) >= 3:
            return True
    return False


def contains_two_pairs(password: str):
    pairs = []
    for i in range(1, len(password)):
        if ALPHABET.index(password[i]) == ALPHABET.index(password[i - 1]):
            if password[i] not in pairs:
                pairs.append(password[i])
    if len(pairs) >= 2:
        return True
    else:
        return False


def is_valid(password: str):
    return includes_straight(password) and contains_two_pairs(password)


def solve(input: str):
    valid = False
    password = input
    while not valid:
        password = increment(password)
        valid = is_valid(password)
    return password


begin_part_one()
input = "cqjxjnds"
part1 = solve(input)
solution(part1)
begin_part_two()
solution(solve(part1))
