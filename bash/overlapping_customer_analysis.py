from itertools import combinations
import pandas as pd

def possible_combinations():
    for i in range(2,3):
        # bvn file names of each entity
        items = ["entity1.txt", "entity2.txt","entity3.txt", "entity4.txt","entity5.txt"]
        combs = list(combinations(items,i))  
        print(combs)  # [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
        print(str(len(combs))+ " combibations")  # 4
    return handle_nested(combs)
    
    
def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.read().splitlines())


# def obtain_entity_names():

def handle_nested(combs):
    for i in combs:
        print(str(i))
        for x,file in enumerate(i):
            if x==0:
                intersection_result = read_file(file)
                print(intersection_result)
            else:
                content = read_file(file)
                print(content)
                intersection_result = intersection_result.intersection(content)
                print(len(intersection_result))
    print(intersection_result)
    update_data_structure(str(i),len(i),intersection_result)    
    return intersection_result     

# def create_data_structure():
    # Create the pandas DataFrame
    # df = pd.DataFrame(columns=['Entities','Quantity','Intersections'])


def update_data_structure(file_names,quantity,intersections):
#     files_names = str(*file_names)e
#     quantity = quantity
#     intersections = intersections
    df.loc[len(df)] = [file_names,quantity,intersections]




# create_data_structure()
df = pd.DataFrame(columns=['Entities','Quantity','Intersections'])
possible_combinations()     
print(df)  