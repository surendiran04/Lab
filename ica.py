from sklearn.decomposition import FastICA
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data (mixture of signals)
np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

# Two source signals: sinusoidal and square signal
s1 = np.sin(2 * time)  # Sinusoidal signal
s2 = np.sign(np.sin(3 * time))  # Square signal

# Stack signals into a 2D array
S = np.c_[s1, s2]

# Mix signals
A = np.array([[1, 1], [0.5, 2]])  # Mixing matrix
X = np.dot(S, A.T)  # Generate observations by mixing the signals

# Apply FastICA to recover the original sources
ica = FastICA(n_components=2)
S_ = ica.fit_transform(X)  # Recovered signals
A_ = ica.mixing_  # Estimated mixing matrix

# Plot the results
plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.title("Original Signals")
plt.plot(S)

plt.subplot(3, 1, 2)
plt.title("Mixed Signals (Observations)")
plt.plot(X)

plt.subplot(3, 1, 3)
plt.title("Recovered Signals by ICA")
plt.plot(S_)

plt.tight_layout()
plt.show()
