<p align="center">
    Surfs Up - Hawaii Weather Analysis
</p>

<p align="center">
    Module 9 - Advanced Data Storage & Retrieval
</p>


##  **Project Overview**
- When vacationing in Hawaii, I decided to make it my life goal to move out and live there permanently. Making a living in Hawaii is difficult, so I needed to come up with a plan to make sure my business proposal will work. I decided that I want to incorporate a Surf & Ice Cream Shop to the area, however I need to find out more about the area before I pack up and move out.I also realized I need investors, as my savings will not cut it. After finding an investor, they understandably had more concerns, in particular about the weather in the region. He suggests I do an analysis on some Weather data from Oahu so I don't make the same mistakes he did - opening a surfshop in a rainy and cold area.

<p align="center">
     Weather data and its purpose
</p>

    1. Why are we analyzing this data?
    2. What is the goal and possible outcomes?
    3. What pieces of data can help build toward and obtain our goal(s)?


## **Analysis**
Using what I've learned from coding, it was clear that I needed to use a mix of SQL and Python to analyze and display my results. It important we connect to the dataset using SQL and then can analyze the data with python. After pull up the data and seeing what we have to work with, it was clear we could begin drawing out questions to answer based on the data in each database. It was vital that we use the stations to determine where this weather data was collected around the island. Its crucial we find out the min, max and average temperature / rainfall. Below is the code I used to provide an analysis for the Months of June and December. The data was displayed using Flask, which is a great method of viewing the data without getting confused by the code.


<p align="center">
  <img src="https://github.com/lawnshogan/surfs_up/blob/main/Code%20Screenshot.png" width="700"/>
</p>

### **The results...**
Here are some observations I found after analyzing the data...

- Minimum temperatures in June, when tourist season is beginning, are higher than in December, when temperatures are lower and less busy. This is great news.
- Maximum and average temperatures are similar year round (a few degrees difference)
- From our Precipitation analysis, its clear we will have to deal with some precipitation year round, as this is a tropical island. Because we used the station data, we were able to see what parts of the island rain more than others - There was a large difference in these precipitation numbers.

### **Summary**

- While doing this analysis, I thought it would be interesting to go even further and think of other ways we could tell a story with our data. Hawaii relys on tourism and it's important to know when these tourists are coming and where they are staying. We could potentially merge these databases together to tie in more information regarding not only the weather, but the tourists as well. This could help determine if the location will draw tourist traffic or not. 

- As we also individually calculated the percipitation and temperature data, we could also combine the two to better understand the correlation between temp and precipitation. Ultimately, we just need to find an area that is warm year round, rains less and also has good access to tourist locations.
