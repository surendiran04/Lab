import requests                                                                                                                                                        
                                                                                                                                                                       
url = "https://raw.githubusercontent.com/surendiran04/Lab/main/sample.txt"                                                                                                                                                                                                                                                                
res=requests.get(url)                                                                                                                                                  
                                                                                                                                                                       
with open("sample.txt","wb") as file:                                                                                                                                  
    file.write(res.content)
