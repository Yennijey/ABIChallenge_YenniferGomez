import pandas as pd

def load_data():
    df = pd.read_csv('titanic.csv')
<<<<<<< HEAD
feature2
    print(df.describe())
=======
    print(df.head())
=======
feature1
    print(df.head())
=======
    print(df.describe())
>>>>>>> 96c9bdc505c99ad0f23cc93a03ea8e7c09d989a1
develop

if __name__ == '__main__':
    load_data()
