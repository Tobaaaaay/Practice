from itertools import combinations

def possible_combinations():
    for i in range(2,3):
        # bvn file names of each entity
        items = ["entity1.txt", "entity2.txt","entity3.txt", "entity4.txt","entity5.txt"]
        combs = list(combinations(items,i))  # Select 3 elements
        print(combs)  # [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
        print(str(len(combs))+ " combibations")  # 4
    return combs
    
# Step 1: Define the file paths (list of tuples and individual files)
# file_paths = [('entity1.txt', 'entity2.txt'), 'entity3.txt', 'entity4.txt']

# Step 2: Function to read the content of a file and return it as a set
def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.read().splitlines())


# Step 3: Function to perform intersection dynamically based on the tuple size
def dynamic_intersection(file_paths):
    # Convert file_paths to a list, in case it's a single file
    # if isinstance(file_paths, str):
        # file_paths = [file_paths]
    # Start with the first file's content
    

    for x in range(0,len(file_paths)):
        selection = file_paths[x]
        intersection_result = read_file(file_paths[0])
    # Iterate over the remaining files and update the intersection result
        for file in selection[0:]:
            content = read_file(file)
            intersection_result = intersection_result.intersection(content)
            print(intersection_result)

# return intersection_result



# Step 4: Apply the dynamic intersection on file_paths
result = dynamic_intersection(possible_combinations())
e
# Step 5: Output the result
print("Common content across all files:", result)