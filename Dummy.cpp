#include <iostream>
#include <cstring>
#include <netdb.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <sstream> 

int main() {
    std::string email, password;


    std::cout << "Enter email: ";
    std::getline(std::cin, email);
    std::cout << "Enter password: ";
    std::getline(std::cin, password);

    std::ostringstream oss;
    oss << "{\"email\":\"" << email << "\",\"password\":\"" << password << "\"}";
    std::string json_payload = oss.str();

    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        std::cerr << "Socket creation failed" << std::endl;
        return -1;
    }

 
    const char* hostname = "mern-secure.onrender.com";
    struct hostent* server = gethostbyname(hostname);
    if (server == nullptr) {
        std::cerr << "No such host: " << hostname << std::endl;
        close(sock);
        return -1;
    }


    sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(80); // HTTP port
    std::memcpy(&server_addr.sin_addr.s_addr, server->h_addr, server->h_length);

    if (connect(sock, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        std::cerr << "Connection to server failed" << std::endl;
        close(sock);
        return -1;
    }

    std::ostringstream request_stream;
    request_stream << "POST /api/auth/signin HTTP/1.1\r\n"
                   << "Host: mern-secure.onrender.com\r\n"
                   << "Content-Type: application/json\r\n"
                   << "Content-Length: " << json_payload.size() << "\r\n"
                   << "Connection: close\r\n"
                   << "\r\n"
                   << json_payload;

    std::string http_request = request_stream.str();

    // Send HTTP request
    send(sock, http_request.c_str(), http_request.size(), 0);

    char buffer[4096];
    int bytes_received = recv(sock, buffer, sizeof(buffer) - 1, 0);
    if (bytes_received > 0) {
        buffer[bytes_received] = '\0'; // Null-terminate the response
        std::cout << buffer << std::endl;
    }

    close(sock);
    return 0;
}
