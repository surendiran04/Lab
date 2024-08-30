import csv                                                                                                                                                                                 
test_set = [["sunny",85,85,"FALSE","no"],                                                                                                                                                  
            ["sunny",80,90,"TRUE","no"],                                                                                                                                                   
            ["overcast",83,86,"FALSE","yes"],                                                                                                                                              
            ["rainy",70,96,"FALSE","yes"],                                                                                                                                                 
            ["rainy", 68, 80,"FALSE","yes"]]                                                                                                                                               
print("-"*100)                                                                                                                                                                             
print("{} -> \n{}".format(1, test_set))                                                                                                                                                    
print("\n{} ->".format(2))                                                                                                                                                                 
def find_s(test_set):                                                                                                                                                                      
    hypothesis = [0] * len(test_set[0])                                                                                                                                                    
    for i in range(len(test_set)):                                                                                                                                                         
        if test_set[i][-1] == "yes":                                                                                                                                                       
            positive = test_set[i]                                                                                                                                                         
            for j in range(len(positive)):                                                                                                                                                 
                if hypothesis[j] == 0:                                                                                                                                                     
                    hypothesis[j] = positive[j]                                                                                                                                            
                elif hypothesis[j] == positive[j]:                                                                                                                                         
                    continue                                                                                                                                                               
                else:                                                                                                                                                                      
                    hypothesis[j] = "?"                                                                                                                                                    
        print(i+1, " Hypothesis : ", hypothesis[:-1])                                                                                                                                      
    print("\n{} ->".format(3))                                                                                                                                                             
    print("General Hypothesis : ", hypothesis[:-1])                                                                                                                                        
                                                                                                                                                                                           
find_s(test_set)                                                                                                                                                                           
def instances(test_set):                                                                                                                                                                   
    print("\n{} ->".format(4))                                                                                                                                                             
    s = []                                                                                                                                                                                 
    for i in range(len(test_set)-1):                                                                                                                                                       
        a = set()                                                                                                                                                                          
        for j in range(len(test_set[0])):                                                                                                                                                  
            a.add(test_set[j][i])                                                                                                                                                          
        s.append(len(a))                                                                                                                                                                   
    i1 = 1                                                                                                                                                                                 
    for i in s:                                                                                                                                                                            
        i1 = i1*i                                                                                                                                                                          
    i2 = 1                                                                                                                                                                                 
    for i in s:                                                                                                                                                                            
        i2 = i2*(i+2)                                                                                                                                                                      
    i3 = 1                                                                                                                                                                                 
    for i in s:                                                                                                                                                                            
        i3 = i3*(i+1)                                                                                                                                                                      
    i3 += 1                                                                                                                                                                                
    print("Total Instances : ", i1)                                                                                                                                                        
    print("Syntatically different : ", i2)                                                                                                                                                 
    print("Semanticallly different : ", i3)                                                                                                                                                
    print("-"*100)                                                                                                                                                                         
instances(test_set)                                                                                                                                                                        
                                                                                                                                                                                           
def discritize(best_set):                                                                                                                                                                  
    it = min(x[1] for x in best_set)                                                                                                                                                       
    at = max(x[1] for x in best_set)                                                                                                                                                       
    ih = min(x[2] for x in best_set)                                                                                                                                                       
    ah = max(x[2] for x in best_set)                                                                                                                                                       
    ti = (at-it)/5                                                                                                                                                                         
    hi = (ah-ih)/5                                                                                                                                                                         
    for i in range(len(best_set)):                                                                                                                                                         
        t = best_set[i][1]                                                                                                                                                                 
        if t >= it and t <= (it + 1*ti):                                                                                                                                                   
            best_set[i][1] = str(it) + "-" + str(it + 1*ti)                                                                                                                                
        elif t >= (it + 1*ti) and t <= (it + 2*ti):                                                                                                                                        
            best_set[i][1] = str(it + 1*ti) + "-" + str(it + 2*ti)                                                                                                                         
        elif t >= (it + 2*ti) and t <= (it + 3*ti):                                                                                                                                        
            best_set[i][1] = str(it + 2*ti) + "-" + str(it + 3*ti)                                                                                                                         
        elif t >= (it + 3*ti) and t <= (it + 4*ti):                                                                                                                                        
            best_set[i][1] = str(it + 3*ti) + "-" + str(it + 4*ti)                                                                                                                         
        elif t >= (it + 4*ti) and t <= (it + 5*ti):                                                                                                                                        
            best_set[i][1] = str(it + 4*ti) + "-" + str(it + 5*ti)                                                                                                                         
    for i in range(len(best_set)):                                                                                                                                                         
        h = best_set[i][2]                                                                                                                                                                 
        if h >= ih and h <= (ih + 1*hi):                                                                                                                                                   
            best_set[i][2] = str(ih) + "-" + str(ih + 1*hi)                                                                                                                                
        elif h >= (ih + 1*hi) and h <= (ih + 2*hi):                                                                                                                                        
            best_set[i][2] = str(ih + 1*hi) + "-" + str(ih + 2*hi)                                                                                                                         
        elif h >= (ih + 2*hi) and h <= (ih + 3*hi):                                                                                                                                        
            best_set[i][2] = str(ih + 2*hi) + "-" + str(ih + 3*hi)                                                                                                                         
        elif h >= (ih + 3*hi) and h <= (ih + 4*hi):                                                                                                                                        
            best_set[i][2] = str(ih + 3*hi) + "-" + str(ih + 4*hi)                                                                                                                         
        elif h >= (ih + 4*hi) and h <= (ih + 5*hi):                                                                                                                                        
            best_set[i][2] = str(ih + 4*hi) + "-" + str(ih + 5*hi)                                                                                                                         
    print("{} -> \n{}".format(1, best_set))                                                                                                                                                
    print("\n{} ->".format(2))                                                                                                                                                             
    print(best_set[2])                                                                                                                                                                     
    print(best_set[3])                                                                                                                                                                     
    find_s(best_set)                                                                                                                                                                       

    instances(best_set)                                                                                                                                                                    
discritize(test_set)
