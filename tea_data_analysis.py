"""
tea_data_analysis.py

Returns a scatter plot of various flavor notes and the price/rating changes of those teas compared to the average tea that can be downloaded as a .png file

Usage:
    in main(), flavor_note_dict = data_dict("<data_file>")
    ...
    scatter_plot(... "<img_nam.png>")

<data_file> should be a CSV file containing the following columns:
    Name,Type,Vendor,Price ($/g),Ratings,Flavor notes

<img_name.png> shold be the name of the output .png file

"""
import matplotlib.pyplot as plt
import random
import numpy as np
import csv

def data_dict(filename):
    """
    Creates a dictionary with flavor note names as keys, and a list of price/rating changes from the average
    :filename: (file) name of .csv file to be read
    """
    data = open(filename, "r")
    data_reader = csv.reader(data)
    data_list = []
    flavor_notes_dict = {"average": []}
    return_dict = {}

    for row in data_reader:
        data_list.append(row)

    for line in data_list[1:]:
        pr = [float(line[3]), float(line[4])]
        flavor_notes_dict["average"].append(pr)
        flavor_notes = line[-1].split(", ")

        for flavor in significant_flavor_notes(flavor_notes):
            if flavor in flavor_notes_dict:
                flavor_notes_dict[flavor].append(pr)
            else:
                flavor_notes_dict[flavor] = [pr]

    total_price = 0
    total_rating = 0

    for pair in flavor_notes_dict["average"]:
        total_price += pair[0]
        total_rating += pair[1]

    average_price = total_price/len(flavor_notes_dict["average"])
    average_rating = total_rating/len(flavor_notes_dict["average"])

    for key in flavor_notes_dict:
        # only takes flavor notes that appear more than 7 times
        if len(flavor_notes_dict[key]) > 7:
            total_price = 0
            total_rating = 0

            for pair in flavor_notes_dict[key]:
                total_price += pair[0]
                total_rating += pair[1]

            # appends return_dict with flavor note price/rating differences from average
            return_dict[key] = [(total_price/len(flavor_notes_dict[key])) - average_price, (total_rating/len(flavor_notes_dict[key])) - average_rating, len(flavor_notes_dict[key])]

    return return_dict


def scatter_plot(data, format_1, name, done, x_axis, y_axis, save = False, filename = None):
    """
    Creates a scatter plot of one stat against another
    :param data: (list) data pairs to be plotted
    :param format_1: (string) format of data points
    :param format_2: (string) format of linear regression line
    :param name: (string) name of the data points for the legend
    :param done: (boolean) if the graph is complete or not
    :param x_axis: (string) name of x axis
    :param y_axis: (string) name of y axis
    :param line: (boolean) if a line should be plotted or not
    :param save: (boolean) if a file should be saved or not
    :param filename: (string) name of filename to be saved as
    :return: None
    """
    # formats data for plt.plot
    x = [data[0]]
    y = [data[1]]

    # plots data
    if name[:7] != "Average":
        plt.scatter(x, y, c=np.random.rand(len(x),3), label=name)

    else:
        plt.scatter(x, y, c="red", label=name)

    # formats legend and axes
    plt.title(y_axis + " plotted with " + x_axis, fontsize=10)
    plt.ylabel(y_axis)
    plt.xlabel(x_axis)
    plt.subplots_adjust(right=0.7)
    plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0, ncol=1, prop={'size': 6})


    # shows graph and legend if final dataset
    if save:
        plt.savefig(filename)

    if done:
        plt.show()


def significant_flavor_notes(flavor_note_list):
    """
     Takes a list of flavor notes and returns a list of the most significant notes
     :param flavor_note_list: (list) A list of flavor notes
     :return: (list) A list of the most significant notes in the input
    """
    return_list = flavor_note_list[:15]
    # Return a list of the flavor note list.
    for i in range(15, len(flavor_note_list)):
        
        if flavor_note_list[i] < flavor_note_list[i - 1]:
            break

        else:
            return_list.append(flavor_note_list[i])

    return return_list


def main():
    flavor_note_dict = data_dict("black_teas.csv")
    print(flavor_note_dict)

    for key in flavor_note_dict:

        if key != "average":
            scatter_plot(flavor_note_dict[key][:3], "b.", key + ", n = " + str(flavor_note_dict[key][2]), False, "price", "rating")

    scatter_plot(flavor_note_dict["average"][:3], "r.", "Average black teas", True, "Price change", "Rating change (from average)", True, "p4.png")


if __name__ == '__main__':
    main()
