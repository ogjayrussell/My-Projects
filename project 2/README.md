#### Problem Statement
What parts of the house are most beneficial to renovate in regards to its’ contribution to sale price? This would be handy for people who are looking to sell their house and wondering what could be renovated to increase value or property developers who are making more profitable developments by focusing resources on the right areas.


Models used: lasso, ridge and linear regression for

--> to predict: saleprice with renovatable features to extract coefficients that represent the importance of each feature.

#### Description of Data
**train_clean :** <br>
Data set containing Ames houses without np.nan values.

Size = (2051,19)




#### Data Dictionary

|Feature|Type|Description|
|---|---|---|
|exter_qual|obj|Overall quality of the exterior of the house|
|bsmt_qual|obj|Basement quality|
|kitchen_qual|obj|Kitchen quality|
|fireplace_qu|obj|Fireplace quality|
|garage_qual|obj|Garage Quality|
|heating_qc|obj|Heating Quality|
|exter_cond|obj|Exterior condition|
|bsmt_cond|obj|Basement Condition|
|garage_cond|obj|Garage Condition|
|bsmtfin_type_1|obj|Quality of basement finished area|
|bsmtfin_type_2|obj|Quality of second finished area (if present)|
|heating|obj|Type of heating |
|paved_drive|obj|Paved driveway|
|fence|obj|Fence quality: privacy, material|
|roof_matl|obj|roof material|
|garage_finish|obj|Interior finish of garage|
|utilities|obj|Amount of utilities in the house|
|alley|obj|Alley access to property|
|saleprice|int|Price the house was sold for|


#### Recommendations and Conclusions
**Conclusion:** <br>
Out of the 3 models, the RidgeCV performed the best with the least amount of bias and with an R2 of 0.81. I wouldn't use this model for personal investment decisions as the coefficients have lost some meaning due to multi-collinearity issues.

The overall_quality feature had the highest coefficient that indicated an increase in price by $12,877.43 when upgrading in an increment of quality which confirms the importance of improving the quality of the house by means of renovation.

Although the model is adequately performing, the results have been decided to be misleading. BUT if we were to interpret this model, we would recommend to property developers/ persons selling their homes that their kitchen is priority to renovate, followed by heating, basement and  fireplace to add at least $2679.48 to their saleprice.


**Recommendations:** <br>
Although not as reliable, our findings can be used as a rough reference for recommendations.

Tedious trial and error was required when carefully creating interaction terms that wouldn't interfere with multicollinearity. More time working on this would eventually reduce bias further. Polynomial features were tested on this model but it had skewed our results completely.
