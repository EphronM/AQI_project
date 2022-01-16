
# Air Quality Index-Prediction

Based on the climate data of BANGALORE city from 2016 till 2020, created a Prediction model which could tell the AQI based on the required inputs.


END-END model has been deployed on Heroku platform for public asses.

**[Site Link](https://airqualityindex9.herokuapp.com/)**




![home page](https://user-images.githubusercontent.com/94764266/149657817-330ab4bf-9e5d-4484-858f-bc5c446dff94.JPG)

## Data Collection

The Whole data set was webscrapped from [TuTiempo](https://en.tutiempo.net/) a weather website.


> * The URL https://en.tutiempo.net/climate/09-2020/ws-432950.html contains html pages where "09" means the month Sept and "2020" indicated the Year. The Last code "432950" presents the city code.

Based on these information, the HTML pages which contains the whole data based on every month was retrieved for the years 2016 - 2020 using python scripts

Using **Beautiful Soup** the Html page was scrapped. The data was cleaned during extraction. The data from Tutiempo only contains the features for the model AQI values need to be found elsewhere.

The AQI data of bangalore was downloaded from [aqicn](https://aqicn.org/data-platform/register/) as csv. The AQI csv contains data for each hour per day. The hourly data needed to be averaged to get per day mean.

After Preprocessing, both the data was combined and exported as "Real_combined.csv"

## EDA

After Collection the data, it was imported as pandas dataframe for data visualisation.

![download](https://user-images.githubusercontent.com/94764266/148679682-b6a55a9f-387a-4469-8547-72dece0c75b6.png)
 
Many insights were captured based on the pairplot.

The most important features were extracted using the **ExtraTreesRegressor** by sklearn. Using those data, a barchart was ploted.

![download (1)](https://user-images.githubusercontent.com/94764266/148679815-83a8dc7e-206e-4352-893a-18fc48c60b76.png)

* The features **tm** (Min temperature) plays an important role.


![download (2)](https://user-images.githubusercontent.com/94764266/148679886-fbea4c0e-d7f3-411a-8e63-2b32dd4732fc.png)

The Output variables are distributed in right squeezed distribution.


## ML algorithm 
* Linear Regression
* Lasso & Reidge Regression
* Decision Tree Regression
* KNN Regression
* Random Forest
* XGBoost Regression
* ANN algorithm

All these algorithms were used to fit the training data to find the best model of greater accuracy.

During the Implemtation of Decision Tree, 

![download (3)](https://user-images.githubusercontent.com/94764266/148680090-cde7d520-d9ab-4503-8f2e-cff73c1286fb.png)

The Tree was ploted for better visualisation.

* Among the ML models, RandomForest and XGBoost Regressor gave better accuracy when compared.
Random Forest gave an accuracy of **83%**. Thus, the rf_model was pickled for deployment.

## Auto ML - TPOT

A autoML model was Implemtation to understand the possiblities of better accuracy.

After running the model for 10mins, the tpot gave an accuracy of **80%** using the model, 


```bash
Pipeline(steps=[('maxabsscaler', MaxAbsScaler()),
    ('kneighborsregressor',
      KNeighborsRegressor(n_neighbors=31, weights='distance'))])
```

## Flask API

Using the Flask framework, a web based app was build, which lets the user enter inputs like:
* Average Temperature 
* Maximum Temperature
* Minimum Temperature
* Average WindSpeed
* Max Sustained WindSpeed

with these inputs from the html form, the data is passed on to the model for prediction,
The predicted result will then be displayed on the top.

## Deployment

The model was deployed to a container-based cloud Platform as a Service (**PaaS**).

![heroku_logo](https://user-images.githubusercontent.com/94764266/148681433-085df2ca-a855-4dd1-a659-8315b7c02829.png)

The whole API was pushed to Heroku for deployment.
