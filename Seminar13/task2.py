def get_dict_data(my_dict: dict, key: str, value = None):
    try:
        return my_dict[key]
    except KeyError:
        return value
    
if __name__ == '__main__':
    my_dict = {'один':1, 'два':2, 'три':3}
    print(get_dict_data(my_dict, 'три'))
    print(get_dict_data(my_dict, 'четыре'))