def total_distance(x, y):
    if len(x) != len(y):
        raise ValueError("Lists must be of equal length")
    
    first_list = sorted(x)
    secound_list = sorted(y)
    all_distances = []
    for i in range(len(first_list)):
        distance = abs(first_list[i] - secound_list[i])
        all_distances.append(distance)
    return sum(all_distances)

def read_input(filename):
    first_list = []
    second_list = []
    
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                num1, num2 = map(int, line.split())
                first_list.append(num1)
                second_list.append(num2)
    
    return first_list, second_list

try:
    x, y = read_input('input.txt')
    result = total_distance(x, y)
    print(result)
except Exception as e:
    print(f"Error: {e}")