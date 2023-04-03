//
// Created by ankush on 3/26/23.
//

#include "Subscriber.h"

Subscriber::Subscriber(std::shared_ptr<UserApplication> userApplication): userApplicationPtr(userApplication), messenger(userApplication->getId()) {
}

void Subscriber::sendMessage(const Message &message) {
    messenger.serializeAndSendMessage(message);

}

const UserApplicationPtr &Subscriber::getUserApplicationPtr() const {
    return userApplicationPtr;
}

bool operator==(std::shared_ptr<Subscriber> subscriberPtr1, std::shared_ptr<Subscriber> subscriberPtr2) {
    return subscriberPtr1->getUserApplicationPtr()->getId() == subscriberPtr2->getUserApplicationPtr()->getId();
}
