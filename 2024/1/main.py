def total_distance(x, y):
    if len(x) != len(y):
        raise ValueError("Lists must be of equal length")
    """
    # brute force solution
    first_list = sorted(x)
    secound_list = sorted(y)
    all_distances = []
    for i in range(len(first_list)):
        distance = abs(first_list[i] - secound_list[i])
        all_distances.append(distance)
    return sum(all_distances)
    """
    
    return sum(abs(a - b) for a, b in zip(sorted(x), sorted(y)))

def total_similarity_score(x, y):
    first_list = sorted(x)
    second_list = sorted(y)
    
    """
    # brute force solution
    count = 0
    similarity = []
    for i in range(len(first_list)):
        count = 0
        for j in range(len(secound_list)):
            if first_list[i] == secound_list[j]:
                count += 1   
        similarity.append(count)

    total_similarity_score = [a*b for a,b in zip(first_list,similarity)]

    return sum(total_similarity_score)
    """
    
    similarity = [second_list.count(a) for a in first_list]
    
    return sum(a * b for a, b in zip(first_list, similarity))
                

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
    total_similarity = total_similarity_score(x, y)
    print(total_similarity) 
    print(result)
except Exception as e:
    print(f"Error: {e}")