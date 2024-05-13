# Your name here
# Your CNET ID here (this is the part of your uchicago email id before the @)
# Your github user id here

"""
INSTRUCTIONS

Available: May 2nd

Due: May 12th at 11:59PM

Gentle reminder that, among other things, you

(a) Must answer your questions in the homework3.py file
(b) Must homework3.py commit to your clone of the GitHub homework repo
(c) Must link your GitHub repo to GradeScope
(d) Must NOT repeatedly use a hard-coded path for the working directory
(e) Must NOT modify the original data in any way

Failure to do any of these will result in the loss of points
"""

"""
QUESTION 1

In this question, you'll be replicating the graph from Lecture 14, slide 5
which shows the population of Europe from 0 AD to the present day in both
the linear and the log scale. You can find the data in population.csv, and the
variable names are self-explanatory.

Open this data and replicate the graph. 

Clarification: You are not required to replicate the y-axis of the right hand
side graph; leaving it as log values is fine!

Clarification: You are not required to save the figure

Hints: Note that...

- The numpy function .log() can be used to convert a column into logs
- It is a single figure with two subplots, one on the left and the other on
the right
- The graph only covers the period after 0 AD
- The graph only covers Europe
- The figure in the slides is 11 inches by 6 inches
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.regression.linear_model import OLS


# import the data
path = "D:/好好学习/Python I/HW3/"  # change as for your computer
pop = pd.read_csv(os.path.join(path, "population.csv"))
countries = pd.read_csv(os.path.join(path, "countries.csv"))
    # Here I downloaded from wikipedia, 
    # see in https://en.wikipedia.org/wiki/Europe#List_of_states_and_territories


# clean the data
pop.rename(columns={"Population (historical estimates)": "Population", 
                    "Entity": "Country_Name"}, 
           inplace=True)
pop = pop[pop["Year"] >= 0]
pop = pop.merge(countries, on = "Country_Name", how = "right")
pop_Eu = pop.groupby("Year")["Population"].sum().reset_index()
pop_Eu["ln_Pop"] = np.log(pop_Eu["Population"])
pop_Eu["Population"] = pop_Eu["Population"] / 1000000


# plot the data
fig, ax = plt.subplots(1, 2, figsize=(11, 6))

ax[0].plot(pop_Eu["Year"], pop_Eu["Population"], "b-")
ax[0].set_ylabel("Estimated Population (in millions)")
ax[0].set_title("Population of Europe from 0 AD", loc = "center")

ax[1].plot(pop_Eu["Year"], pop_Eu["ln_Pop"], "r-")
ax[1].set_title("log Population of Europe from 0 AD", loc = "center")
ax[1].set_ylabel("ln Estimated Population (in natural logarithm)")

for ax in ax: 
    ax.set_xlabel("Year")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, axis="both", linestyle="--")

plt.show()


"""
QUESTION 2

A country's "capital stock" is the value of its' physical capital, which includes the 
stock of equipment, buildings, and other durable goods used in the production 
of goods and services. Macroeconomists seem to conisder it important to have 
public policies that encourage the growth of capital stock. Why is that?

In this exercise we will look at the relationship between capital stock and 
GDP. You can find data from the IMF in "capitalstock.csv" and documentation in
"capitalstock documentation.txt".

In this exercise we will only be using the variables that are demarcated in
thousands of 2017 international dollars to adjust for variation in the value 
of nominal national currency. Hint: These are the the variables that 
end in _rppp.

1. Open the dataset capitalstock.csv and limit the dataframe to only 
observations from 2018

2. Construct a variable called "capital_stock" that is the sum of the general
government capital stock and private capital stock. Drop 
observations where the value of capital stock is 0 or missing. (We will be 
ignoring public-private partnership capital stock for the purpose of t
his exercise.)

3. Create a scatterplot showing the relationship between log GDP and log
capital stock. Put capital stock on the y-axis. Add the line of best 
fit. Add labels where appropriate and make any cosmetic adjustments you want.

(Note: Does this graph suggest that macroeconomists are correct to consider 
 capital stock important? You don't have to answer this question - it's 
 merely for your own edification.)

4. Estimate a model of the relationship between the log of GDP 
and the log of capital stock using OLS. GDP is the dependent 
variable. Print a table showing the details of your model and, using comments, 
interpret the coefficient on capital stock. 

Hint: when using the scatter() method that belongs to axes objects, the alpha
option can be used to make the markers transparent. s is the option that
controls size
"""

# import the data
cap = pd.read_csv(os.path.join(path, "capitalstock.csv"))


# clean the data
cap = cap[cap["year"] >= 2018]
cap["year"].describe()
cap["capital_stock"] = cap["kgov_rppp"] + cap["kpriv_rppp"]
cap = cap[ (cap["capital_stock"] != 0) & (cap["capital_stock"].notnull()) ]

cap["log_capital_stock"] = np.log(cap["capital_stock"])
cap["log_GDP"] = np.log(cap["GDP_rppp"])


# plot the data
fig, ax = plt.subplots(figsize=(11, 6))

ax.scatter(cap["log_GDP"], cap["log_capital_stock"], alpha=0.5, color='blue', s=20)
ax.set_title("Scatter Plot of log GDP vs log Capital Stock", loc = "center")
ax.set_xlabel("log GDP")
ax.set_ylabel("log Capital Stock")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

m, b = np.polyfit(cap['log_GDP'], cap['log_capital_stock'], 1)
gen_line = np.poly1d((m, b))
ax.plot(cap['log_GDP'], gen_line(cap['log_GDP']), "k--", label='Best Fit Line')
plt.legend()

plt.show()


# regression
model1 = OLS.from_formula("log_GDP ~ log_capital_stock", data=cap).fit()
print(model1.summary())

### Statistic Interpret: 
### the coefficient on capital stock is 0.9757, means that when captical stock 
### changes 1 percent, the nation's GDP of the year changes 0.9757 percent 
### coresspondly. 
### The t-value is 91.828, which is significant under the level of 5%. 


