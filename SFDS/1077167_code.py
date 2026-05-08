import numpy as np
import sys

# read input values
Input_list = []
for line in sys.stdin:
    Input_list.append(float(line.strip()))

values = np.array(Input_list)

# split inputs and targets
feature_variable = values[:5].reshape(1,5)
Target = values[5:].reshape(1,3)

# learning rate
lr = 0.1

# initialise weights and biases
Weight_1 = np.ones((5,10))
bias_1 = np.ones((1,10))

Weight_2 = np.ones((10,3))
bias_2 = np.ones((1,3))

# sigmoid activation function
def sigmoid_func(input_value):
    """Takes a value and apply sigmoid function to it and return results """
    value_sig = 1 / (1 + np.exp(-input_value))
    return value_sig

# output of sigmoid function
def sigmoid_output(input_value):
    """Takes a value and apply the function to it and return results """
    value_sig_out = input_value * (1 - input_value)
    return value_sig_out


# feedforward step implementation

hidden = sigmoid_func(np.dot(feature_variable, Weight_1) + bias_1)
output = sigmoid_func(np.dot(hidden, Weight_2) + bias_2)

# Initial loss calculation
Initial_loss = 0.5 * np.sum((output - Target) ** 2)

# backpropagation implementation

output_error = (output - Target) * sigmoid_output(output)

dWeight_2 = np.dot(hidden.T, output_error)
dbias_2 = output_error

hidden_error = np.dot(output_error, Weight_2.T) * sigmoid_output(hidden) 

dWeight_1 = np.dot(feature_variable.T, hidden_error)
dbias_1 = hidden_error

# update weights
Weight_2 = Weight_2 - lr * dWeight_2
bias_2 = bias_2 - lr * dbias_2

Weight_1 = Weight_1 - lr * dWeight_1
bias_1 = bias_1 - lr * dbias_1

# backpropagation for outputs

hidden = sigmoid_func(np.dot(feature_variable, Weight_1) + bias_1)
output = sigmoid_func(np.dot(hidden, Weight_2) + bias_2)

final_loss = 0.5 * np.sum((output - Target) ** 2)

# results
print(np.round(Initial_loss,4))
print(np.round(final_loss,4))