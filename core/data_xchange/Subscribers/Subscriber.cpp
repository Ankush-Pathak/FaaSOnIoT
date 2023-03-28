//
// Created by ankush on 3/26/23.
//

#include "Subscriber.h"

Subscriber::Subscriber(UserApplication *userApplication): userApplicationPtr(userApplication), messenger(userApplication->getId()) {
}

void Subscriber::sendMessage(const Message &message) {
    messenger.serializeAndSendMessage(message);

}

const UserApplicationPtr &Subscriber::getUserApplicationPtr() const {
    return userApplicationPtr;
}
