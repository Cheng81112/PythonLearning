'''
前向反馈
2-input neuron
sigmoid activation function
w=[0,1]
b=4
x=[2,3]
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

weight = np.array([0,1])
bias = 4
n = Neuron(weight,bias)

x = np.array([2,3])
print(n.feedforward(x))  # 0.9990889488055994

# np.dot的用法
