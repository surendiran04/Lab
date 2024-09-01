import numpy as np

# Define the Unit Step Function
def unitStep(v):
    return np.where(v >= 0, 1, 0)

# Define the Perceptron Model for a single layer
def perceptronModel(X, y, learning_rate=0.1, epochs=10):
    n_samples, n_features = X.shape
    # Initialize weights and bias
    w = np.zeros(n_features)
    b = 0

    # Training process
    for _ in range(epochs):
        for idx, x_i in enumerate(X):
            # Linear combination
            linear_output = np.dot(x_i, w) + b
            # Prediction
            y_pred = unitStep(linear_output)
            # Update rule
            update = learning_rate * (y[idx] - y_pred)
            w += update * x_i
            b += update

    return w, b

# Prediction function for single-layer perceptron
def predict(X, w, b):
    linear_output = np.dot(X, w) + b
    return unitStep(linear_output)

# XOR using Multi-Layer Perceptron
def XOR_logicFunction(X):
    # First layer weights and biases
    w1 = np.array([[1, 1], [1, 1]])
    b1 = np.array([-0.5, -1.5])

    # Second layer weights and biases
    w2 = np.array([1, -2])
    b2 = 0.5

    # First layer outputs
    z1 = np.dot(X, w1.T) + b1
    a1 = unitStep(z1)

    # Second layer output
    z2 = np.dot(a1, w2) + b2
    output = unitStep(z2)
    
    return output

# Define training and testing data for each logic gate
def test_logic_gates():
    # Training data for AND, OR, NOR
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    # Labels for each gate
    y_AND = np.array([0, 0, 0, 1])  # AND gate
    y_OR = np.array([0, 1, 1, 1])   # OR gate
    y_NOR = np.array([1, 0, 0, 0])  # NOR gate

    # Training and testing the perceptron for AND gate
    print("\nAND Gate:")
    w_AND, b_AND = perceptronModel(X, y_AND)
    for x in X:
        print(f"Input: {x}, Predicted Output: {predict(x, w_AND, b_AND)}")

    # Training and testing the perceptron for OR gate
    print("\nOR Gate:")
    w_OR, b_OR = perceptronModel(X, y_OR)
    for x in X:
        print(f"Input: {x}, Predicted Output: {predict(x, w_OR, b_OR)}")

    # Training and testing the perceptron for NOR gate
    print("\nNOR Gate:")
    w_NOR, b_NOR = perceptronModel(X, y_NOR)
    for x in X:
        print(f"Input: {x}, Predicted Output: {predict(x, w_NOR, b_NOR)}")

    # Testing XOR using Multi-Layer Perceptron
    print("\nXOR Gate:")
    for x in X:
        print(f"Input: {x}, Predicted Output: {XOR_logicFunction(x)}")

# Run the tests
if __name__ == "__main__":
    test_logic_gates()
