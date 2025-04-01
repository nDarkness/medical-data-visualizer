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
    # diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
    diastolic_pressure = (df["ap_lo"] <= df["ap_hi"])
    # height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
    height_025 = (df['height'] >= df['height'].quantile(0.025))
    # height is more than the 97.5th percentile
    height_97 = (df['height'] >= df['height'].quantile(0.975))
    # weight is less than the 2.5th percentile
    weight_025 = (df['weight'] >= df['weight'].quantile(0.025))
    # weight is more than the 97.5th percentile
    weight_97 = (df['weight'] >= df['weight'].quantile(0.975))
    
    df_heat = df[diastolic_pressure & height_025 & height_97 & weight_025 & weight_97]
    

    # Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr()
    

    # Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(11, 9))


    # Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    sns.heatmap(corr, annot=True, mask=mask, fmt=".1f", square=True, linewidths=.5)


    # Do not modify the next two lines.
    fig.savefig('heatmap.png')
    return fig
    

