import re
import pandas as pd

def read_rests_data(filepath):
    """
    Function for reading txt data to dataframe
    :param filepath: (str) path to file
    :return df: pandas data frame
    """

    with open(filepath) as f:
        data = f.read().split('\n')

    bar_dict=dict()

    for line in data:

        fields = [re.split("(?:(?<=url)|(?<=title)|(?<=language)|(?<=tag)):",x) for x in line.strip().split("\t")]

        if (len(fields) < 2) or ('offer' in fields[0][1]):
            continue
        bar_descr = dict()

        for name, value in fields:
            if name == 'title':
                bar_title = value
            elif name == 'tag':
                [k, v] = re.split(":", value, 1)
                if k=='score':
                    sc_type, rtg = v.split(':')
                    bar_descr[k+'_'+sc_type] = rtg
                else:
                    bar_descr[k] = v
        bar_dict[bar_title] = bar_descr
    return pd.DataFrame(bar_dict).T


if __name__ == '__main__':
    filepath = 'datasets/RestAll.txt'
    df = read_rests_data(filepath)
    print('Hello')