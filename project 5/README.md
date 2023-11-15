### Problem Statement
The U.S. Department of Housing and Urban Development (HUD) provides counseling services for persons who seek guidance with housing issues or topics such as reverse mortgages, pre-purchase decisions or foreclosures and delinquencies. Providing these services require a lot of resources and it’s important to accommodate for the populations that are in need (by state). We've created a user-friendly interactive dashboard that will predict the level of engagement towards HUD services at the U.S. state level. The goal is for HUD to reference the dashboard to gauge a better understanding of regional needs associated to housing issues in order to allocate personnel and monetary resources even more effectively.

### How we achieved this:
We firstly made an index that represented a combination of chosen predictors that represented housing affordability and economic health --> This was forecasted using a VAR model for each state --> Comparison of current vs forecasted index indicates the future demand of a service.

### Annotation of Notebooks
1 = Data Cleaning <br>
2 = Exploratory Data Analysis <br>
3 = Modeling processes

### Description of Data
|CSV|Description|
|---|---|
|chained_cpi.csv|Consumer Price Indexs- shelter, all items, all items less food and energy
|continued_claims_by_state.csv|The amount of unemployment continued claims by state
|continued_unemployment_rate_by_state.csv|The unemployment continued claims rate by state
|covered_employees_by_state.csv| Number of covered employees by state
|delinquency_join_to_hud_data.csv| Preparatory dataset for tableau integration. Includes results from the VAR models by state i.e. current index, forecasted index, and evaluation metrics being RMSE, MAE and MAPE
|household_dti_by_state.csv| Household debt to income ratio by state
|hpi_state.csv| House Pricing Index by state
|hud_data_geo.csv| Latitude and Longitude of HUD agencies
|hud_data.csv| Descriptive data on location, address, and types of services provided by each HUD agency. Also has results of VAR models applied.
|initial_claims_by_state.csv| The amount of unemployment initial claims by state.
|initial_unemployment_rate_by_state.csv| The unemployment intitial claims rate by state
|mba_purchase_index_mth.csv| Monthly purchase index
|mba_purchase_index_wk.csv| Weekly purchase index
|mortgage_rates.csv| Mortgage rates (30 year fixed, 15 year fixed, 5/1 adjustable)
|national_metrics.csv| Aligned version of all of the national metrics starting from 2010 i.e. purchase index, consumer price indexes, mortgage rates, gdp, personal income, population, household debt to income ratio, housing price index, insured employees, inital and continued claims rates.
|nominal_gdp_by_state.csv| Nominal Gross Domestic Product by state
|oecd_hpi_by_state.csv| Housing price index by state. 2 versions are kept as there would be merging issues
|per_capita_income_by_state.csv| Per capita income by state
|personal_income_by_state.csv| Personal income by state
|population_by_state.csv| Population by state
|prepurchase_join_to_hud_data.csv| Pre-purhcase
|shelter_cpi.csv| Consumer price index for shelter
|state_level_metrics.csv| Final dataset outlining all state-level metrics that are considered for our predictive modeling. Metrics outlined in 'Predictors' section below.
|unemployment_cleaned.csv| Unemployment rate by state




### Predictors

**Delinquency Index**

The index represents the need for HUD deliquency and foreclosure services. These metrics are taken from state_level_metrics.csv

|Feature|Type|Description|
|---|---|---|
|personal_income|numeric|Personal income
|per_capita_income|numeric| Per capita income
|nominal_gdp|numeric| nominal gross domestic product
|household_dti|numeric| household debt to income ratio
|initial_claims|numeric| Unemployment insurance (initial claims)
|continued_claims|numeric| Unemployment insurance (continued claims)
|insured_employees|numeric| Number of insured unemployed people
|purchase_index|numeric| National Purchase Index
|all_items|numeric| National Consumer Price Index


<br>

**Pre-purchase Index**

The index represents the need for HUD pre-purchase services. These metrics are taken from state_level_metrics.csv

|Feature|Type|Description|
|---|---|---|
|personal_income|-|-
|per_capita_income|-|-
|nominal_gdp|-|-
|household_dti|-|-
|housing_price_index|-|-
|initial_claims|-|-
|continued_claims|-|-
|insured_employees|-|-
|purchase_index|-|-
|all_items|-|-
|**fixed_mortgage_30**|numeric|National 30 year fixed mortgage rate
|**fixed_mortgage_15**|numeric|National 15 year fixed mortgage rate
|**adjustable_mortgage**|numeric|National 5/1 adjustable mortgage





### Recommendations and Conclusions
**Conclusion:** <br>
To explore the outcome of our predictions by state: https://public.tableau.com/views/hud_counseling_services/Navigation?:language=en-US&:display_count=n&:origin=viz_share_link
<br> <br>
We had faced some limitations within the data collection and modelling processes. In regards to data collection, we sourced many data sets with varying formatting, time frames, and some not meeting our requirement for state-wide data. Modelling limitations were mostly because of the time constraint which meant that revising earlier steps wasn't that affordable. The dashboard that we've created is an indicator of regional demand for deliquency and pre-purchase HUD services and will hopefully increase accessibility for U.S citizens in need.


**Recommendations:** <br>
- Improve the interpretability of the indices to quantify how much more or less citizens will need assistance in a given state.
<br>
- Aim is for HUD to reference this dashboard and predictive model to proactively address problems that American homeowners and homebuyers have by effectively re-allocating personnel and monetary resources.
