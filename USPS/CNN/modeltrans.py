from tensorflow.keras.models import load_model
from tensorflow.python.keras import backend as k
import tensorflow as tf


model = load_model('./model/normalinandroid_cnn.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("./model/normalinandroid_cnn.tflite", "wb").write(tflite_model)
