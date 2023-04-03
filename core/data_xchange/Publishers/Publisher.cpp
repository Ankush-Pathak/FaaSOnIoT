//
// Created by ankush on 3/26/23.
//

#include "Publisher.h"

Publisher::Publisher(UserApplicationPtr &userApplicationPtr) : userApplicationPtr(userApplicationPtr), messenger(userApplicationPtr->getId()) {
}

void Publisher::addTopic(TopicPtr &topicPtr) {
    topicPtrs.push_back(topicPtr);
}

void Publisher::checkAndProcessMessage() {
    if(!messenger.isMessagePending())
        return;
    Message message = messenger.recvAndDeserializeMessage();
    checkTopicMatchAndForward(message);
}

void Publisher::checkTopicMatchAndForward(const Message &message) {
    for(TopicPtr &topicPtr: topicPtrs) {
        if(topicPtr->isMatch(message.topic())) {
           topicPtr->forwardMessageToSubscribers(message);
        }
    }
}

const UserApplicationPtr &Publisher::getUserApplicationPtr() const {
    return userApplicationPtr;
}

bool operator==(std::shared_ptr<Publisher> publisherPtr1, std::shared_ptr<Publisher> publisherPtr2) {
    return publisherPtr1->getUserApplicationPtr()->getId() == publisherPtr2->getUserApplicationPtr()->getId();
}
