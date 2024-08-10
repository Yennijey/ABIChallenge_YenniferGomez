from model import ModeloTitanic

# Instanciar y entrenar el modelo
modelo_titanic = ModeloTitanic()
modelo_titanic.entrenar()

def obtener_prediccion(pclass, sex, age):
    # Convertir sex a un valor numérico, como se hizo en el modelo
    sex_encoded = 1 if sex.lower() == 'male' else 0
    entrada = [pclass, sex_encoded, age]
    return modelo_titanic.predecir(entrada)
