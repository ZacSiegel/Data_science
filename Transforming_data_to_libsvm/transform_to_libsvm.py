
import pandas as pd
import sklearn.datasets as sd


df = pd.read_csv("agaricus-lepiota.data", header=None)
#print(df)

class_labels = df[0].unique()
#print(f'The class labels are: {class_labels}')

# class label 0 for poisonous, 1 for edible
CL = {class_labels[0]: '0', class_labels[1]: '1'}
new_class_labels = df[0].map(CL)

# new dataframe with new class labels created 
new_df = pd.DataFrame()
new_df[0] = new_class_labels

col_count = 1
num_of_columns = len(df.columns)
for i  in range(1, num_of_columns):
    # column 11 is missing a lot of data, so we exclude it
    if i != 11:
        # this will convert each attribute into multiple binary attributes
        x = pd.get_dummies(df[i])
        # x.columns returns headers for new attributes
        for j in range(0, len(x.columns)):
            # getting new column from x and adding it to new dataframe
            new_df[col_count] = x[x.columns[j]]
            col_count += 1
        
print(new_df)

class_labels = new_df[0]
train_data = new_df.iloc[:, 1:len(new_df.columns)]


sd.dump_svmlight_file(train_data, class_labels, "mushroom_prepared_data.libsvm", False)