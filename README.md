# COVID Misinformation in Nigeria

This code base contains the code used to download tweets from users based in Nigeria from January 1st, 2020 to October 31st, 2020. We have some python scripts and notebooks for how we cleaned the data and some analysis on the tweets. We do not include the actual twitter data that we used for privacy reasons. The project is also still ongoing. You can view our [slide deck](https://docs.google.com/presentation/d/1484OVt3fEI1WVLKQyyVvMZQJcZwA0J1mfvQfH6CFllI/edit?usp=sharing) to get more information on the data we used and our future plans.  

### 1. Data Cleaning 

* [`disinfo.py`](https://github.com/Gankara/CovidMisinfoInNigeria/tree/master/code/data_cleaning): Python script used to access tweets based on hastags and location. Must have appropriate twitter API access credentials in YAML file to run.
* [`to_csv_fn.py`](https://github.com/Gankara/CovidMisinfoInNigeria/tree/master/code/data_cleaning): Python script used to convert json twitter files to csv files.
* [`merge_data.py`](https://github.com/Gankara/CovidMisinfoInNigeria/tree/master/code/data_cleaning): Python script used to merge all of the csv files together and add column with hashtag used for each tweet. 


### 2. Analysis 

* [`analysis_corr.ipynb`](https://github.com/Gankara/CovidMisinfoInNigeria/tree/master/code/corr_analysis): Python notebook used to clean full tweets csv and merge with WHO covid cases. Also contains correlation analysis between the tweets and cases in Nigeria. 
* [`analysis_lda.ipynb`](https://github.com/Gankara/CovidMisinfoInNigeria/tree/master/code/topic_modelling): Python notebook used to run Latent Dirichlet Allocation on the text of tweets to discover most popular topics discussed online. 
* [`analysis_misinfo.ipynb`](https://github.com/Gankara/CovidMisinfoInNigeria/tree/master/code/misinfo_analysis%20): Python notebook used to find tweets that contains keywords identified as being related to misinformation in Nigeria. 


## THIS CODEBASE IS A DRAFT AND CURRENTLY STILL BEING UPDATE. PlEASE DO NOT SHARE WIDELY. 
