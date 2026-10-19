class ModelLayer:
    def __init__(self, layer_name, learning_rate=0.01, initial_weights=None):   
        if initial_weights is None:
            initial_weights = []    
        self.layer_name = layer_name
        self._learning_rate = learning_rate
        self.__weights = initial_weights

    def get_weights(self):
        return self.__weights.copy()

    def set_weights(self, new_weights):
        if new_weights is None:
            raise ValueError("Invalid weight values provided")

        if not all(isinstance(weight, (float)) for weight in new_weights):
            raise ValueError("Invalid weight values provided")

        self.__weights = new_weights.copy()


layer = ModelLayer("Dense_1", initial_weights=[0.25, -0.15, 0.40])

try:
    print(layer.__weights)  
except AttributeError as e:
    print(f"Error: {e}")


print(layer._ModelLayer__weights)


