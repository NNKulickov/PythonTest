import yaml
from yaml.loader import SafeLoader
# custom module
from module_print import print_hi

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('config/config.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
        print_hi(data['name'])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
