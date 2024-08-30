import numpy as np                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
concepts = np.array([                                                                                                                                                   
                                                                                                                                                                        
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'],                                                                                                              
                                                                                                                                                                        
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'],                                                                                                                
                                                                                                                                                                        
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'],                                                                                                              
                                                                                                                                                                        
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change']                                                                                                               
                                                                                                                                                                        
])                                                                                                                                                                      
                                                                                                                                                                        
target = np.array(['Yes', 'Yes', 'No', 'Yes'])                                                                                                                          
                                                                                                                                                                       
print("Concepts:\n", concepts)                                                                                                                                          
                                                                                                                                                                        
print("Target:\n", target)                                                                                                                                              
                                                                                                                                                                        
def learn(concepts, target):                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    specific_h = concepts[0].copy()                                                                                                                                     
                                                                                                                                                                        
    print("\nInitialization of specific_h and general_h:")                                                                                                              
                                                                                                                                                                        
    print("Specific Hypothesis:", specific_h)                                                                                                                           
                                                                                                                                                                                                                                                                                                                                           
    general_h = [['?' for _ in range(len(specific_h))] for _ in range(len(specific_h))]                                                                                 
                                                                                                                                                                        
    print("General Hypothesis:", general_h)                                                                                                                             
                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                        
    for i, h in enumerate(concepts):                                                                                                                                    
                                                                                                                                                                        
        if target[i].lower() == "yes":                                                                                                                                  
                                                                                                                                                                        
            for x in range(len(specific_h)):                                                                                                                            
                                                                                                                                                                        
                if h[x] != specific_h[x]:                                                                                                                               
                                                                                                                                                                        
                    specific_h[x] = '?'                                                                                                                                 
                                                                                                                                                                        
            print("\nUpdated Specific_h:", specific_h)                                                                                                                  
                                                                                                                                                                                                                                                                                                                                   
                                                                                                                                                                        
        elif target[i].lower() == "no":                                                                                                                                 
                                                                                                                                                                        
            for x in range(len(specific_h)):                                                                                                                            
                                                                                                                                                                        
                if h[x] != specific_h[x]:                                                                                                                               
                                                                                                                                                                        
                    general_h[x][x] = specific_h[x]                                                                                                                     
                                                                                                                                                                        
                else:                                                                                                                                                   
                                                                                                                                                                        
                    general_h[x][x] = '?'                                                                                                                               
                                                                                                                                                                        
            print(f"\nSteps of Candidate Elimination Algorithm ({i + 1}):")                                                                                             
                                                                                                                                                                        
            print("Specific Hypothesis:", specific_h)                                                                                                                   
                                                                                                                                                                        
            print("General Hypothesis:", general_h)                                                                                                                     
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                                                                                                                                     
                                                                                                                                                                        
    general_h = [h for h in general_h if not all(val == '?' for val in h)]                                                                                              
                                                                                                                                                                        
                                                                                                                                                                        
                                                                                                                                                                        
    return specific_h, general_h                                                                                                                                        
                                                                                                                                     
                                                                                                                                                                        
s_final, g_final = learn(concepts, target)                                                                                                                              
                                                                                                                                                                        
print("\nFinal Specific_h:\n", s_final)                                                                                                                                 
                                                                                                                                                                        
print("Final General_h:\n", g_final)
