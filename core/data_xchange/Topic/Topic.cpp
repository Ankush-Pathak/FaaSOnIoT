//
// Created by ankush on 3/27/23.
//

#include "Topic.h"

#include <utility>

Topic::Topic(std::string name) : name(std::move(name)) {}

void Topic::addSubscriber(SubscriberPtr &subscriberPtr) {
    subscriberPtrs->addSubscriber(subscriberPtr);
}

bool Topic::isMatch(const std::string &otherName) {
    return name == otherName;
}

void Topic::forwardMessageToSubscribers(const Message &message) {
    subscriberPtrs->sendMessage(message);
}

const std::string &Topic::getName() const {
    return name;
}
