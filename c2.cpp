RECEIVER
// client_stop_and_wait.cpp
#include<arpa/inet.h>
#include<netdb.h>
#include<iostream>
#include<cstdlib>
#include<unistd.h>
#include<cstring>
#include<random>

#define PORT 53567
#define SA struct sockaddr

using namespace std;

// Simulate loss of acknowledgment randomly
bool simulate_ack_loss() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 10); // Random number between 1 and 10

    int chance = dis(gen);
    if (chance <= 2) {
        // 20% chance of losing the acknowledgment
        return false;
    }
    return true;
}

void func(int sockfd){
    char frame[1024] = {0};

    for(;;){
        bzero(frame, sizeof(frame));

        // Receive frame from server
        read(sockfd, frame, sizeof(frame));

        // Exit condition when all frames are sent
        if(strlen(frame) == 0){
            cout << "All frames received successfully!" << endl;
            break;
        }

        cout << "Received frame: " << frame << endl;

        // Simulate ACK loss randomly
        if (simulate_ack_loss()) {
            cout << "Sending ACK\n";
            write(sockfd, "ACK", sizeof("ACK"));
        } else {
            cout << "ACK lost for frame: " << frame << endl;
        }
    }
}

int main(){
    int sockfd;
    struct sockaddr_in servaddr;

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
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    servaddr.sin_port = htons(PORT);

    // Connect to server
    if(connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0){
        cerr << "Client connection failed" << endl;
        exit(0);
    } else {
        cout << "Client connected to server successfully" << endl;
    }

    // Function to receive data from the server
    func(sockfd);

    // Close the socket
    close(sockfd);
    return 0;
}
