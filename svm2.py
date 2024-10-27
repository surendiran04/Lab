import numpy as np                                                                                                                                                      
                                                                                                                                                                        
import matplotlib.pyplot as plt                                                                                                                                         
                                                                                                                                                                        
from sklearn import datasets                                                                                                                                            
                                                                                                                                                                        
from sklearn import svm                                                                                                                                                 
                                                                                                                                                                        
from sklearn.model_selection import train_test_split                                                                                                                    
                                                                                                                                                                        
from sklearn.metrics import classification_report, confusion_matrix                                                                                                     
                                                                                                                                                                        

                                                                                                                                                                        
def load_iris_dataset():                                                                                                                                                
                                                                                                                                                                        
    """Load the Iris dataset from sklearn."""                                                                                                                           
                                                                                                                                                                        
    iris = datasets.load_iris()                                                                                                                                         
                                                                                                                                                                        
    return iris.data, iris.target                                                                                                                                       
                                                                                                                                                                        
                                                                                                                                                                        
def split_dataset(X, y, test_size=0.2, random_state=42):                                                                                                                
                                                                                                                                                                        
    """Split the dataset into training and testing sets."""                                                                                                             
                                                                                                                                                                        
    return train_test_split(X, y, test_size=test_size, random_state=random_state)                                                                                       
                                                                                                                                                                        

                                                                                                                                                                        
def create_svm_classifier(kernel='linear'):                                                                                                                             
                                                                                                                                                                        
    """Create an SVM classifier with the specified kernel."""                                                                                                           
                                                                                                                                                                        
    return svm.SVC(kernel=kernel)                                                                                                                                       
                                                                                                                                                                        

                                                                                                                                                                        
def train_classifier(clf, X_train, y_train):                                                                                                                            
                                                                                                                                                                        
    """Train the SVM classifier on the training data."""                                                                                                                
                                                                                                                                                                        
    clf.fit(X_train, y_train)                                                                                                                                           
                                                                                                                                                                        
                                                                                                                                                                        
def make_predictions(clf, X_test):                                                                                                                                      
                                                                                                                                                                        
    """Make predictions using the trained classifier on the test data."""                                                                                               
                                                                                                                                                                        
    return clf.predict(X_test)                                                                                                                                          
                                                                                                                                                                        

                                                                                                                                                                        
def print_classification_report(y_test, y_pred):                                                                                                                        
                                                                                                                                                                        
    """Print the classification report to evaluate the model's performance."""                                                                                          
                                                                                                                                                                        
    print("Classification Report:")                                                                                                                                     
                                                                                                                                                                        
    print(classification_report(y_test, y_pred))                                                                                                                        
                                                                                                                                                                        

                                                                                                                                                                        
def print_confusion_matrix(y_test, y_pred):                                                                                                                             
                                                                                                                                                                        
    """Print the confusion matrix to evaluate the model's performance."""                                                                                               
                                                                                                                                                                        
    print("Confusion Matrix:")                                                                                                                                          
                                                                                                                                                                        
    print(confusion_matrix(y_test, y_pred))                                                                                                                             
                                                                                                                                                                        

                                                                                                                                                                        
def plot_decision_boundary(X, y, model):                                                                                                                                
                                                                                                                                                                        
    """Visualize the decision boundary of the SVM model."""                                                                                                             
                                                                                                                                                                        
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
                                                                                                                                                                        

                                                                                                                                                                        
def main():                                                                                                                                                             
                                                                                                                                                                        
    """Main function to execute the SVM classification workflow."""                                                                                                     
                                                                                                                                                                        
    # Load the Iris dataset                                                                                                                                             
                                                                                                                                                                        
    X, y = load_iris_dataset()                                                                                                                                          
                                                                                                                                                                        

                                                                                                                                                                        
    # Split the dataset into training and testing sets                                                                                                                  
                                                                                                                                                                        
    X_train, X_test, y_train, y_test = split_dataset(X, y)                                                                                                              
                                                                                                                                                                        

                                                                                                                                                                        
    # Create and train the SVM classifier                                                                                                                               
                                                                                                                                                                        
    clf = create_svm_classifier()                                                                                                                                       
                                                                                                                                                                        
    train_classifier(clf, X_train, y_train)                                                                                                                             
                                                                                                                                                                        

                                                                                                                                                                        
    # Make predictions on the test set                                                                                                                                  
                                                                                                                                                                        
    y_pred = make_predictions(clf, X_test)                                                                                                                              
                                                                                                                                                                        

                                                                                                                                                                        
    # Print classification report and confusion matrix                                                                                                                  
                                                                                                                                                                        
    print_classification_report(y_test, y_pred)                                                                                                                         
                                                                                                                                                                        
    print_confusion_matrix(y_test, y_pred)                                                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
    # Visualizing the decision boundary (only for the first two features)                                                                                               
                                                                                                                                                                        
    X_train_2d = X_train[:, :2]  # Reduce to 2D for visualization                                                                                                       
                                                                                                                                                                        
    clf_2d = create_svm_classifier()  # Create a new classifier for 2D                                                                                                  
                                                                                                                                                                        
    train_classifier(clf_2d, X_train_2d, y_train)  # Train with 2D data                                                                                                 
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
    # Plot decision boundary                                                                                                                                            
                                                                                                                                                                        
    plot_decision_boundary(X_train_2d, y_train, clf_2d)                                                                                                                 
                                                                                                                                                                        

                                                                                                                                                                        
if name == "main":                                                                                                                                              
                                                                                                                                                                        
    main()
