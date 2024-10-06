import base64                                                                                                                                                                                          
                                                                                                                                                                                                       
import json                                                                                                                                                                                            
                                                                                                                                                                                                       
import requests                                                                                                                                                                                        
                                                                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       
# Get file name from user                                                                                                                                                                              
                                                                                                                                                                                                       
fname = input("Enter the file name to upload: ")                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       
# Read the file content and encode it in base64                                                                                                                                                        
                                                                                                                                                                                                       
with open(fname, "rb") as file:                                                                                                                                                                        
                                                                                                                                                                                                       
    file_content = file.read()                                                                                                                                                                         
                                                                                                                                                                                                       
    encoded_content = base64.b64encode(file_content).decode("utf-8")                                                                                                                                   
                                                                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       
# Create the payload for GitHub API                                                                                                                                                                    
                                                                                                                                                                                                       
payload = {                                                                                                                                                                                            
                                                                                                                                                                                                       
    "message": f"uploaded {fname}",                                                                                                                                                                    
                                                                                                                                                                                                       
    "content": encoded_content                                                                                                                                                                         
                                                                                                                                                                                                       
}                                                                                                                                                                                                      
                                                                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       
# Save payload to a JSON file (optional)                                                                                                                                                               
                                                                                                                                                                                                       
with open("payload.json", "w") as json_file:                                                                                                                                                           
                                                                                                                                                                                                       
    json.dump(payload, json_file)                                                                                                                                                                      
                                                                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       
# GitHub API request details                                                                                                                                                                           
                                                                                                                                                                                                       
api_url = f"https://api.github.com/repos/Irfan-Fareeth/demolab/contents/{fname}"                                                                                                                       
                                                                                                                                                                                                       
headers = {                                                                                                                                                                                            
                                                                                                                                                                                                       
    "Authorization": "token --token",                                                                                                                                 
                                                                                                                                                                                                       
    "Content-Type": "application/json"                                                                                                                                                                 
                                                                                                                                                                                                       
}                                                                                                                                                                                                      
                                                                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       
# Make the PUT request to upload the file                                                                                                                                                              
                                                                                                                                                                                                       
response = requests.put(api_url, headers=headers, data=json.dumps(payload))                                                                                                                            
                                                                                                                                                                                                       
                                                                                                                                                                                                       
                                                                                                                                                                                                       
# Check the response status                                                                                                                                                                            
                                                                                                                                                                                                       
if response.status_code == 201:                                                                                                                                                                        
                                                                                                                                                                                                       
    print(f"File {fname} uploaded successfully.")                                                                                                                                                      
                                                                                                                                                                                                       
else:                                                                                                                                                                                                  
                                                                                                                                                                                                       
    print(f"Failed to upload {fname}. Response: {response.status_code} - {response.text}")
