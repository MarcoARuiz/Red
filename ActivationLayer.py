from Layer import Layer
import numpy as np

# Hereda los elementos de la clase Layer
class ActivationLayer(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    # Regresa la entrada
    def forward_propagation(self, input_data):
        self.input = input_data
        self.output = self.activation(self.input)
        return self.output

    # Regresa el error de entrada =dE/dX para un error de salida=dE/dY.
    # No se aprende aqui por lo que no se ocupa el learning rate
    def backward_propagation(self, output_error, learning_rate):
        return self.activation_prime(self.input) * output_error