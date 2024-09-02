def activation(out, threshold):                                                                                                                                        
    if out >= threshold:                                                                                                                                               
        return 1                                                                                                                                                       
    else:                                                                                                                                                              
        return 0                                                                                                                                                       
                                                                                                                                                                       
def perceptron(and_input):                                                                                                                                             
    a = [0,0,1,1]                                                                                                                                                      
    b = [0,1,0,1]                                                                                                                                                      
    y = [0,0,0,1]                                                                                                                                                      
    w = [0.1,0.8]                                                                                                                                                      
    threshold = 1                                                                                                                                                      
    learning_rate = 0.5                                                                                                                                                
    i = 0                                                                                                                                                              
    while i<4:                                                                                                                                                         
        sum = a[i]*w[0] + b[i]*w[1]                                                                                                                                    
        o = activation(sum, threshold)                                                                                                                                 
        print("Input : " + str(a[i]) + "," + str(b[i]))                                                                                                                
        print("weight : " + str(w[0]) + "," + str(w[1]))                                                                                                               
        print("summation :" + str(sum) + "threshold" + str(threshold) )                                                                                                
        print("Actual output : " + str(y[i]) + "predicated output : " + str(o))                                                                                        
        if(o != y[i]):                                                                                                                                                 
            print("----\nUpdating weights")                                                                                                                            
            w[0] = w[0] + learning_rate * (y[i] - o) * a[i]                                                                                                            
            w[1] = w[1] + learning_rate * (y[i] - o) * b[i]                                                                                                            
            print("Updated weights : " + str(w[0]) + "," + str(w[1]))                                                                                                  
            print("\nweights updated training again:")                                                                                                                 
            print("##########################")                                                                                                                        
            i = -1                                                                                                                                                     
        i = i + 1                                                                                                                                                      
        print("-------------------------")                                                                                                                             
    sum = and_input[0]*w[0] + and_input[1]*w[1]                                                                                                                        
    return activation(sum, threshold)                                                                                                                                  
                                                                                                                                                                       
and_input = [1,1]                                                                                                                                                      
print("And gate output for " + str(and_input) + ":" + str(perceptron(and_input)))                                                                                      
                                                                                                                                                                       
