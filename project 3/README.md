### Problem Statement
Can we make a model that is able to discern the difference between fictional or non-fictional language? I dive into the depths of reddit to explore the language difference between 2 subreddits- 'LifeProTips' that gives genuine life advice vs 'godtiersuperpowers' which describes people's superpower fantasies.


### Description of Data
|CSV|Size|Description|
|---|---|---|
|LifeProTips_top_scraped.csv|(988, 7)|Posts sorted by 'top' from the subreddit 'LifeProTips'
|godtiersuperpowers_top_scraped.csv|(1000, 7)|Posts sorted by 'top' from the subreddit 'godtiersuperpowers'
|LifeProTips_hot_scraped.csv|(353, 7)|Posts sorted by 'hot'
|godtiersuperpowers_hot_scraped.csv|(988, 7)|Posts sorted by 'hot'
|LifeProTips_new_scraped.csv|(982, 7)|Posts sorted by 'new'
|godtiersuperpowers_new_scraped.csv|(991, 7)|Posts sorted by 'new'
|sub_data.csv|(3961, 9)|A concatenation of the csv files from LifeProTips and godtiersuperpowers which have been reshuffled randomly by their rows.


**Features**

|Feature|Type|Description|
|---|---|---|
|id|obj|ID of the post
|url|obj|A link to the post on reddit
|title|obj|The title of the post written by a user. This is the information that we have based our model on
|self_text|obj|The sub text found under the title of a post which is also written by the user
|score|int|Number of upvotes in the post
|num_comments|int|Number of comments in the post
|subreddit|obj|The target, indicating what subreddit the post came from
|title_word_count|int|The word count of each title indicated by the amount of spaces present
|title_length|int|The amount of characters present in the title


### Appendix
**Sorting posts by:**
- 'Top' means the most highly rated posts within that subreddit
- 'Hot' means the trending posts within that subreddits
- 'New' means the newest posts on that subreddit





### Recommendations and Conclusions
**Conclusion:** <br>
ForestTree Classifier is the model of choice as it is able to distinguish between non-fiction and fantasy quite confidently with reference to the AUC score of 0.97! LifeProTips and godtiersuperpowers share similar language but that wasn't changing model's ability to bypass that impressively. With an optimistic view of this performance, we can further this project to analyse data for facebook and perhaps discern fake news from real news.

**Recommendations:** <br>
Words that were obviously more prominant in godtiersuperpowers such as 'invisible' didn't hold as much weight as I'd like them to have. If I were able to weight words with a higher disparity of balance between subreddits, I feel that the model could perform even better. 
