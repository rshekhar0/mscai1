from math import exp
from random import seed, random

def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights': [random() for _ in range(n_inputs + 1)]} for _ in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights': [random() for _ in range(n_hidden + 1)]} for _ in range(n_outputs)]
    network.append(output_layer)
    return network

def activate(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    return activation

def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))

def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = transfer(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))

def transfer_derivative(output):
    return output * (1.0 - output)

def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network) - 1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])

def update_weights(network, row, learn_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += learn_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] += learn_rate * neuron['delta']

def train_network(network, train, learn_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for _ in range(n_outputs)]
            expected[int(row[-1])] = 1
            sum_error += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, learn_rate)
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, learn_rate, sum_error))

def back_propagation(train, test, l_rate, n_epoch, n_hidden):
    n_inputs = len(train[0]) - 1
    n_outputs = len(set([row[-1] for row in train]))
    network = initialize_network(n_inputs, n_hidden, n_outputs)
    train_network(network, train, l_rate, n_epoch, n_outputs)
    predictions = [predict(network, row) for row in test]
    return predictions

# User Input
seed(1)
hidden_neurons = int(input("Enter the number of hidden neurons: "))
learning_rate = float(input("Enter the learning rate: "))
epochs = int(input("Enter the number of training epochs: "))

# Example Dataset
dataset = [
    [2.7810836, 2.550537003, 0],
    [1.465489372, 2.362125076, 0],
    [3.396561688, 4.400293529, 0],
    [1.38807019, 1.850220317, 0],
    [3.06407232, 3.005305973, 0],
    [7.627531214, 2.759262235, 1],
    [5.332441248, 2.088626775, 1],
    [6.922596716, 1.77106367, 1],
    [8.675418651, -0.242068655, 1],
    [7.673756466, 3.508563011, 1]
]

n_inputs = len(dataset[0]) - 1
n_outputs = len(set([row[-1] for row in dataset]))
network = initialize_network(n_inputs, hidden_neurons, n_outputs)

# Feedforward
print("Feedforward:")
for row in dataset:
    output = forward_propagate(network, row)
    print(f"Input: {row[:-1]}, Predicted Output: {output}")

# Backpropagation
print("\nBackpropagation:")
for epoch in range(epochs):
    sum_error = 0
    for row in dataset:
        outputs = forward_propagate(network, row)
        expected = [0 for _ in range(n_outputs)]
        expected[int(row[-1])] = 1
        sum_error += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
        backward_propagate_error(network, expected)
        update_weights(network, row, learning_rate)
    print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, learning_rate, sum_error))

# Print final weights
print("\nFinal Weights:")
for i, layer in enumerate(network):
    print(f"\nLayer {i + 1} Weights:")
    for j, neuron in enumerate(layer):
        print(f"Neuron {j + 1} Weights: {neuron['weights']}")
