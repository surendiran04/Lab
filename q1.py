import numpy as np                                                                                                                                                      
                                                                                                                                                                        
import matplotlib.pyplot as plt                                                                                                                                         
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Sample data                                                                                                                                                           
                                                                                                                                                                        
X = np.array([1, 2, 3, 4, 5])  # Independent variable (input)                                                                                                           
                                                                                                                                                                        
y = np.array([2, 4, 5, 4, 5])  # Dependent variable (output)                                                                                                            
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Mean of X and y                                                                                                                                                       
                                                                                                                                                                        
mean_X = np.mean(X)                                                                                                                                                     
                                                                                                                                                                        
mean_y = np.mean(y)                                                                                                                                                     
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Calculate the coefficients (slope m and intercept b)                                                                                                                  
                                                                                                                                                                        
numerator = np.sum((X - mean_X) * (y - mean_y))                                                                                                                         
                                                                                                                                                                        
denominator = np.sum((X - mean_X) ** 2)                                                                                                                                 
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
m = numerator / denominator                                                                                                                                             
                                                                                                                                                                        
b = mean_y - (m * mean_X)                                                                                                                                               
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Regression line equation: y = mx + b                                                                                                                                  
                                                                                                                                                                        
print(f"Slope (m): {m}")                                                                                                                                                
                                                                                                                                                                        
print(f"Intercept (b): {b}")                                                                                                                                            
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Predict y values based on the model                                                                                                                                   
                                                                                                                                                                        
y_pred = m * X + b                                                                                                                                                      
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Function to predict y for a given x                                                                                                                                   
                                                                                                                                                                        
def predict(x):                                                                                                                                                         
                                                                                                                                                                        
    return m * x + b                                                                                                                                                    
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Test prediction for a specific x value                                                                                                                                
                                                                                                                                                                        
x_value = 6                                                                                                                                                             
                                                                                                                                                                        
predicted_y = predict(x_value)                                                                                                                                          
                                                                                                                                                                        
print(f"Predicted y for x = {x_value}: {predicted_y}")                                                                                                                  
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Plot the data and the regression line                                                                                                                                 
                                                                                                                                                                        
plt.scatter(X, y, color='blue', label='Data points')                                                                                                                    
                                                                                                                                                                        
plt.plot(X, y_pred, color='red', label='Regression line')                                                                                                               
                                                                                                                                                                        
plt.scatter(x_value, predicted_y, color='green', label=f'Predicted y for x={x_value}', zorder=5)                                                                        
                                                                                                                                                                        
plt.xlabel('X')                                                                                                                                                         
                                                                                                                                                                        
plt.ylabel('y')                                                                                                                                                         
                                                                                                                                                                        
plt.legend()                                                                                                                                                            
                                                                                                                                                                        
plt.show()                                                                                                                                                              
(file) [s2022103572@sflinuxonline 09.09.2024-00:12:01 - /wk6]$ cat mlr.py                                                                                               
import numpy as np                                                                                                                                                      
                                                                                                                                                                        
import matplotlib.pyplot as plt                                                                                                                                         
                                                                                                                                                                        
from mpl_toolkits.mplot3d import Axes3D                                                                                                                                 
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Sample data (two independent variables X1 and X2)                                                                                                                     
                                                                                                                                                                        
X1 = np.array([1, 2, 3, 4, 5])                                                                                                                                          
                                                                                                                                                                        
X2 = np.array([2, 3, 4, 5, 6])                                                                                                                                          
                                                                                                                                                                        
y = np.array([3, 5, 7, 9, 11])  # Dependent variable                                                                                                                    
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Combine X1 and X2 into a single matrix X                                                                                                                              
                                                                                                                                                                        
X = np.column_stack((X1, X2))                                                                                                                                           
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Add a column of ones to X to represent the intercept (b)                                                                                                              
                                                                                                                                                                        
X_b = np.column_stack((np.ones(X.shape[0]), X))                                                                                                                         
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Use least squares to calculate the coefficients (b0, b1, b2)                                                                                                          
                                                                                                                                                                        
theta, residuals, rank, s = np.linalg.lstsq(X_b, y, rcond=None)                                                                                                         
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Extract the coefficients                                                                                                                                              
                                                                                                                                                                        
b0, b1, b2 = theta                                                                                                                                                      
                                                                                                                                                                        
print(f"Intercept (b0): {b0}")                                                                                                                                          
                                                                                                                                                                        
print(f"Coefficient for X1 (b1): {b1}")                                                                                                                                 
                                                                                                                                                                        
print(f"Coefficient for X2 (b2): {b2}")                                                                                                                                 
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Predict y values based on the model                                                                                                                                   
                                                                                                                                                                        
y_pred = X_b.dot(theta)                                                                                                                                                 
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Function to predict y for given x1 and x2 values                                                                                                                      
                                                                                                                                                                        
def predict(x1, x2):                                                                                                                                                    
                                                                                                                                                                        
    return b0 + b1 * x1 + b2 * x2                                                                                                                                       
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Test prediction for specific x1 and x2 values                                                                                                                         
                                                                                                                                                                        
x1_value = 6                                                                                                                                                            
                                                                                                                                                                        
x2_value = 7                                                                                                                                                            
                                                                                                                                                                        
predicted_y = predict(x1_value, x2_value)                                                                                                                               
                                                                                                                                                                        
print(f"Predicted y for x1 = {x1_value}, x2 = {x2_value}: {predicted_y}")                                                                                               
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# 3D plot for visualization                                                                                                                                             
                                                                                                                                                                        
fig = plt.figure()                                                                                                                                                      
                                                                                                                                                                        
ax = fig.add_subplot(111, projection='3d')                                                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Plot original data points                                                                                                                                             
                                                                                                                                                                        
ax.scatter(X1, X2, y, color='blue', label='Data points')                                                                                                                
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Create a grid for plotting the regression plane                                                                                                                       
                                                                                                                                                                        
X1_grid, X2_grid = np.meshgrid(np.linspace(min(X1), max(X1), 10), np.linspace(min(X2), max(X2), 10))                                                                    
                                                                                                                                                                        
y_grid = b0 + b1 * X1_grid + b2 * X2_grid                                                                                                                               
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Plot the regression plane                                                                                                                                             
                                                                                                                                                                        
ax.plot_surface(X1_grid, X2_grid, y_grid, color='red', alpha=0.5)                                                                                                       
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Plot the predicted point                                                                                                                                              
                                                                                                                                                                        
ax.scatter(x1_value, x2_value, predicted_y, color='green', label=f'Predicted y for x1={x1_value}, x2={x2_value}', s=100)                                                
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
ax.set_xlabel('X1')                                                                                                                                                     
                                                                                                                                                                        
ax.set_ylabel('X2')                                                                                                                                                     
                                                                                                                                                                        
ax.set_zlabel('y')                                                                                                                                                      
                                                                                                                                                                        
plt.legend()                                                                                                                                                            
                                                                                                                                                                        
plt.show()
