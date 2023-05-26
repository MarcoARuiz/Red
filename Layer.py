# Clase de Capas
class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    # Calcula la salida Y de una capa en base a una entrada X
    def forward_propagation(self, input):
        raise NotImplementedError

    # Calcula dE/dX para una dE/dY. La que actualiza
    def backward_propasgation(self, output_error, learning_rate):
        raise NotImplementedError
    
