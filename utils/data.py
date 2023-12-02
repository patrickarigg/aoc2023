import os
def get_data(day):
    #get any test data
    data_dict = {}
    data_files = [file for file in os.listdir(f'{os.path.dirname(__file__)}/../day{day}/data') if file.endswith('.txt')]
    for data_file in data_files:
        with open(f'{os.path.dirname(__file__)}/../day{day}/data/{data_file}') as file:
            file_content = file.read()
            data = file_content.split('\n')
            data.remove('')
        data_dict[data_file]=data

    return data_dict
