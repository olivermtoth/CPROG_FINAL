"""
Price predicting model. preddicitng the price of the stock for the following market day,
using an LSTM-Attention model.
"""
import tensorflow as tf


# https://www.tensorflow.org/api_docs/python/tf/keras/Model
# https://cs230.stanford.edu/projects_winter_2020/reports/32066186.pdf
import tensorflow as tf

class AttentionsLSTM(tf.keras.Model):
    def __init__(self, num_units, num_classes, lstm_dropout_rate=0.1, attention_dropout_rate=0.1, output_dropout_rate=0.1):
        super(AttentionsLSTM, self).__init__()
        
        # Define the LSTM layer
        self.lstm_layer = tf.keras.layers.LSTM(units=num_units, return_sequences=True, dropout=lstm_dropout_rate)
        
        # Define the attention mechanism
        self.attention_layer = tf.keras.layers.Dense(units=num_units, activation='tanh')
        self.attention_dropout = tf.keras.layers.Dropout(rate=attention_dropout_rate)
        self.attention_weight_layer = tf.keras.layers.Dense(units=1, activation='softmax')
        
        # Define the reshape layer
        self.reshape_layer = tf.keras.layers.Reshape((-1, num_units))
        
        # Define the output layer
        self.output_layer = tf.keras.layers.Dense(units=num_classes, activation='softmax')
        self.output_dropout = tf.keras.layers.Dropout(rate=output_dropout_rate)
        
    def call(self, inputs):
        # Reshape the inputs
        reshaped_inputs = self.reshape_layer(inputs)
        
        # Pass the inputs through the LSTM layer
        lstm_output = self.lstm_layer(reshaped_inputs)
        lstm_output_dropout = self.lstm_dropout(lstm_output)
        
        # Calculate the attention weights
        attention_layer_output = self.attention_layer(lstm_output_dropout)
        attention_layer_output_dropout = self.attention_dropout(attention_layer_output)
        attention_weights = self.attention_weight_layer(attention_layer_output_dropout)
        
        # Apply the attention weights to the LSTM output
        weighted_output = tf.reduce_sum(tf.multiply(lstm_output_dropout, attention_weights), axis=1)
        weighted_output_dropout = self.output_dropout(weighted_output)
        
        # Pass the weighted output through the output layer
        output = self.output_layer(weighted_output_dropout)
        
        return output



