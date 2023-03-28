//
// Created by ankush on 3/26/23.
//

#ifndef DATA_XCHANGE_MESSENGER_H
#define DATA_XCHANGE_MESSENGER_H


#include <string>
#include "messages/pub_sub_messages.pb.h"

class Messenger {
    int messageQueueId;
    const static std::string pathanme;
    const static int DEFAULT_MSG_TYPE;
    const static int MAX_MSG_LEN;

    struct MessageBuffer {
        long type;
        char payload[1024];
    };
    void send(const std::string& raw_message);
    std::string recv() const;
public:
    Messenger(std::string uid);
    bool isMessagePending();
    Message recvAndDeserializeMessage();
    void serializeAndSendMessage(const Message &message);

};

const std::string Messenger::pathanme = "faas_on_iot";
const int Messenger::DEFAULT_MSG_TYPE = 1;
const int Messenger::MAX_MSG_LEN = 1024;


#endif //DATA_XCHANGE_MESSENGER_H
