import os
import re
import pandas as pd
from collections import defaultdict

#define the directory
directory = "/workspaces/python/"
current_directory_path = os.getcwd()
# obtain existing subdirectories where the csv files will be obtained from
subdirectories = os.scandir(current_directory_path)

# regex expression for '.csv  files'
csv_pattern = re.compile(r'.*\.csv$', re.IGNORECASE)
# regex expression for '.xlxs files'
xlxs_pattern = re.compile(r'.*\.xlsx$', re.IGNORECASE)

# os.getcwd
print(current_directory_path)
print(subdirectories)

# array to store sub directories
subdirectories_path = []
subdirectories_name = []

# for loop to obtain the list of subdirectories in the cwd
for x in subdirectories:
    if x.is_dir():
        subdirectories_path.append(x.path)
        subdirectories_path.append(x.name)
        print(x.name)

#check each sub-folder
for inspect_file in subdirectories_path:

    with os.scandir(inspect_file) as inspect_subdirectory:
    # for csv_file in subdirectories:
    # check if the file is a .csv or .xls
        for files in inspect_subdirectory:
            if files.is_file() and csv_pattern.match(files.name):
                print(inspect_file+ ' .csv file format detected')

                # obtain header of file using pandas and file path
                df = pd.read_csv(files.path)
                csv_header = df.columns.tolist()

            # elif files.is_file() and xlsx_pattern.match(files.name):
                # print(inspect_file+ ' this is not a csv file..next please :(')
            # else:
            #     print(inspect_file+ " neither excel or excel workbook found")

    # obtain the file name
    # obtain the header in the file
    # map the header to each file



'''
create dictionary in the following format

subdirectory_dictionary = {

    subdirectory_name _1= {

        subdirectory_file_name_1 = { "column_headers" }
        }      

    }

} 

'''

# Create a defaultdict where each value is another defaultdict
data = defaultdict(lambda: defaultdict(dict))

# Adding data
data['subdirectory_dictionary'][x.name] = 'Alice'
data['subdirectory_dictionary'][x.name]['Alice'] = 'hello'
data['subdirectory_dictionary'][x.name][files.name] = csv_header


# data['person1']['age'] = 30
# data['person2']['name'] = 'Bob'
# data['person2']['age'] = 25