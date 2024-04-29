"""
Write your answers in the space between the questions, and commit/push only
this file (homework2.py) and countries.csv to your repo. Note that there can 
be a difference between giving a "minimally" right answer, 
and a really good answer, so it can pay to put thought into your work. 

This is a much longer project than those you've done in class - remember to use
comments to help readers navigate your work!

To answer these questions, you will use the two csv files provided in the repo.
The file named gdp.csv contains the per capita GDP of many countries in and 
around Europe in 2023 US dollars. The file named population.csv contains 
estimates of the population of many countries.
"""

"""
QUESTION 1

Short: Open the data

Long: Load the GDP data into a dataframe. Specify an absolute path using the Python 
os library to join filenames, so that anyone who clones your homework repo 
only needs to update one string for all loading to work.
"""

import os
import pandas as pd

path = "D:/好好学习/Python I/HW2/"
filename_gdp = "gdp.csv"
gdp = pd.read_csv(os.path.join(path, filename_gdp))


"""
QUESTION 2

Short: Clean the data

Long: There are numerous issues with the data, on account of it having been 
haphazardly assembled from an online table. To start with, the column containing
country names has been labeled TIME. Fix this.

Next, trim this down to only member states of the European Union. To do this, 
find a list of members states (hint: there are 27 as of Apr 2024) and manually 
create your own CSV file with this list. Name this file countries.csv. Load it 
into a dataframe. Merge the two dataframes and keep only those rows with a 
match.

(Hint: This process should also flag the two errors in naming in gdp.csv. One 
 country has a dated name. Another is simply misspelt. Correct these.)
"""

gdp = gdp.rename({"TIME": "Country_Name"}, axis = 1)
gdp["Country_Name"] = gdp["Country_Name"].replace({"Itly": "Italy", "Czechia": "Czech Republic"})

filename_countries = "countries.csv"
countries = pd.read_csv(os.path.join(path, filename_countries))
gdp_merge = gdp.merge(countries, on = 'Country_Name', how = 'right')
    # "Czech Republic" has no value in "left", hence filled by "nan". 


"""
QUESTION 3

Short: Reshape the data

Long: Convert this wide data into long data with columns named year and gdp.
The year column should contain int datatype objects.

Remember to convert GDP from string to float. (Hint: the data uses ":" instead
of NaN to denote missing values. You will have to fix this first.) 
"""

gdp_long = gdp_merge.melt(id_vars=["Country_Name"], 
                          var_name="year", value_name="gdp")


# for "year": replace prefix "GDP" first; then change string into integer
gdp_long["year"] = gdp_long["year"].map( lambda x: int(x.replace("GDP", "")) )


# for "gdp", replace the ":" by "nan" first; then change string into float
gdp_long["gdp"] = gdp_long["gdp"].replace(":", float("nan"))
gdp_long["gdp"] = gdp_long["gdp"].apply( lambda x: float(x) if isinstance(x, str) else x )
    # print(type(gdp_long.loc[301, "gdp"]))  # test code for data type


"""
QUESTION 4

Short: Repeat this process for the population data.

Long: Load population.csv into a dataframe. Rename the TIME columns. 
Merge it with the dataframe loaded from countries.csv. Make it long, naming
the resulting columns year and population. Convert population and year into int.
"""

filename_pop = "population.csv"
pop = pd.read_csv(os.path.join(path, filename_pop))

pop = pop.rename({"TIME": "Country_Name"}, axis = 1)
pop_merge = pop.merge(countries, on = 'Country_Name', how = 'right')

pop_long = pop_merge.melt(id_vars=["Country_Name"], 
                          var_name="year", value_name="population")
pop_long["year"] = pop_long["year"].map( lambda x: int(x.replace("GDP", "")) )
pop_long["population"] = pop_long["population"].replace(":", float("nan"))
pop_long["population"] = pop_long["population"].apply( lambda x: int(x) if isinstance(x, str) else x )
    # Here, let pop_long["population"] be integer, not float
    
    
"""
QUESTION 5

Short: Merge the two dataframe, find the total GDP

Long: Merge the two dataframes. Total GDP is per capita GDP times the 
population.
"""

gdpandpop = gdp_long.merge(pop_long, on = ("Country_Name", "year"), how = "inner")
gdpandpop["totalgdp"] = gdpandpop["gdp"]*gdpandpop["population"]


"""
QUESTION 6

Short: For each country, find the annual GDP growth rate in percentage points.
Round down to 2 digits.

Long: Sort the data by name, and then year. You can now use a variety of methods
to get the gdp growth rate, and we'll suggest one here: 

1. Use groupby and shift(1) to create a column containing total GDP from the
previous year. We haven't covered shift in class, so you'll need to look
this method up. Using groupby has the benefit of automatically generating a
missing value for 2012; if you don't do this, you'll need to ensure that you
replace all 2012 values with missing values.

2. Use the following arithematic operation to get the growth rate:
    gdp_growth = (total_gdp - total_gdp_previous_year) * 100 / total_gdp
"""

gdpandpop = gdpandpop.sort_values(by=["Country_Name", "year"], ascending=True)

gdpandpop["totalgdp_pre"] = gdpandpop["totalgdp"].shift(1)
gdpandpop.loc[ gdpandpop["year"]==2012, "totalgdp_pre" ] = float('nan')
    # I did not use this: gdpandpop_group = gdpandpop.groupby(["Country_Name", "year"])

gdpandpop["gdp_growth"] = (gdpandpop["totalgdp"] - gdpandpop["totalgdp_pre"]) \
    * 100 / gdpandpop["totalgdp"]
gdpandpop["gdp_growth"] = gdpandpop["gdp_growth"].round(2)


"""
QUESTION 7

Short: Which country has the highest total gdp (for the any year) in the EU? 

Long: Do not hardcode your answer! You will have to put the automate putting 
the name of the country into a string called country_name and using the following
format string to display it:

print(f"The largest country in the EU is {country_name}")
"""

country_name = gdpandpop["Country_Name"].loc[ gdpandpop["totalgdp"] == gdpandpop["totalgdp"].max() ]
    # Here, country_name_df is a dataframe that only contains 1 row 1 colomn
print(f"The largest country in the EU is {country_name.iloc[0]}")


"""
QUESTION 8

Create a dataframe that consists only of the country you found in Question 7

In which year did this country have the most growth in the period 2012-23?

In which year did this country have the least growth in the peroid 2012-23?

Do not hardcode your answer. You will have to use the following format strings 
to show your answer:

print(f"Their best year was {best_year}")
print(f"Their worst year was {worst_year}")
"""
country_largest = gdpandpop.loc[ gdpandpop["Country_Name"]==country_name.iloc[0] ]

best_year = country_largest["year"].loc[ country_largest["gdp_growth"] == country_largest["gdp_growth"].max() ]
worst_year = country_largest["year"].loc[ country_largest["gdp_growth"] == country_largest["gdp_growth"].min() ]
print(f"Their best year was {best_year.iloc[0]}")
print(f"Their worst year was {worst_year.iloc[0]}")





