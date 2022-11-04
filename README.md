## real-estate-price-prediction

## Description

in the first part of the project getting the dataframe of properties for sale in Belguim (appartement and house) from immoweb.be website.
Analysing an Visulization: 
After setting the data base of the properties cleaning it and analyzing it to study the correlation between different factors. Taking the price as target key and 
analyse the impact of other features on it. As result we found that feature (house type, heating type and prorerty condition) have significant impact on the price of 
properties in Belgium.
In Machine learning: create two modules to predict the price of the properties adding more features to increase the accurecy of the modules we used (propert type,
heating type, provinance, zip code, instruction year, land surface and kitchen type)  with accuracy score of 34% with the first module which using linear regression and
label encoding and 70% with the second module using onehotencoder and Random Forest Regression on test data.
In Deployment: we adapting the module by using pipeline in order to build an API using Flask where the user can provide his property features and hae the estimated 
predicted price with accurcy of 70%.

## Installation

The project has been coded in Python 3.10.2 Flask==2.2.2 

## Future Development

Deploy a Web Application with Docker and Render

## Contributors

AbuSharekh Maysa

## Personal situation

Junior Data Scientist at BeCode in Ghent.


