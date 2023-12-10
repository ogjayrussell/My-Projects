import networkx as nx
import pandas as pd
def jac(train_graph, test_graph, edges_train, edges_test):
    
#creating a list of all of the possible edges present in the graph (matrix of all edges) without  repetitions
#code inspired from Tibebes. M
    
    jac_train = pd.DataFrame(nx.jaccard_coefficient(train_graph, edges_train))
    jac_test = pd.DataFrame(nx.jaccard_coefficient(test_graph, edges_test))
    
    jac_train = jac_train.rename(columns = {2: 'JAC'})
    jac_test = jac_test.rename(columns = {2: 'JAC'})
    
    #multi index to increase accessibility
    jac_train = jac_train.set_index([jac_train.columns[0], jac_train.columns[1]])
    jac_test = jac_test.set_index([jac_test.columns[0], jac_test.columns[1]])
    
    return jac_train, jac_test
    
def aac(train_graph, test_graph, edges_train, edges_test):
    edges_train_copy = edges_train.copy()
    edges_test_copy = edges_test.copy()
    
    #removing mirror node pairs from edges as acadamic adar will run into error
    for edges in [edges_train, edges_test]:
        for i, tup in enumerate(edges):
            if edges[i][0] == edges[i][1]:
                del edges[i]
        
        
                
    #df without the mirrors
    aac_train = pd.DataFrame(nx.adamic_adar_index(train_graph, edges_train))
    aac_test = pd.DataFrame(nx.adamic_adar_index(test_graph, edges_test))
    
    
    #df with mirrors
    mirrors_train = pd.DataFrame(edges_train_copy)
    mirrors_test = pd.DataFrame(edges_test_copy)
    
    #adding back mirrors
    aac_train = pd.merge(aac_train, mirrors_train, how = 'right')
    aac_test = pd.merge(aac_test, mirrors_test, how = 'right')
    
    #renaming columns
    aac_train = aac_train.rename(columns = {2: 'AAC'})
    aac_test = aac_test.rename(columns = {2: 'AAC'})
    
    #replacing mirrors with an AAC score of 0
    aac_train['AAC'] = aac_train['AAC'].fillna(0)
    aac_test['AAC'] = aac_test['AAC'].fillna(0)
    
    #multi index to increase accessibility 
    aac_train = aac_train.set_index([aac_train.columns[0], aac_train.columns[1]])
    aac_test = aac_test.set_index([aac_test.columns[0], aac_test.columns[1]])
    
    return aac_train, aac_test
                
    
def extract_features(X_train_tuples, X_test_tuples, pairwise, jac_train, jac_test, aac_train, aac_test):
    
    #to store results
    result_train = []
    result_test =[]
    
    #accessing the features indexes
    for x in X_train_tuples:
        
        #pairwise
        p = pairwise[x[0],x[1]]
        
        #jaccard coefficient follows a half matrix, the reverse pairs are handled with  exceptions otherwise there's an indexing error
        try:
            jac1 = float(jac_train.loc[x[0],x[1]])
        except:
            jac1 = float(jac_train.loc[x[1],x[0]])
        
        #acadamic adar coefficient also follows a half matrix
        try: 
            aac1 = float(aac_train.loc[x[0],x[1]])
        except:
            aac1 = float(aac_train.loc[x[1],x[0]])
    
        #dict with features
        train_dic = {
            'parwise_distance': p,
            'JAC' : jac1,
            'AAC' : aac1,
        }
        
        result_train.append(train_dic)
    
    for x in X_test_tuples:

        p = pairwise[x[0],x[1]]
        
        try:
            jac2 = float(jac_test.loc[x[0],x[1]])
        except:
            jac2 = float(jac_test.loc[x[1],x[0]])
            
        try:
            aac2 = float(aac_test.loc[x[0],x[1]])
        except:
            aac2 = float(aac_test.loc[x[1],x[0]])
    
        test_dic = {
            'parwise_distance': p,
            'JAC' : jac2,
            'AAC' : aac2,
        }
    
        result_test.append(test_dic)
    
    train_feat = pd.DataFrame(result_train)
    test_feat = pd.DataFrame(result_test)
    
    return train_feat, test_feat