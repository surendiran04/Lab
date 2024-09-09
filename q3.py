import numpy as np                                                                                                                                                      
                                                                                                                                                                        
def sigmoid(x):                                                                                                                                                         
                                                                                                                                                                        
        return 1.0 / (1.0 + np.exp(-x))                                                                                                                                 
                                                                                                                                                                        
def sigmoid_prime(x):                                                                                                                                                   
                                                                                                                                                                        
        return x * (1.0 - x)                                                                                                                                            
                                                                                                                                                                        
epochs = 5000                                                                                                                                                           
                                                                                                                                                                        
input_size, hidden_size, output_size = 2, 3, 1                                                                                                                          
                                                                                                                                                                        
learning_rate = 0.1                                                                                                                                                     
                                                                                                                                                                        
# Truth table                                                                                                                                                           
                                                                                                                                                                        
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])                                                                                                                          
                                                                                                                                                                        
Y = np.array([[0], [1], [1], [0]])                                                                                                                                      
                                                                                                                                                                        
# Fill hidden and output layers with random values.                                                                                                                     
                                                                                                                                                                        
w_hidden = np.random.uniform(size=(input_size, hidden_size))                                                                                                            
                                                                                                                                                                        
w_output = np.random.uniform(size=(hidden_size, output_size))                                                                                                           
                                                                                                                                                                        
# Learning iteration                                                                                                                                                    
                                                                                                                                                                        
for epoch in range(epochs):                                                                                                                                             
                                                                                                                                                                        
        # Forward propagation                                                                                                                                           
                                                                                                                                                                        
        actual_hidden = sigmoid(np.dot(X, w_hidden))                                                                                                                    
                                                                                                                                                                        
        output = np.dot(actual_hidden, w_output)                                                                                                                        
                                                                                                                                                                        
        # Calculate error (expected output - calculated output)                                                                                                         
                                                                                                                                                                        
        error = Y - output                                                                                                                                              
                                                                                                                                                                        
        # Backward Propagation                                                                                                                                          
                                                                                                                                                                        
        dZ = error * learning_rate                                                                                                                                      
                                                                                                                                                                        
        w_output += actual_hidden.T.dot(dZ)                                                                                                                             
                                                                                                                                                                        
        dH = dZ.dot(w_output.T) * sigmoid_prime(actual_hidden)                                                                                                          
                                                                                                                                                                        
        w_hidden += X.T.dot(dH)                                                                                                                                         
                                                                                                                                                                        
        # Print the outputs for each step (epoch)                                                                                                                       
                                                                                                                                                                        
        if epoch % 100 == 0:  # Print every 100 epochs                                                                                                                  
                                                                                                                                                                        
                print(f"Epoch {epoch}:")                                                                                                                                
                                                                                                                                                                        
                for i in range(len(X)):                                                                                                                                 
                                                                                                                                                                        
                        actual_hidden = sigmoid(np.dot(X[i], w_hidden))                                                                                                 
                                                                                                                                                                        
                        actual_output = np.dot(actual_hidden, w_output)                                                                                                 
                                                                                                                                                                        
                        print(f'Input: {X[i]} Predicted Output: {actual_output}')                                                                                       
                                                                                                                                                                        
# Final Output after training                                                                                                                                           
                                                                                                                                                                        
print("\nFinal Output after training:")                                                                                                                                 
                                                                                                                                                                        
for i in range(len(X)):                                                                                                                                                 
                                                                                                                                                                        
        actual_hidden = sigmoid(np.dot(X[i], w_hidden))                                                                                                                 
                                                                                                                                                                        
        actual_output = np.dot(actual_hidden, w_output)                                                                                                                 
                                                                                                                                                                        
        print(f'Input: {X[i]} Predicted Output: {actual_output}')
