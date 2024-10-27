import numpy as np                                                                                                                                                      
                                                                                                                                                                        
import matplotlib.pyplot as plt                                                                                                                                         
                                                                                                                                                                        
from sklearn import datasets                                                                                                                                            
                                                                                                                                                                        
from sklearn import svm                                                                                                                                                 
                                                                                                                                                                        
from sklearn.model_selection import train_test_split                                                                                                                    
                                                                                                                                                                        
from sklearn.metrics import classification_report, confusion_matrix                                                                                                     
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Load the iris dataset                                                                                                                                                 
                                                                                                                                                                        
iris = datasets.load_iris()                                                                                                                                             
                                                                                                                                                                        
X = iris.data  # Features                                                                                                                                               
                                                                                                                                                                        
y = iris.target  # Labels                                                                                                                                               
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Split the dataset into training and testing sets                                                                                                                      
                                                                                                                                                                        
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)                                                                               
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Create an SVM classifier                                                                                                                                              
                                                                                                                                                                        
clf = svm.SVC(kernel='linear')  # You can also try 'rbf', 'poly', etc.                                                                                                  
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Train the classifier                                                                                                                                                  
                                                                                                                                                                        
clf.fit(X_train, y_train)                                                                                                                                               
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Make predictions on the test set                                                                                                                                      
                                                                                                                                                                        
y_pred = clf.predict(X_test)                                                                                                                                            
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Print the classification report and confusion matrix                                                                                                                  
                                                                                                                                                                        
print("Classification Report:")                                                                                                                                         
                                                                                                                                                                        
print(classification_report(y_test, y_pred))                                                                                                                            
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
print("Confusion Matrix:")                                                                                                                                              
                                                                                                                                                                        
print(confusion_matrix(y_test, y_pred))                                                                                                                                 
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Visualizing the decision boundary (only for the first two features)                                                                                                   
                                                                                                                                                                        
def plot_decision_boundary(X, y, model):                                                                                                                                
                                                                                                                                                                        
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1                                                                                                                 
                                                                                                                                                                        
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1                                                                                                                 
                                                                                                                                                                        
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),                                                                                                                 
                                                                                                                                                                        
                         np.arange(y_min, y_max, 0.01))                                                                                                                 
                                                                                                                                                                        

                                                                                                                                                                        
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])                                                                                                                    
                                                                                                                                                                        
    Z = Z.reshape(xx.shape)                                                                                                                                             
                                                                                                                                                                        

                                                                                                                                                                        
    plt.contourf(xx, yy, Z, alpha=0.8)                                                                                                                                  
                                                                                                                                                                        
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', s=50)                                                                                                
                                                                                                                                                                        
    plt.xlabel('Feature 1')                                                                                                                                             
                                                                                                                                                                        
    plt.ylabel('Feature 2')                                                                                                                                             
                                                                                                                                                                        
    plt.title('SVM Decision Boundary')                                                                                                                                  
                                                                                                                                                                        
    plt.show()                                                                                                                                                          
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# For visualization, we need to reduce to 2 dimensions (using the first two features)                                                                                   
                                                                                                                                                                        
X_train_2d = X_train[:, :2]                                                                                                                                             
                                                                                                                                                                        
clf_2d = svm.SVC(kernel='linear')                                                                                                                                       
                                                                                                                                                                        
clf_2d.fit(X_train_2d, y_train)                                                                                                                                         
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
# Plot decision boundary                                                                                                                                                
                                                                                                                                                                        
plot_decision_boundary(X_train_2d, y_train, clf_2d)
