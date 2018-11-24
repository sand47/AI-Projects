# Random Forest Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/datafull/train.csv')
test = pd.read_csv('/datafull/test.csv')

# use train.isnull().sum(axis=0)to see number of null 

train = train.fillna({"N_BEDROOM": train["N_BEDROOM"].mean(), "INT_SQFT": train["INT_SQFT"].mean(),
                     "N_BATHROOM": train["N_BATHROOM"].mean(), "QS_OVERALL": train["QS_OVERALL"].mean()})

test = test.fillna({"N_BEDROOM": test["N_BEDROOM"].mean(), "INT_SQFT": train["INT_SQFT"].mean(),
                     "N_BATHROOM": test["N_BATHROOM"].mean(), "QS_OVERALL": test["QS_OVERALL"].mean()})


train['diff_reg_comm'] = train['REG_FEE'] - train['COMMIS']
test['diff_reg_comm'] = test['REG_FEE'] - test['COMMIS']



from sklearn.preprocessing import LabelEncoder

lb_make = LabelEncoder()
train["AREA"] = lb_make.fit_transform(train["AREA"])
test["AREA"] = lb_make.fit_transform(test["AREA"])

train["SALE_COND"] = lb_make.fit_transform(train["SALE_COND"])
test["SALE_COND"] = lb_make.fit_transform(test["SALE_COND"])

train["PARK_FACIL"] = lb_make.fit_transform(train["PARK_FACIL"])
test["PARK_FACIL"] = lb_make.fit_transform(test["PARK_FACIL"])

train["BUILDTYPE"] = lb_make.fit_transform(train["BUILDTYPE"])
test["BUILDTYPE"] = lb_make.fit_transform(test["BUILDTYPE"])

train["UTILITY_AVAIL"] = lb_make.fit_transform(train["UTILITY_AVAIL"])
test["UTILITY_AVAIL"] = lb_make.fit_transform(test["UTILITY_AVAIL"])

train["STREET"] = lb_make.fit_transform(train["STREET"])
test["STREET"] = lb_make.fit_transform(test["STREET"])

train["MZZONE"] = lb_make.fit_transform(train["MZZONE"])
test["MZZONE"] = lb_make.fit_transform(test["MZZONE"])



feature_names = [x for x in train.columns if x not in ['PRT_ID','SALES_PRICE','DATE_SALE','DATE_BUILD']]
target = train['SALES_PRICE']

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 21))
train[feature_names] = scaler.fit_transform(train[feature_names])
test[feature_names] = scaler.fit_transform(test[feature_names])


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

X_tr, X_val, y_tr, y_val = train_test_split(train[feature_names], target,test_size = 0.2, random_state = 1)
# Feature Scaling

# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X, y)

# Predicting a new result
pred = model.predict(test[feature_names])

sub = pd.DataFrame()
sub['PRT_ID'] = test['PRT_ID']
sub['SALES_PRICE'] = pred
sub.to_csv('house_prices.csv', index=False)
