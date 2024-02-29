# Tea Flavor Analysis

This project was the final for the "Evolution of Food" seminar course at Pomona College with the code and paper for the project written in December 2022. The paper, csv files, and coding was done by me, [Samuel Wang](https://github.com/swangtree). A link to the paper can be found [here](https://docs.google.com/document/d/1m8sX9uINlREx4-TNqPJcAEAJGZtXbgFtzmOfzaird94/edit?usp=sharing).

## Table of Contents

- [About](#about)
- [Configuration](#configuration) 
- [Features](#features)
- [Documentation](#documentation)

## About

The goal of the paper is to compare the correlations between popular flavor notes and the prices and ratings of teas. A couple key themes explored in the paper are:

1. **Consumer perception of quality based on flavor profiles** - How are certain flavor notes like "creamy" or "brothy" associated with higher quality and pricing?

2. **Internal product cues** - The paper focuses on how intrinsic flavor characteristics act as cues for quality. This is compared to extrinsic cues like packaging, branding etc.

3. **Applications of flavor analysis** - Understanding correlations between flavors and perceptions of value can help with product development, food pairings, and targeted marketing.

The figures used the in paper are created from charts made in `tea_data_analysis.py`. The data was manually scraped from [Steepster](https://steepster.com/) into csv files (I copied and pasted data from different websites into an excel file). In the future, I want to explore web scraping tools, but for this project the data was manually scraped due to time constraints.

The entire paper process start to finish was completed within a week, so files aren't organized as neatly as I would like, but I'm happy with the end result!

## Configuration

The script contains several configurable parameters:

- `significant_flavor_notes()` - customize the number of flavor notes in each tea to consider, for ex. only take the top 5 flavor notes from each tea
- `scatter_plot()` - configure plot styles and labels

See the documentation in `tea_data_analysis.py` for details.

## Features

Key features of this project:

- Parses tea data from CSV file 
- Extracts significant flavor notes
- Calculates average price and rating
- Generates scatter plots for visual analysis
- Computes correlation between attributes

The plots allow quick visual inspection of how different flavor notes correlate with price and rating. This can reveal interesting patterns in how certain tasting notes are perceived as more "premium".

## Documentation
In addition to the sources listed in the bibliography of the paper, these additional resources were used:
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
- I used this [StackOverflow discussion](https://stackoverflow.com/questions/14720331/how-to-generate-random-colors-in-matplotlib) for creating random colors