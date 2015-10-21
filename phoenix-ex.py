import json
from pandas import DataFrame
import pylab
import matplotlib.pyplot as plt

business_file = 'yelp_academic_dataset_business.json'

## FIRST APPROACH ##
# business_records = [json.loads(line) for line in open(business_file)]
# business_data_frame = DataFrame(business_records)

# column = 'stars'
# business_counts = business_data_frame.groupby(column).size()

# print business_counts
# business_counts.plot(kind='bar', rot=0)

## SECOND APPROACH ##
# functions that automatically plot the data when you pass the JSON file name


def gets_data_frame(file_path):
    """
    Creates a DataFrame object from a JSON file.

    @param file_path: the absolute path of the JSON file that contains the data
    """

    # don't process the entire review file at once, use enumerate
    # http://stackoverflow.com/questions/2081836/reading-specific-lines-only-python/2081880#2081880
    if 'review' not in file_path:
        records = [json.loads(line) for line in open(file_path)]
    else:
        records = []
        fp = open(file_path)
        for i, line in enumerate(fp):
            if i < 10000:
                record = json.loads(line)
                records.append(record)
        
    # insert all records stored in lists to pandas DataFrame
    data_frame = DataFrame(records)

    # business_data_frame = DataFrame([json.loads(line) for line in open('yelp_academic_Dataset_business.json')])
    # stars_group = business_data_frame.groupby('stars')
    # counts = stars_group.size()
    # counts.plot('bar', rot=0)
    # pylab.show()

    # plot_data(business_data_frame, 'stars', 'bar', 'Business ratings', 'Rating', 'Number of places', False, False, 'linear')
    # plot_data(data_frame, column, plot_type, title, x_label, y_label, show_total, show_range, y_scale)
    return data_frame


def plots_data(data_frame, counts, column, plot_type='line', title=None, x_label=None, y_label=None, show_total=True, show_range=False, y_scale='linear'):
    """
    Plots the data including the values for the mean, median, std dev, and, if requested,
    the sum of all the values, and a range with the minimum and maximum values.

    @param column: the column that will be used to group and count the data
    @param plot_type: the graph type, e.g. 'bar', 'barh', 'line', etc.
    @param title: the title of the graph
    @param x_label: the x-axis label
    @param y_label: the y-axis label
    @param show_total: a boolean indicating if the sum of all values should be displayed
    @param show_range: a boolean indicating if the min and max values should be displayed
    """

    # groupby_counts = data_frame.groupyby(column)
    # counts = groupby_counts.size()
    # counts = data_frame.groupyby[column].size()
    mean = data_frame.mean()[column]
    std = data_frame.std()[column]
    median = data_frame.median()[column]

    label = 'mean=' + str(mean) + '\nmedian=' + str(median) + '\nstd=' + str(std)

    if show_total:
        total = data_frame.sum()[column]
        label = label + '\ntotal=' + str(total)

    if show_range:
        min_value = data_frame.min()[column]
        max_value = data_frame.max()[column]
        label = label + '\nrange=[' + str(min_value) + ', ' + str(max_value) + ']'

    fig, ax = plt.subplots(1)

    counts.plot(kind=plot_type, rot=0)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.set_yscale(y_scale)

    # these are matplotlib.patch.Patch properties
    properties = dict(boxstyle='round', facecolor='wheat', alpha=0.95)

    ax.text(0.05, 0.95, label, fontsize=14, transform=ax.transAxes, verticalalignment='top', bbox=properties)

## BUSINESSES

## ARGH ... why doesn't plots_data receive the data_frame????!!?!
# business_data_frame = gets_data_frame('yelp_academic_dataset_business.json')
# stars_group = business_data_frame.groupby('stars')
# stars_counts = stars_group.size()

# plots_data(business_data_frame, stars_counts, 'stars', 'bar', 'Business ratings', 'Rating', 'Number of places', False, False, 'linear')
# # pylab.show()

# reviews_group = business_data_frame.groupby('review_count')
# reviews_counts = reviews_group.size()

# plots_data(business_data_frame, reviews_counts, 'review_count', 'line', 'Reviews per business', 'Review count', 'Frequency', True, True, 'log')
# # pylab.show()


## REVIEWS

review_file = 'yelp_academic_dataset_review.json'
review_data_frame = gets_data_frame(review_file)
rev_stars_group = review_data_frame.groupby('stars')
rev_stars_counts = rev_stars_group.size()

plots_data(review_data_frame, rev_stars_counts, 'stars', 'bar', 'Review ratings', 'Rating Awarded', 'Number of Reviews', False, False, 'linear')
pylab.show()
