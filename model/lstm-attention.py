"""
Price predicting model. preddicitng the price of the stock for the following market day,
using an LSTM-Attention model.
"""
import tensorflow as tf


# https://www.tensorflow.org/api_docs/python/tf/keras/Model
# https://cs230.stanford.edu/projects_winter_2020/reports/32066186.pdf
class LSTM_Attention_1day(tf.keras.Model):
    """
    Class predicting the price from one trading day from now.
    """

    def __init__(self):
        super().__init__()
        self.dense = tf.keras.layers.Dense(unit=6)  # Input layer
        self.lstm = tf.keras.layers.LSTM()  # Long/Short Term Memory Layer
        self.attention = tf.keras.layers.Attention()  # Attention Layer
        self.output = self.dense(unit=1)  # Output layer

    def call(self, input, training=True):
        """
        Call method for compute the predicted price
        """
        x = self.dense(input)
        x = self.lstm(x)
        x = self.attention(x)
        return self.output(x)



