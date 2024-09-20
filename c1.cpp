SENDER
// server_stop_and_wait.cpp
#include<iostream>
#include<netinet/in.h>
#include<cstdlib>
#include<unistd.h>
#include<sys/socket.h>
#include<sys/types.h>
#include<cstring>
#include<chrono>
#include<thread>

#define PORT 53567
#define SA struct sockaddr
#define TIMEOUT 5  // Timeout for 5 seconds

using namespace std;

bool send_frame(int connfd, const string& frame, int frame_number){
    cout << "Sending frame " << frame_number << ": " << frame << endl;
    write(connfd, frame.c_str(), frame.length());

    // Wait for acknowledgment
    char ack[1024] = {0};
    fd_set set;
    struct timeval timeout;

    // Initialize the timeout data
    FD_ZERO(&set);
    FD_SET(connfd, &set);
    timeout.tv_sec = TIMEOUT;
    timeout.tv_usec = 0;

    // Wait for acknowledgment within timeout period
    int rv = select(connfd + 1, &set, NULL, NULL, &timeout);

    if(rv == -1){
        cerr << "Error in select()\n";
        return false;
    } else if(rv == 0) {
        // Timeout occurred
        cout << "Timeout! No acknowledgment for frame " << frame_number << ". Resending...\n";
        return false;
    } else {
        // Acknowledgment received
        read(connfd, ack, sizeof(ack));
        cout << "Received ACK for frame " << frame_number << ": " << ack << endl;
        return (strcmp(ack, "ACK") == 0);
    }
}

int main(){
    int sockfd, connfd, len;
    struct sockaddr_in servaddr, cli;

    // Create socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if(sockfd == -1){
        cerr << "Socket creation failed" << endl;
        exit(0);
    } else {
        cout << "Socket created successfully" << endl;
    }

    bzero(&servaddr, sizeof(servaddr));

    // Assign IP and port
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    // Bind the socket
    if(bind(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0){
        cerr << "Bind failed" << endl;
        exit(0);
    } else {
        cout << "Binded successfully" << endl;
    }

    // Listen for clients
    if(listen(sockfd, 5) != 0){
        cerr << "Listen failed" << endl;
    } else {
        cout << "Server listening" << endl;
    }

    len = sizeof(cli);

    // Accept client connection
    connfd = accept(sockfd, (SA*)&cli, (socklen_t*)&len);
    if(connfd < 0){
        cerr << "Server accept failed" << endl;
    } else {
        cout << "Server accepted the client" << endl;
    }

    // Sending data using Stop-and-Wait ARQ protocol
    int frame_number = 1;
    string frames[] = {"Frame1", "Frame2", "Frame3", "Frame4", "Frame5"};
    int total_frames = 5;

    for(int i = 0; i < total_frames;){
        if(send_frame(connfd, frames[i], i + 1)){
            i++;  // Move to the next frame if ACK is received
        } else {
            // Retransmit the current frame
            cout << "Retransmitting frame " << i + 1 << "...\n";
        }
    }

    cout << "All frames sent successfully!" << endl;

    // Close the connection
    close(connfd);
    close(sockfd);
    return 0;
}
