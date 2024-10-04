#include <iostream> //server
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define MAX_CWND 100  // Maximum congestion window size

using namespace std;

void aimd(int &cwnd, bool packet_loss) {
    if (packet_loss) {
        // Multiplicative Decrease
        cwnd = max(1, cwnd / 2);
        cout << "Packet loss detected! Multiplicatively decreasing cwnd to " << cwnd << endl;
    } else {
        // Additive Increase
        cwnd += 1;
        cout << "Increasing cwnd to " << cwnd << endl;
    }
}

int main() {
    int server_fd, client_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    int cwnd = 1;  // Initial congestion window size
    char buffer[1024] = {0};
    const char *data = "Hello from server";

    // Creating socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Bind socket to port
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Listen for incoming connections
    if (listen(server_fd, 3) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    cout << "Server listening on port " << PORT << endl;

    // Accept client connection
    if ((client_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen)) < 0) {
        perror("Accept failed");
        exit(EXIT_FAILURE);
    }

    while (true) {
        // Send data based on congestion window size (cwnd)
        for (int i = 0; i < cwnd && i < MAX_CWND; i++) {
            send(client_socket, data, strlen(data), 0);
            cout << "Sent packet " << i + 1 << " with cwnd = " << cwnd << endl;
            usleep(100000); // Simulating network delay
        }

        // Wait for client ACK or packet loss notification
        int valread = read(client_socket, buffer, 1024);
        if (valread > 0) {
            if (strcmp(buffer, "ACK") == 0) {
                aimd(cwnd, false);  // No packet loss
            } else if (strcmp(buffer, "LOSS") == 0) {
                aimd(cwnd, true);  // Packet loss detected
            }
        }
        memset(buffer, 0, 1024);
    }

    close(client_socket);
    close(server_fd);
    return 0;
}
