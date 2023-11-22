import numpy as np
import os
import tensorflow as tf

# Generar datos para la nueva ecuación
X = np.linspace(0, 10, 100)  # Valores de x de 0 a 10
y = 2 * X + 1 + np.random.normal(scale=2, size=len(X))  # Agregamos ruido para hacerlo más realista

# Dividir los datos en conjuntos de entrenamiento, validación y prueba
train_end = int(0.6 * len(X))
test_start = int(0.8 * len(X))

X_train, y_train = X[:train_end], y[:train_end]
X_test, y_test = X[test_start:], y[test_start:]
X_val, y_val = X[train_end:test_start], y[train_end:test_start]

# Limpiar la sesión de Keras
tf.keras.backend.clear_session()

# Definir el modelo
linear_model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1], name='Single')
])

# Compilar el modelo
linear_model.compile(optimizer=tf.keras.optimizers.SGD(), loss=tf.keras.losses.mean_squared_error)

# Imprimir el resumen del modelo
print(linear_model.summary())

# Entrenar el modelo
linear_model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20)

# Hacer predicciones
predictions = linear_model.predict(np.array([[0.0], [2.0], [3.1], [4.2], [5.2]]))
print(predictions.tolist())

# Guardar el modelo
export_path = 'linear-model/1/'
tf.saved_model.save(linear_model, os.path.join('./', export_path))
