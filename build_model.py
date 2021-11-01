import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle


def main():
    # Get the dataset from the users GitHub repository
    dataset_path = "input/creditcard.csv"
    creditcard_data = pd.read_csv(dataset_path)

    # Get model
    X = creditcard_data.drop('Class', axis='columns').values
    Y = creditcard_data.Class.values
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.33, random_state=42)
    logistic = linear_model.LogisticRegression(class_weight='balanced')
    logistic.fit(Xtrain, Ytrain)

    print("\nModel Training Finished")
    accuracy = logistic.score(Xtest, Ytest)
    print("\nAccuracy of the Model: "+str(accuracy*100))

    if logistic:
        pickle.dump(logistic, open('model.pkl', 'wb'))


if __name__ == "__main__":
    main()
