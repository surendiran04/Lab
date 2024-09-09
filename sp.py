import numpy as np                                                                                                                                                      



class SingleLayerPerceptron:                                                                                                                                            

    def _init_(self, input_size, learning_rate=0.1, epochs=10, initial_weights=None):                                                                                 

        if initial_weights is None:                                                                                                                                     

            # Initialize weights to zero if no initial weights are provided                                                                                             

            self.weights = np.zeros(input_size + 1)                                                                                                                     

        else:                                                                                                                                                           

            # Use the provided initial weights                                                                                                                          

            self.weights = np.array(initial_weights)                                                                                                                    




        self.learning_rate = learning_rate                                                                                                                              




        self.epochs = epochs                                                                                                                                            








    def activation(self, x):                                                                                                                                            

        return 1 if x >= 0 else 0                                                                                                                                       






    def predict(self, inputs):                                                                                                                                          

        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]                                                                                                  

        return self.activation(summation)                                                                                                                               





    def train(self, training_inputs, labels):                                                                                                                           

        for epoch in range(self.epochs):                                                                                                                                

            print(f"\nEpoch {epoch + 1}/{self.epochs}")                                                                                                                 

            for inputs, label in zip(training_inputs, labels):                                                                                                          

                prediction = self.predict(inputs)                                                                                                                       




                error = label - prediction                                                                                                                              




                self.weights[1:] += self.learning_rate * error * inputs                                                                                                 

                self.weights[0] += self.learning_rate * error                                                                                                           

                print(f"  Inputs: {inputs}, Prediction: {prediction}, Error: {error}")                                                                                  

                print(f"  Updated Weights: {self.weights}")                                                                                                             



# Training data for different logic gates                                                                                                                               

logic_gates = {                                                                                                                                                         




    "AND": {                                                                                                                                                            

        "inputs": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),                                                                                                           

        "labels": np.array([0, 0, 0, 1])                                                                                                                                

     },                                                                                                                                                                 




    "OR": {                                                                                                                                                             

        "inputs": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),                                                                                                           

        "labels": np.array([0, 1, 1, 1])                                                                                                                                

    },                                                                                                                                                                  



    "NOR": {                                                                                                                                                            

        "inputs": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),                                                                                                           

        "labels": np.array([1, 0, 0, 0])                                                                                                                                

    },                                                                                                                                                                  




    "XOR": {                                                                                                                                                            

        "inputs": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),                                                                                                           

        "labels": np.array([0, 1, 1, 0])                                                                                                                                

    }                                                                                                                                                                   




}                                                                                                                                                                       





# Initialize the perceptron                                                                                                                                             

input_size = 2                                                                                                                                                          

learning_rate = 0.1                                                                                                                                                     

epochs = 10                                                                                                                                                             

initial_weights = [0.5, -0.2, -0.3]  # Example initial weights                                                                                                          



# Train and test perceptrons for each logic gate                                                                                                                        

for gate, data in logic_gates.items():                                                                                                                                  

    print(f"\nTraining Perceptron for {gate} gate")                                                                                                                     

    perceptron = SingleLayerPerceptron(input_size, learning_rate, epochs, initial_weights)                                                                              




    perceptron.train(data['inputs'], data['labels'])                                                                                                                    

    print(f"\nTesting {gate} gate after training")                                                                                                                      

    for inputs, label in zip(data['inputs'], data['labels']):                                                                                                           
        prediction=perceptron.predict(inputs)                                                                                                                           
        print(f" Input: {inputs},Expected Output: {label}, Predicted Output: {prediction}")                                                                             
        print("="*50)
