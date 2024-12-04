# check if levels are safe or unsafe
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
from typing import List


def is_sequence_safe(sequence: List[int]) -> bool:
    prev_diff = None
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
        if prev_diff is not None:
            if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
                return False
        prev_diff = diff
    return True

def check_safety(x: str) -> int:
    lists = [[int(num) for num in line.split()] for line in x.splitlines()]
    safe_count = 0
    
    for i in lists:
        if is_sequence_safe(i):
            safe_count += 1
            continue
        
        for i in range(len(i)):
            modified = i[:i] + i[i+1:]
            if is_sequence_safe(modified):
                safe_count += 1
                break
                
    return safe_count

with open('input.txt', 'r') as file:
    content = file.read()
    print(check_safety(content))