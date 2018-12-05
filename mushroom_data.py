import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint

pd.set_option('display.max_columns', None)
pp = pprint.PrettyPrinter(indent=4)
mushrooms = pd.read_csv('C:\\Users\\mcdonago\\source\\repos\\mushroom_data\\mushroom_data\\mushrooms.csv')
barWidth = .35
figure_counter = 0
cut_off_sample_size = 100
cut_off_ratio = .9

def fill_missing_values(grouped_by_dict):
    return grouped_by_dict.unstack(fill_value=0)

def ready_data(dataset, column_name):
    return fill_missing_values(dataset.groupby('class')[column_name].value_counts())

# two ways to do this. Current iteration method or cap_shape.values and use magic numbers.... This
# seems to be the more robust way
def seperate_edible_mushrooms(mush_dict):
    edible_mush = []
    poison_mush = []
    for key in mush_dict:
        edible_mush.append(mush_dict[key]['e'])
        poison_mush.append(mush_dict[key]['p'])
    return edible_mush, poison_mush

def graph_data(all_data, edible_data, poison_data):
    global figure_counter
    edible_location = np.arange(len(edible_data))
    poison_location = [column + barWidth for column in edible_location]
    plt.bar(edible_location, edible_data, color='#7f6d5f', width=barWidth, edgecolor='white', label='e')
    plt.bar(poison_location, poison_data, color='#557f2d', width=barWidth, edgecolor='white', label='p')
    plt.xticks([r + barWidth for r in range(len(edible_data))], all_data.keys())
    # Create legend & Show graphic
    plt.legend()
    plt.figure(figure_counter)


def graph_all_columns(dataset):
    global figure_counter
    for key in dataset.keys():
        if key == 'class':
            continue
        plt.title(key)
        combined_edible_poison_data = ready_data(dataset, key)
        edible_data, poison_data = seperate_edible_mushrooms(combined_edible_poison_data)
        graph_data(combined_edible_poison_data, edible_data, poison_data)
        figure_counter+=1

def get_ratios(readied_data):
    column_ratios = {}
    for key in readied_data:
        column_ratios[key] = {
            'ratio': 0,
            'total': 0,
            'edible': 0,
            'poison': 0}
    for key in readied_data:
        edible_value = readied_data[key]['e']
        poison_value = readied_data[key]['p']
        total = edible_value + poison_value
        column_ratios[key]['ratio'] = abs((edible_value - poison_value)/(total))
        column_ratios[key]['total'] = total 
        column_ratios[key]['edible'] = edible_value
        column_ratios[key]['poison'] = poison_value
    return column_ratios

def get_all_ratios(all_data):
    all_ratios = {}
    for column in all_data.columns:
        if column == 'class':
            continue
        unique_column_freq = ready_data(all_data, column)
        column_ratio = get_ratios(unique_column_freq)
        all_ratios[column] = column_ratio
    return all_ratios

def set_correlation(mush_dict):
    for column in list(mush_dict):
        for value in list(mush_dict[column]):
            if .25<mush_dict[column][value]['ratio']<.75:
                mush_dict[column][value]['correlation'] = 'no correlation'
            if ((.1<mush_dict[column][value]['ratio']<=.25) or 
               (.75<=mush_dict[column][value]['ratio']<=.9)): 
                mush_dict[column][value]['correlation'] = 'correlated'
            if ((0<=mush_dict[column][value]['ratio']<=.1) or 
               (.9<mush_dict[column][value]['ratio']<=1)):
                mush_dict[column][value]['correlation'] = 'strongly correlated'

def rem_keys(mush_dict, rem_key, cut_off):
    rem_col = {}
    for column in list(mush_dict):
        for value in list(mush_dict[column]):
            if mush_dict[column][value][rem_key] < cut_off:
                rem_col[column] = {}
                rem_col[column][value] = mush_dict[column].pop(value, None)
    return rem_col

def rem_small_totals(mush_dict):
    return rem_keys(mush_dict, 'total', cut_off_sample_size)

def rem_small_ratios(mush_dict):
    return rem_keys(mush_dict, 'ratio', cut_off_ratio)

#graph_all_columns(mushrooms)
#plt.show()
all_col_ratios = get_all_ratios(mushrooms)
set_correlation(all_col_ratios)
#removed_total_columns = rem_small_totals(all_col_ratios)
#removed_ratio_columns = rem_small_ratios(all_col_ratios)






