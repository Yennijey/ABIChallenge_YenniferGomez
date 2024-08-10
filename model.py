import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

class ModeloTitanic:
    def __init__(self):
        self.modelo = DecisionTreeClassifier()
        self.encoder = LabelEncoder()

    def entrenar(self):
        # Cargar los datos del Titanic
        df = pd.read_csv('titanic.csv')
        
        # Preprocesamiento simple
        df['Sex'] = self.encoder.fit_transform(df['Sex'])
        df = df[['Pclass', 'Sex', 'Age', 'Survived']].dropna()

        X = df[['Pclass', 'Sex', 'Age']]
        y = df['Survived']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Entrenar el modelo
        self.modelo.fit(X_train, y_train)

    def predecir(self, entrada):
        return self.modelo.predict([entrada])[0]
