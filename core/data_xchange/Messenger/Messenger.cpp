//
// Created by ankush on 3/26/23.
//

#include "Messenger.h"
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <spdlog/spdlog.h>

Messenger::Messenger(std::string uid) {
   key_t key = ftok(pathanme.c_str(), std::hash<std::string>{}(uid));
   if(key == -1) {
       spdlog::error("Could not convert path and identifier to IPC key for uid: {} : {}", uid, strerror(errno));
   }

   messageQueueId = msgget(key, 0666 | IPC_CREAT);

   if(messageQueueId == -1) {
       spdlog::error("Could not create/get message queue for UID: {} : {}", uid, strerror(errno));
   }
}

void Messenger::send(const std::string& raw_message) {
    if(messageQueueId == -1) {
        spdlog::error("Message queue not initialized, message send failed");
        return;
    }

    if(raw_message.length() > MAX_MSG_LEN){
        spdlog::error("Message length greater than {} no allowed, send failed", MAX_MSG_LEN);
        return;
    }

    MessageBuffer messageBuffer;
    messageBuffer.type = DEFAULT_MSG_TYPE;
    strcpy(messageBuffer.payload, raw_message.c_str());
    int retVal = msgsnd(messageQueueId, &messageBuffer, sizeof(messageBuffer), 0);

    if(retVal == -1) {
        spdlog::error("Could not send message: {}", strerror(errno));
    }
}

std::string Messenger::recv() const {
    if(messageQueueId == -1) {
        spdlog::error("Message queue not initialized, message send failed");
        return {};
    }

    MessageBuffer messageBuffer;
    size_t retVal = msgrcv(messageQueueId, &messageBuffer, sizeof(messageBuffer), DEFAULT_MSG_TYPE, 0);
    if(retVal == -1) {
        spdlog::error("Could not receive message: {}", strerror(errno));
        return {};
    }
    return {messageBuffer.payload, retVal - sizeof(messageBuffer.type)};
}
