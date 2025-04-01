import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv("medical_examination.csv")
#print(df)

# Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
df['overweight'] = (df["weight"] / (df["height"] / 100) ** 2 > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df["gluc"] = (df["gluc"] > 1).astype(int)
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)

# Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])


    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index()
    df_cat = df_cat.rename(columns={0: "totals"})
    

    # Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().
    cht = sns.catplot(x="variable", y="totals", col="cardio", hue="value", data=df_cat, kind="bar") 


    # Get the figure for the output and store it in the fig variable.
    fig = cht.fig


    # Do not modify the next two lines.
    fig.savefig('catplot.png')
    return fig


# Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data: 
    df_heat = None

    # Calculate the correlation matrix and store it in the corr variable.
    corr = None

    # Generate a mask for the upper triangle and store it in the mask variable.
    mask = None



    # Set up the matplotlib figure.
    fig, ax = None

    # Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().



    # Do not modify the next two lines.
    fig.savefig('heatmap.png')
    return fig
    

