//
// Created by ankush on 3/26/23.
//

#include "Subscribers.h"

void Subscribers::addSubscriber(std::shared_ptr<Subscriber> &subscriberPtr) {
    subscribers.insert(subscriberPtr);

}

void Subscribers::sendMessage(const Message &message) {
    for(std::shared_ptr<Subscriber> subscriberPtr: subscribers) {
        subscriberPtr->sendMessage(message);
    }
}
