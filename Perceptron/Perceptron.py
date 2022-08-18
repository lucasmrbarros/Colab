class Perceptron(object):
  
  def __init__(self, alpha=0.1, epochs=10):
    np.random.seed(1) # [OBS1]
    self.alpha = alpha # alpha é a nossa taxa de aprendizado
    self.epochs = epochs
    self.weights = None
    self.bias = None
  
  def fit (self, X, Y):
    n_samples, n_features = X.shape
    # Inicialize os Pesos e Bias: [ATIVIDADE 1]


    for epoch in range(self.epochs):
      for x_i,y_esperado in zip(X,Y):
        # Defina as funções de treinamento: [ATIVIDADE 2]

    
    def predict(self, X):
    # Calcule o output do perceptron: [ATIVIDADE 3]

    return output

  def activation(self, signal):
    return np.where( signal >= 0, 1, 0) # Função degrau de ativação
        





