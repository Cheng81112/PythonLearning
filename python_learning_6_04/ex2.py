'''
feedforward
'''
import numpy as np
def sigmoid(x):
    # activation function: f(x)=1/(1+e^(-x))
    return 1/(1+np.exp(-x))
class Neuron:
    def __init__(self,weight,bias):
        self.weight = weight
        self.bias = bias

    def feedforward(self,inputs):
        total = np.dot(self.weight,inputs) + self.bias
        return sigmoid(total)

class OurNeuralNetwordk:
    '''
    - 2 inputs
    - a hidden layer with 2 neurons(h1,h2)
    - an output layer with 1 neuron (o1)
    each neuron has the same weights and bias:
    - w = [0,1]
    - b = 0
    '''
    def __init__(self,weight,bias):
        self.weight = weight
        self.bias = bias

        self.h1 = Neuron(weight,bias)
        self.h2 = Neuron(weight,bias)
        self.o1 = Neuron(weight,bias)

    def feedforward(self,x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)

        # the inputs for o1
        out_o1 = self.o1.feedforward(np.array([out_h1,out_h2]))
        return out_o1
weight = np.array([0,1])
bias = 0
network = OurNeuralNetwordk(weight,bias)

x = np.array([2,3])
print(network.feedforward(x))



# sys.setrecursionlimit(100000) # 例如这里设置为十万







