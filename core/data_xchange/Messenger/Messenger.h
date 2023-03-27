//
// Created by ankush on 3/26/23.
//

#ifndef DATA_XCHANGE_MESSENGER_H
#define DATA_XCHANGE_MESSENGER_H


#include <string>

class Messenger {
    int messageQueueId;
    const std::string pathanme = "faas_on_iot";
    const int DEFAULT_MSG_TYPE = 1;
    const int MAX_MSG_LEN = 1024;

    struct MessageBuffer {
        long type;
        char payload[1024];
    };

public:
    Messenger(std::string uid);
    void send(const std::string& raw_message);
    std::string recv() const;

};


#endif //DATA_XCHANGE_MESSENGER_H
