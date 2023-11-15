###########################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import f1_score, plot_roc_curve, roc_auc_score, roc_curve
###########################



def extract_subreddit(subreddit_list):
    for name in subreddit_list:
        
        #1. Making directory for each subreddit and CSV pathway
        # os.makedirs(f'./data/{name}')
        csv_top = f'../data/{name}_top_scraped.csv'
        csv_hot = f'../data/{name}_hot_scraped.csv'
        csv_new = f'../data/{name}_new_scraped.csv'
        
        #2. Accessing the targeted subreddit in subreddit_list
        subreddit = reddit.subreddit(name)
        
        #3. Only include posts sorted by- top and hot
        #   Also limits to 2000 posts
        sub_posts_top = subreddit.top(limit = 1000)
        sub_posts_hot = subreddit.hot(limit = 1000)
        sub_posts_new = subreddit.new(limit = 1000)
        
        #4. Creating dictionary that will store the wanted information
       
        top = {
            "id" : [],
            "url" : [],
            "title" : [],
            'self_text' : [],
            "score" : [],
            "num_comments": [],
            'subreddit': []
        }
        
        hot = {
            "id" : [],
            "url" : [],
            "title" : [],
            'self_text' : [],
            "score" : [],
            "num_comments": [],
            'subreddit': []
        }
        
        new = {
            "id" : [],
            "url" : [],
            "title" : [],
            'self_text' : [],
            "score" : [],
            "num_comments": [],
            'subreddit': []
        }
        
        #5. Extracting information and appending to post_info
        
        for post_t in sub_posts_top:
            
            # Avoiding 'sticky' posts- highlighted posts by subreddit mods
            if not post_t.stickied:
                top["id"].append(post_t.id)
                top["url"].append(post_t.url)
                top["title"].append(post_t.title)
                top["score"].append(post_t.score)
                top["num_comments"].append(post_t.num_comments)
                top["subreddit"].append(str(post_t.subreddit))
                top["self_text"].append(post_t.selftext)
        
        for post_h in sub_posts_hot:
            
            if not post_h.stickied:
                hot["id"].append(post_h.id)
                hot["url"].append(post_h.url)
                hot["title"].append(post_h.title)
                hot["score"].append(post_h.score)
                hot["num_comments"].append(post_h.num_comments)
                hot["subreddit"].append(str(post_h.subreddit))
                hot["self_text"].append(post_h.selftext)
                
        for post_n in sub_posts_new:
            
            if not post_h.stickied:
                new["id"].append(post_n.id)
                new["url"].append(post_n.url)
                new["title"].append(post_n.title)
                new["score"].append(post_n.score)
                new["num_comments"].append(post_n.num_comments)
                new["subreddit"].append(str(post_n.subreddit))
                new["self_text"].append(post_n.selftext)
        
    #6. Return dataframe using post_info dictionary and saving it as a CSV file
        pd.DataFrame(top).to_csv(csv_top, index = False)
        pd.DataFrame(hot).to_csv(csv_hot, index = False)
        pd.DataFrame(new).to_csv(csv_new, index = False)
    return 


#get_metrics will will give the metrics that are in question- accuracy of train and test samples, recall, specificity
def get_metrics(model, X_test, y_test):

    #True negative, False positive, False negative and True positive derived from confusion_matrix will
    #help get our Recall and Specificity
    pred_test = model.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, pred_test).ravel()

    print(f'Train accuracy: {model.best_score_}')
    print(f'Test accuracy: {model.score(X_test, y_test)}')
    
    #the formulas for Recall and Specificity
    print(f'Recall: {tp/(tp+fn)}')
    print(f'Specificity: {tn/(tn+fp)}')
    return 

def recall_specificity(model, X_test, y_test):
    #Plotting ROC curve 
    plot_roc_curve(model, X_test, y_test)
    plt.plot([0, 1], [0, 1], label="baseline", linestyle="--")
    plt.title('ROC Curve')
    print(f'AUC: {roc_auc_score(y_test, model.predict_proba(X_test)[:,1])}')
    
    #our true values and predicted probabilities 
    pred_df = pd.DataFrame({'true_values': y_test,
                            'pred_probs': model.predict_proba(X_test)[:,1]})
    
    #Plotting a distribution plot on the predicted probabilities derived from our model
    plt.figure(figsize = (12, 5))
    
    #Plotting the 1 and 0 of the true values and  
    for group in pred_df.groupby('true_values'):
        sns.distplot(group[1], kde = False, bins = 20, label = f'Actual Outcome = {group[0]}')

    plt.xlabel('Predicted Probability that LifeProTips = 1')
    plt.legend()
    plt.title('Predicted Probability Distribution and their Actual Values')
    return