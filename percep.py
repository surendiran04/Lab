inputs = [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]                                                                                                          
outputs = [1, 1, 1, 0, 1, 0, 0, 0]                                                                                                                                                         
weights = [0.1, 0.2, 0.3]                                                                                                                                                                  
pweights = weights.copy()                                                                                                                                                                  
bias = 1                                                                                                                                                                                   
bw = 0.1                                                                                                                                                                                   
lrl = [0.4]                                                                                                                                                                                
epochs = 5                                                                                                                                                                                 
                                                                                                                                                                                           
def function(lr):                                                                                                                                                                          
    def predict(x):                                                                                                                                                                        
        res = 0                                                                                                                                                                            
        for i in range(len(x)):                                                                                                                                                            
            res += x[i] * weights[i]                                                                                                                                                       
        res += (bias*bw)                                                                                                                                                                   
        if res > 0:                                                                                                                                                                        
            return 1                                                                                                                                                                       
        else:                                                                                                                                                                              
            return 0                                                                                                                                                                       
                                                                                                                                                                                           
    def distribute(error, x):                                                                                                                                                              
        global bw                                                                                                                                                                          
        for i in range(len(weights)):                                                                                                                                                      
            weights[i] = weights[i] + error*lr*x[i]                                                                                                                                        
            pweights[i] = round(weights[i], 2)                                                                                                                                             
        bw = bw + error*lr*bias                                                                                                                                                            

    def predict_new(new):                                                                                                                                                                  
        print("NEW INPUT'S PREDICTION :")                                                                                                                                                  
        p = []                                                                                                                                                                             
        for i in new:                                                                                                                                                                      
            p.append(predict(i))                                                                                                                                                           
        print(p)                                                                                                                                                                           
                                                                                                                                                                                           
    er = 0, 0                                                                                                                                                                              
    print("="*175)                                                                                                                                                                         
    print("INPUT\t\t", "WEIGHTS\t\t", "BIAS\t\t", "LR\t\t", "OUTPUT\t\t", "PREDICT\t", "ERROR")                                                                                            
    print("="*175)                                                                                                                                                                         
    for i in range(epochs):                                                                                                                                                                
        print("-"*10, "EPOCH ",i+1," ", "-"*10)                                                                                                                                            
        for a in range(len(inputs)):                                                                                                                                                       
            yout = predict(inputs[a])                                                                                                                                                      
            y = outputs[a]                                                                                                                                                                 
            error = (y - yout)                                                                                                                                                             
            if error != 0:                                                                                                                                                                 
                er = i+1, a+1                                                                                                                                                              
            print(inputs[a], "\t", pweights, "\t", round(bias, 2), "\t\t", lr, "\t\t", outputs[a], "\t\t", yout, "\t\t", error)                                                            
            distribute(error, inputs[a])                                                                                                                                                   
    print("="*175)                                                                                                                                                                         
    print("CONVEREGED AT EPOCH => ", er[0], " AND ITERATION => ", er[1])                                                                                                                   
for i in lrl:                                                                                                                                                                              
    function(i)
