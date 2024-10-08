[s2022103530@sflinuxonline 03.10.2024-20:04:53 - /week7]$ cat nagles_client.c                                                         
#include <stdlib.h>                                                                                                                   
#include <fcntl.h>                                                                                                                    
#include <stdio.h>                                                                                                                    
#include <sys/types.h>                                                                                                                
#include <sys/socket.h>                                                                                                               
#include <netinet/in.h>                                                                                                               
#include <string.h>                                                                                                                   
#include <arpa/inet.h>                                                                                                                
#include <unistd.h>                                                                                                                   
#define size 1024                                                                                                                     
                                                                                                                                      
int main()                                                                                                                            
{                                                                                                                                     
        int sockfd,connfd=0,n,x=0,i,y=1,flag=0,first=0;                                                                               
        double rtt,ud,time=0,temp;                                                                                                    
        struct sockaddr_in serv_addr;                                                                                                 
        char buffer[100];                                                                                                             
        char packets[size],ack[100];                                                                                                  
                                                                                                                                      
        serv_addr.sin_family = AF_INET;                                                                                               
        serv_addr.sin_port = htons(9999);                                                                                             
        serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");                                                                           
                                                                                                                                      
        sockfd=socket(AF_INET, SOCK_STREAM, 0);                                                                                       
                                                                                                                                      
        if(sockfd<0)                                                                                                                  
        {                                                                                                                             
                printf("Socket creation failed\n");                                                                                   
                return 1;                                                                                                             
        }                                                                                                                             
                                                                                                                                      
        connfd = connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));                                                    
                                                                                                                                      
        if(connfd<0)                                                                                                                  
        {                                                                                                                             
                printf("server accept failed\n");                                                                                     
                return 1;                                                                                                             
        }                                                                                                                             
        else                                                                                                                          
                printf("connection established\n");                                                                                   
                                                                                                                                      
        printf("enter RTT value: ");                                                                                                  
        scanf("%lf",&rtt);                                                                                                            
        printf("enter uniform delay after which each packet is sent: ");                                                              
        scanf("%lf",&ud);                                                                                                             
                                                                                                                                      
        printf("enter the number of packets to be sent: ");                                                                           
        scanf("%d",&n);                                                                                                               
                                                                                                                                      
        printf("enter the contents of data: ");                                                                                       
        scanf("%s",packets);                                                                                                          
                                                                                                                                      
        temp=(int)(rtt/ud);                                                                                                           
                                                                                                                                      
        while(flag==0){                                                                                                               
                buffer[0]='\0';                                                                                                       
                int k=-1;                                                                                                             
                                                                                                                                      
                for(i=1;i<=y;i++){                                                                                                    
                        if((i==1)&&(packets[x]=='\0')){                                                                               
                                flag=1;                                                                                               
                                goto two;                                                                                             
                        }                                                                                                             
                        else if((i!=1)&&(packets[x]=='\0')){                                                                          
                                flag=1;                                                                                               
                                goto one;                                                                                             
                        }                                                                                                             
                        else{                                                                                                         
                                if(x==0)                                                                                              
                                        first=1;                                                                                      
                                buffer[++k]=packets[x++];                                                                             
                        }                                                                                                             
                }                                                                                                                     
                                                                                                                                      
one:                                                                                                                                  
                buffer[++k]='\0';                                                                                                     
                printf("\nsending packets: %s",buffer);                                                                               
                                                                                                                                      
                send(sockfd,buffer,strlen(buffer)+1,0);                                                                               
                recv(sockfd,ack,sizeof(ack),0);                                                                                       
                                                                                                                                      
                printf("\nreceived acknowledgement: %s",ack);                                                                         
                                                                                                                                      
                time+=rtt;                                                                                                            
                                                                                                                                      
                if(first==1){                                                                                                         
                        first=0;                                                                                                      
                        y=temp-1;                                                                                                     
                }                                                                                                                     
                else                                                                                                                  
                        y=temp;                                                                                                       
        }                                                                                                                             
                                                                                                                                      
two:                                                                                                                                  
        send(sockfd,"exit",5,0);                                                                                                      
        printf("\n\ntotal time taken for transmission: %lf\n",time);                                                                  
                                                                                                                                      
        close(sockfd);                                                                                                                
        return 0;                                                                                                                     
}                                                                                                                                     
[s2022103530@sflinuxonline 03.10.2024-20:05:04 - /week7]$ cat nagles_server.c                                                         
#include <stdio.h>                                                                                                                    
#include <fcntl.h>                                                                                                                    
#include <arpa/inet.h>                                                                                                                
#include <sys/types.h>                                                                                                                
#include <sys/socket.h>                                                                                                               
#include <netinet/in.h>                                                                                                               
#include <string.h>                                                                                                                   
#include <unistd.h>                                                                                                                   
#include <stdlib.h>                                                                                                                   
#define buff_size 1024                                                                                                                
                                                                                                                                      
int main()                                                                                                                            
{                                                                                                                                     
        int sockfd,connfd;                                                                                                            
        struct sockaddr_in serv_addr;                                                                                                 
                                                                                                                                      
        char ack[buff_size]="ACK",buffer[buff_size];                                                                                  
                                                                                                                                      
        serv_addr.sin_family = AF_INET;                                                                                               
        serv_addr.sin_port = htons(9999);                                                                                             
        serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);                                                                                
                                                                                                                                      
        sockfd = socket(AF_INET, SOCK_STREAM, 0);                                                                                     
                                                                                                                                      
        if(sockfd < 0){                                                                                                               
                printf("Socket creation failed!\n");                                                                                  
                return 1;                                                                                                             
        }                                                                                                                             
                                                                                                                                      
        if(bind(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr))<0){                                                          
                printf("Binding failed!!\n");                                                                                         
                return 1;                                                                                                             
        }                                                                                                                             
                                                                                                                                      
        if(listen(sockfd,5)<0){                                                                                                       
                printf("Listening failed\n");                                                                                         
                return 1;                                                                                                             
        }                                                                                                                             
                                                                                                                                      
        connfd = accept(sockfd, (struct sockaddr*)NULL, NULL);                                                                        
                                                                                                                                      
        if(connfd)                                                                                                                    
                printf("Connection established with the client\n");                                                                   
        for(;;){                                                                                                                      
                recv(connfd,buffer,sizeof(buffer),0);                                                                                 
                                                                                                                                      
                if(strncmp(buffer,"exit",strlen("exit"))==0){                                                                         
                        printf("\n\nexiting.....\n");                                                                                 
                        break;                                                                                                        
                }                                                                                                                     
                                                                                                                                      
                printf("\nreceived packets: %s",buffer);                                                                              
                printf("\nsending acknowledgement..\n");                                                                              
                send(connfd,ack,strlen(ack)+1,0);                                                                                     
        }                                                                                                                             
                                                                                                                                      
        close(connfd);                                                                                                                
        close(sockfd);                                                                                                                
                                                                                                                                      
        return 0;                                                                                                                     
}
