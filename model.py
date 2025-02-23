import tensorflow as tf
import numpy as np

# Load your trained model
model = tf.keras.models.load_model("saved_model\model_saved.h5")

def predict_heart_disease(features):
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return int(prediction[0][0] > 0.5)  # Convert probability to binary result (0 or 1)
