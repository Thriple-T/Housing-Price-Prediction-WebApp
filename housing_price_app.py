import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import pickle

df=pd.read_csv("train.csv")

selective_df= df[['LotArea', 'OverallQual', 'OverallCond',
                'YearBuilt', 'YearRemodAdd', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea',
                'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
                'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars',
                'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
            'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold', 'SalePrice']]

#splitting features and labels
X=selective_df.drop(columns=["SalePrice"],axis=1)
y=selective_df['SalePrice']

#training a model
linear = LinearRegression()
linear.fit(X,y)

# generate a model
with open('house_pricing_model.pkl','wb') as f:
    pickle.dump(linear,f)

print("Done")
