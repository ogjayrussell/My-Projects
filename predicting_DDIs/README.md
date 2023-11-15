# PREDICTING UNDISCOVERED DRUG-DRUG INTERACTIONS


## Problem Statement <br>

The discovery of Drug to Drug interactions (DDIs) are dependent on clinical trials and resourcefully intensive research. The surveillance of drug safety profiles is difficult and time consuming, leaving patients prone to risk of an adverse event if not addressed/ discovered in time. In this project, I explore computational methods to predict unknown DDIs using Deep Learning Neural Networks and other machine learning models such as XGboost and Logistic Regression.

## Tech Stack
- Keras/Tensorflow
- Python
- sklearn
- Tokenisers
- PostgreSQL
- pgAdmin 4

## Project Process

1. Data cleaning
2. Feature Engineering (tokenisation)
3. Exploratory Data Analysis
4. Machine learning methods (XGBoost, Logistic Regression)
4. Preprocessing
5. Deep Learning methods (Neural Networks)

## Background <br>

#### The Importance of Identifying DDIs
 Multiple drug combinations in therapy are common but increase the risk of adverse events because concomitant drugs can share pharmacological or metabolic pathways. DDIs are a leading cause for preventable Adverse Drug Reactions, placing a significant risk on patients and a burden on the healthcare system. Clinical trials for new drugs don’t address the issue of DDIs directly, and potential DDIs are often not discovered until the third phase of a clinical trial. As of now, the most practical way to explore the large number of drug combinations for detecting DDIs are through in silico drug-drug interaction detection; requiring resources, planning and time. It has only been as of recent where more robust computational methods have been developed.

#### The Type of Problem: Link Prediction
The prediction of DDIs follows the concept of a link prediction problem. With a graph that is represented by drugs as nodes and links as interactions, the focus is on the likelihood of a link forming between 2 drugs. This project aims to build a model that is trained on known DDIs at a hypothetical time at T, and predicting new DDIs at T1.


## Data Formatting and Modeling

### Data Formatting process
Healthcare information is notoriously inaccessible due to the information being quite sensitive. Luckily information on pharmaceutical drugs is available for free, with an impressive push towards increasing transparency to curate large databases such as DrugBank and ChEMBL. The project required only 2 sets of data:
- Known DDIs
- Chemical Structures of each unique drug

Collecting known DDIs were relatively straight forward and was sourced from http://ddinter.scbdd.com/. The data provided was 8 complete sets of known DDIs, categorised by the types of interactions i.e. immunomodulatory, metabolistic...

The Chemical Structures of the drugs were sourced from the ChEMBL's massive database https://www.ebi.ac.uk/chembl/. This required for me to host a pgAdmin PostgreSQL server, and navigate the database on approved drugs and their associated chemical structures. Nomenclature describing molecule chemical structures vary, but I chose to follow the SMILES format that was established for computing feasibility, which looks like:
> CCC(=O)N(C1CCN(CCC2=CC=CC=C2)CC1)C1=CC=CC=C1

Tokenisation was necessary to dissect the substructures of the molecule. This had to be done appropriately to retain the integrity of the SMILES intention to express the structure. Tokenisation was performed with a pre-trained SMILES tokenizer that came with its own vocabulary, and would return the above example into:
>[CC, C(=O)N(, C1CCN(, CCC2, =, CC=, CC, =C, 2)...

Once tokenised, comparability between the structure and the known DDIs had to be made. With the list of tokens representing each drug's chemical structure, the drug's chemical structure's similarities were represented by pairwise distance.

#### Data Dictionary

|CSV|Size|Description|
|---|---|---|
|all_drugs_lookup.csv|(1404,2)|Node ID and their associated drugs|
|chem_sim_eda.csv|(1404, 3)|List of each unique drug and their chemical structures following SMILES formatting|
chem_sim.csv|(89008, 5)|Drug to drug interactions with their associated chemical structures and similarity scores|
interactions.csv|(222383, 4)|Complete dataset of all known, unknown and types of interactions|
known_drugs_names.csv|(89008, 3)|All of the confirmed DDIs with the name of their drugs, and types of interactions|
known_drugs.csv|(89008, 2)|The dataset of all known interactions, but represented as nodes for training|
structure_links.csv|(11912, 5)|All types of drugs and different types of nomenclature for their chemical structures|
ddinter_downloads_code_A.csv|(56367, 5)|Interactions involving alimentary tract and metabolism drugs|
ddinter_downloads_code_B.csv|(15140, 5)|Interactions involving blood and blood forming organs drugs
ddinter_downloads_code_D.csv|(25681, 5)|Interactions involving dermatological drugs
ddinter_downloads_code_H.csv|(11727, 5)|Interactions involving systemic hormonal preparations, excluding sex hormones and insulins drugs
ddinter_downloads_code_L.csv|(65389, 5)|Interactions involving antineoplastic and immunomodulating agents drugs
ddinter_downloads_code_P.csv|(5492, 5)|Interactions involving antiparasitic products, insecticides and repellents drugs
ddinter_downloads_code_R.csv|(30563, 5)|Interactions involving respiratory system drugs|
ddinter_downloads_code_R.csv|(12024, 5)|Interactions involving various drugs

### Modeling process

#### Feature Engineering

One thing to disclaim is that the Neural network is only based on known DDIs, no other information was required to train the model. For the XGboost and Logistic Regression, additional features were extracted from graph nodes. <br>

Before getting into the modeling for this task, a lot of preliminary research was done to provide a general scope of the optimal methodology on this particular problem. For this link prediction problem, I found that research is still very progressive and that the state-of-the-art performances are constantly changing due to introduced and improved methodologies. An intuitive approach is to extract features based on graph similarity indicators that are based on Jacard coefficients and Acadamic Adar coefficients. They both explore the neighbourhoods of the node pairs, and use that information as an indicator of similarity. Nodes are likely to be linked if they have a lot of similar neighbours.

In addition to this, the reason for collecting the chemical structures is to establish relationships between the structures of molecules and their corresponding biological activity i.e. DDIs. With this, a pairwise distance was calculated between each drug based on their chemical structures.



### Modeling
**Neural network** <br>
The approach that I've taken is to combine 2 subnetworks that are 2 approaches that explore the relationship of the drug pairs with addition and multiplication. The objective is to combine the generalised interactive term from the addition embedding to the more sophisticated interactive term from the multiplication embedding. This model is only reliant on DDIs,(node_a, node_b), and will define their relationships through embeddings that represent the 2 subnetworks.<br>


### Results
The Neural network was able to outperform the baseline and XGBoost, particularly in terms of minimising bias/variance. The model resulted with a 77% test accuracy, and a recall score of 77%, meaning that with 10 predicted interactions, roughly 8 were correctly labeled as an interaction and the 2 other interactions were misclassified. Additionally, the Area Under Curve (AUC) score was 0.85, which means that the model's ability to classify interactions correctly isn't at a standard that should be relied on.




## Next Steps
- From research, the results of the neural network model can be optimised even further by adjusting the weights that are applied within the embedding layers. Other methodology can also be explored that stem from Collaborative Filtering (recommender systems) that either use matrix factorisation or other Neural Network structures.

- Another suggestion is to change the composition of the test set to include completely new drugs, and integrate that into the workflow of feature engineering.
