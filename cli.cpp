#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 8080

using namespace std;

int main() {
    int client_fd;
    struct sockaddr_in server_address;
    char buffer[1024] = {0};

    // Creating socket
    if ((client_fd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation error");
        return -1;
    }

    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);

    // Convert IPv4 address from text to binary form
    if (inet_pton(AF_INET, "127.0.0.1", &server_address.sin_addr) <= 0) {
        cout << "Invalid address/Address not supported" << endl;
        return -1;
    }

    // Connect to server
    if (connect(client_fd, (struct sockaddr *)&server_address, sizeof(server_address)) < 0) {
        cout << "Connection Failed" << endl;
        return -1;
    }

    while (true) {
        // Receive data from server
        int valread = read(client_fd, buffer, 1024);
        if (valread > 0) {
            cout << "Received: " << buffer << endl;
        }

        // Simulate random packet loss
        if (rand() % 10 == 0) {
            // Send LOSS notification to server
            send(client_fd, "LOSS", strlen("LOSS"), 0);
            cout << "Simulating packet loss" << endl;
        } else {
            // Send ACK to server
            send(client_fd, "ACK", strlen("ACK"), 0);
            cout << "Sending ACK" << endl;
        }
        memset(buffer, 0, 1024);
        usleep(500000);  // Delay before next iteration
    }

    close(client_fd);
    return 0;
}
