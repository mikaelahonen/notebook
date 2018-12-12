#Keras
Initial building block in Keras is a model.

Perceptrons
* Perceptron: A single linear layer.
* MLP: Multilayer perceptron.

Neuron is dense, if all nerves of a layer are connected all nerves of previous and net layer.

## Weights
Each neuron can be initialized with specific weights.
[Full list](https://keras.io/initializations/)

### random_uniform
Weights are initialized to uniformly random small values in
(-0.05, 0.05). In other words, any value within the given interval is equally likely
to be drawn.

### random_normal
Weights are initialized according to a Gaussian, with a zero
mean and small standard deviation of 0.05. For those of you who are not familiar
with a Gaussian, think about a symmetric bell curve shape.

### zero
All weights are initialized to zero.

## Activation functions
[Full list](https://keras.io/activations/)

