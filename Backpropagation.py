import csv
import numpy as np

#Sigmoid Function
def transfer(x): #this function maps any value between 0 and 1
    return 1/(1 + np.exp(-x))

#Derivative of Sigmoid Function
def transfer_derivative(x):
    return x * (1 - x)

lines = csv.reader(open('../input/Dataset4.csv'))
dataset = list(lines)
for i in range(len(dataset)):
    dataset[i] = [float(x) for x in dataset[i]]

epoch = 50
lrate = 0.5
n_inputs = len(dataset[0]) - 1
n_hidden = 2
n_outputs = 1

#initialize network
hidden_w = np.random.uniform(size=(n_hidden, n_inputs))
hidden_b = np.random.uniform(size=(n_hidden, 1))
output_w = np.random.uniform(size=(n_outputs, n_hidden))
output_b = np.random.uniform(size=(n_outputs, 1))
print('Hidden weights: ', hidden_w)
print('Hidden bias: ', hidden_b)
print('Output weights: ', output_w)
print('Output bias: ', output_b)
print()

for i in range(epoch):
    l = list()
    sum_error = 0
    for row in dataset:
        #forward prop
        ip = np.array(row[0:len(row)-1])[np.newaxis]
        ip = ip.T
        hip = np.dot(hidden_w, ip) + hidden_b
        hop = transfer(hip)
        op = np.dot(output_w, hop) + output_b
        output = transfer(op)
        
        #displaying output. Remove asscalar if n_outputs > 1.
        l.append((np.asscalar(output), row[-1]))
        sum_error += (row[-1] - output)**2
        
        #back prop
        EO = row[-1] - output
        delta_output = EO * transfer_derivative(output)
        EH = np.dot(output_w.T, delta_output)
        delta_hidden = EH * transfer_derivative(hop)
        
        #update weight
        output_w += np.dot(delta_output, hop.T) * lrate
        output_b += lrate * delta_output
        hidden_w += np.dot(delta_hidden, ip.T) * lrate
        hidden_b += lrate * delta_hidden
        
    print('Epoch: ', i)
    print('Error: ', sum_error)
    print(l)
    print()