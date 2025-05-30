import math
import random

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(output):
    return output * (1 - output)

# Initialize network with random weights
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = []
    # Hidden layer
    hidden_layer = [{'weights': [random.uniform(-1, 1) for _ in range(n_inputs + 1)]} for _ in range(n_hidden)]
    network.append(hidden_layer)
    # Output layer
    output_layer = [{'weights': [random.uniform(-1, 1) for _ in range(n_hidden + 1)]} for _ in range(n_outputs)]
    network.append(output_layer)
    return network

# Forward propagation
def forward_propagate(network, inputs):
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = neuron['weights'][-1]  # Bias
            for i in range(len(inputs)):
                activation += neuron['weights'][i] * inputs[i]
            neuron['output'] = sigmoid(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

# Backward propagation of error
def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = []
        if i == len(network) - 1:  # output layer
            for j, neuron in enumerate(layer):
                error = expected[j] - neuron['output']
                errors.append(error)
        else:  # hidden layer
            for j, neuron in enumerate(layer):
                error = sum(next_neuron['weights'][j] * next_neuron['delta']
                            for next_neuron in network[i + 1])
                errors.append(error)
        for j, neuron in enumerate(layer):
            neuron['delta'] = errors[j] * sigmoid_derivative(neuron['output'])

# Update weights using error delta
def update_weights(network, row, learning_rate):
    inputs = row
    for i, layer in enumerate(network):
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in layer:
            for j in range(len(inputs)):
                neuron['weights'][j] += learning_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] += learning_rate * neuron['delta']  # bias

# Train the network
def train_network(network, dataset, learning_rate, n_epoch):
    for epoch in range(n_epoch):
        total_error = 0
        for row in dataset:
            inputs = row[:-1]
            expected = [row[-1]]
            outputs = forward_propagate(network, inputs)
            total_error += sum((expected[i] - outputs[i]) ** 2 for i in range(len(expected)))
            backward_propagate_error(network, expected)
            update_weights(network, inputs, learning_rate)
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}, Error: {total_error:.6f}")

def predict(network, row):
    outputs = forward_propagate(network, row)
    return [round(output) for output in outputs]

dataset = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

n_inputs = 2
n_hidden = 2
n_outputs = 1
learning_rate = 0.5
n_epoch = 10000

network = initialize_network(n_inputs, n_hidden, n_outputs)
train_network(network, dataset, learning_rate, n_epoch)

print("\nPredictions:")
for row in dataset:
    prediction = predict(network, row[:-1])
    print(f"{row[:-1]} => {prediction}")
