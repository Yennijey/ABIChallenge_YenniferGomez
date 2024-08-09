import pandas as pd

# Datos dummy del Titanic
data = {
    'PassengerId': [6, 7, 8, 9, 10],
    'Survived': [0, 1, 1, 0, 1],
    'Pclass': [2, 3, 1, 3, 2],
    'Name': ['Moran, Mr. James', 'McCarthy, Mr. Timothy J', 'Palsson, Master. Gosta Leonard', 'Johnson, Mrs. Oscar W', 'Nasser, Mrs. Nicholas'],
    'Sex': ['male', 'male', 'male', 'female', 'female'],
    'Age': [27, 54, 2, 27, 14],
    'SibSp': [0, 0, 1, 0, 1],
    'Parch': [0, 0, 1, 2, 0],
    'Ticket': ['330877', '17463', '349909', '347742', '237736'],
    'Fare': [8.4583, 51.8625, 21.075, 11.1333, 30.0708],
    'Embarked': ['Q', 'S', 'S', 'S', 'C']
}

# Crear DataFrame
df = pd.DataFrame(data)
print(df.describe())
