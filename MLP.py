import numpy as np                                                                                                                                                     
import matplotlib.pyplot as plt                                                                                                                                        
from IPython.display import clear_output                                                                                                                               

%matplotlib inline                                                                                                                                                     

from sklearn.model_selection import train_test_split                                                                                                                   
                                                                                                                                                                      
from sklearn.datasets import make_circles                                                                                                                              

N = 100                                                                                                                                                                
d = 2                                                                                                                                                                  
X, t = make_circles(n_samples = N, noise = 0.03, random_state = 42)                                                                                                    
X_train, X_test, t_train, t_test = train_test_split(X, t, test_size=0.2, random_state=42)                                                                              
rng = np.random.default_rng()                                                                                                                                          

def logistic(x):                                                                                                                                       
    return 1.0/(1.0 + np.exp(-x))                                                                                                                                      
                                                                                                                                                                       
def logistic_derivative(x):                                                                                                                                            
    return logistic(x) * (1 - logistic(x))                                                                                                                             

class MLP:                                                                                                                                                                                                                                                                                                                             
    def __init__(self, d, K, activation_function, activation_function_derivative, max_val, eta):                                                                                                                                                                                                                                              
        self.d = d                                                                                                                                                     

        self.K = K                                                                                                                                                     

        self.activation_function = activation_function                                                                                                                 
        self.activation_function_derivative = activation_function_derivative                                                                                           
        self.eta = eta                                                                                                                                                 

                                                                                                                                                                       
        self.W1  = rng.uniform(-max_val, max_val, (K, d))                                                                                                              

        self.b1  = rng.uniform(-max_val, max_val, (K, 1))                                                                                                              

                                                                                                                                                                       
        self.W2 = rng.uniform(-max_val, max_val, (1, K))                                                                                                               

        self.b2 = rng.uniform(-max_val, max_val, (1, 1))                                                                                                               

                                                                                                                                                                       
    def feedforward(self, x):                                                                                                                                          

                                                                                                                                                                       
        # Make sure x has 2 rows                                                                                                                                       

        x = np.array(x).reshape((self.d, -1))                                                                                                                          



        # Hidden layer                                                                                                                                                 

        self.h = self.activation_function(np.dot(self.W1, x) + self.b1)                                                                                                


        # Output layer                                                                                                                                                 

        self.y = logistic(np.dot(self.W2, self.h) + self.b2)                                                                                                           

                                                                                                                                                                       
                                                                                                                                                                       
    def train(self, X_train, t_train, nb_epochs, visualize=True):                                                                                                      

        errors = []                                                                                                                                                    

                                                                                                                                                                       
        for epoch in range(nb_epochs):                                                                                                                                 

                                                                                                                                                                       
            nb_errors = 0                                                                                                                                              



            # Epoch                                                                                                                                                    

            for i in range(X_train.shape[0]):                                                                                                                          


                # Feedforward pass: sets self.h and self.y                                                                                                             

                self.feedforward(X_train[i, :])                                                                                                                        

                                                                                                                                                                       
                # Backpropagation                                                                                                                                      

                self.backprop(X_train[i, :], t_train[i])                                                                                                               

                                                                                                                                                                       
                # Predict the class:                                                                                                                                   

                if self.y[0, 0] > 0.5:                                                                                                                                 

                    c = 1                                                                                                                                              

                else:                                                                                                                                                  

                    c = 0                                                                                                                                              



                # Count the number of misclassifications                                                                                                               

                if t_train[i] != c:                                                                                                                                    

                    nb_errors += 1                                                                                                                                     

                                                                                                                                                                       
            # Compute the error rate                                                                                                                                   

            errors.append(nb_errors/X_train.shape[0])                                                                                                                  

                                                                                                                                                                       
            # Plot the decision function every 10 epochs                                                                                                               

            if epoch % 10 == 0 and visualize:                                                                                                                          

                self.plot_classification()                                                                                                                             


f nb_errors == 0:                                                                                                                                                      

                if visualize:                                                                                                                                          

                    self.plot_classification()                                                                                                                         

                break                                                                                                                                                  

        # errors.append(0)                                                                                                                                             
        return errors, epoch+1                                                                                                                                         



    def backprop(self, x, t):                                                                                                                                          

                                                                                                                                                                       
        # Make sure x has 2 rows                                                                                                                                       

        x = np.array(x).reshape((self.d, -1))                                                                                                                          



        # TODO: implement backpropagation                                                                                                                              
        delta2 = -(self.y - t)                                                                                                                                         
        #Hidden layer error                                                                                                                                            
        delta1 = self.activation_function_derivative(np.dot(self.W1, x) + self.b1) * np.dot(self.W2.T, delta2)                                                         
                                                                                                                                                                       
        # Update weights and biases                                                                                                                                    
        self.W2 += self.eta * np.dot(delta2, self.h.T)                                                                                                                 
        self.b2 += self.eta * delta2                                                                                                                                   
                                                                                                                                                                       
        self.W1 += self.eta * np.dot(delta1, x.T)                                                                                                                      
        self.b1 += self.eta * delta1                                                                                                                                   
                                                                                                                                                                       
    def test(self, X_test, t_test):                                                                                                                                    

                                                                                                                                                                       
        nb_errors = 0                                                                                                                                                  

        for i in range(X_test.shape[0]):                                                                                                                               



            # Feedforward pass                                                                                                                                         

            self.feedforward(X_test[i, :])                                                                                                                             



            # Predict the class:                                                                                                                                       

            if self.y[0, 0] > 0.5:                                                                                                                                     

                c = 1                                                                                                                                                  

            else:                                                                                                                                                      
                c = 0                                                                                                                                                  



            # Count the number of misclassifications                                                                                                                   

            if t_test[i] != c:                                                                                                                                         

                nb_errors += 1                                                                                                                                         



        return nb_errors/X_test.shape[0]                                                                                                                               

                                                                                                                                                                       
    def plot_classification(self):                                                                                                                                     



        # Allow redrawing                                                                                                                                              

        clear_output(wait=True)                                                                                                                                        



        x_min, x_max = X_train[:, 0].min(), X_train[:, 0].max()                                                                                                        

        y_min, y_max = X_train[:, 1].min(), X_train[:, 1].max()                                                                                                        

        xx, yy = np.meshgrid(np.arange(x_min, x_max, .02), np.arange(y_min, y_max, .02))                                                                               



        x1 = xx.ravel()                                                                                                                                                

        x2 = yy.ravel()                                                                                                                                                

        x = np.array([[x1[i], x2[i]] for i in range(x1.shape[0])])                                                                                                     



        self.feedforward(x.T)                                                                                                                                          

        Z = self.y.copy()                                                                                                                                              

        Z[Z>0.5] = 1                                                                                                                                                   

        Z[Z<=0.5] = 0                                                                                                                                                  

        from matplotlib.colors import ListedColormap    

        cm_bright = ListedColormap(['#FF0000', '#0000FF'])                                                                                                             
        fig = plt.figure(figsize=(10, 6))                                                                                                                              

        plt.contourf(xx, yy, Z.reshape(xx.shape), cmap=cm_bright, alpha=.4)                                                                                            

        plt.scatter(X_train[:, 0], X_train[:, 1], c=t_train, cmap=cm_bright, edgecolors='k')                                                                           

        plt.scatter(X_test[:, 0], X_test[:, 1], c=t_test, cmap=cm_bright, alpha=0.4, edgecolors='k')                                                                   

        plt.xlim(xx.min(), xx.max())                                                                                                                                   

        plt.ylim(yy.min(), yy.max())                                                                                                                                   

        plt.show()                                                                                                                                                     
                                                                                                                                                                       
mlp = MLP(2, 15, logistic,logistic_derivative, 1, 0.05)                                                                                                                
errors, epochs = mlp.train(X_train, t_train, 1000)                                                                                                                     
err = mlp.test(X_test, t_test)                                                                                                                                         
plt.plot(range(epochs), errors, color = 'red', linewidth = 3, label = 'regression line')                                                                               
print("Train Error = ", errors[-1], "Test error ", err, "Converged at = ", epochs, "Accuracy = ", errors[-1]/err) 
