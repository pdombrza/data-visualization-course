
## Task - filtering the data.
We've loaded the dataframe. However, to generate the visualizations, we need to first prepare it. 
Our final goal is to create a plot to see the total count of games sold on each platform (PC, PS4, XBOX ONE and WiiU) by genre.

For this task, we'll be using the `pandas` library.

Create 3 functions: 
1. To view unique values of the `Platform` column in the `DataFrame`. <div class="hint"> Use `df.unique()` </div>
2. To return the list of platforms we are interested in.
3. To filter the `DataFrame`, group the genre and platform and calculate size of each group. Return the `DataFrame` with 
prepared data.
<div class="hint"> 
Use `df.loc[df['Platform'].isin(platforms)]` to filter the data. <br>
Use `df.groupby` to group the dataframe. <br>
Use `df.size()` to get sizes of individual groups <br>
Use `df.reset_index()` to turn groups into columns <br>
Feel free to look at the reference code.
</div>
