//
// Created by ankpath on 3/26/23.
//

#include <queue>
#include <mutex>
#include "Server/Request/Request.h"
#include "Topic/Topic.h"
#include "Publishers/Publishers.h"

int main() {
    std::queue<RequestPtr> requestQueue;
    std::mutex requestQueueLock;
    TopicSet topicSet;
    Publishers publishers;
    while (1) {
        RequestPtr requestPtr;
        {
            std::lock_guard<std::mutex> lockGuard(requestQueueLock);
            requestPtr = requestQueue.front();
            requestQueue.pop();
        }
        switch(requestPtr->getReqType()) {
            case Request::PUB:
                TopicPtr topicPtr = std::make_shared<Topic>(requestPtr->getTopic());
                if(topicSet.find(topicPtr) != topicSet.end())
                    topicSet.insert(topicPtr);
                else
                    topicPtr = *topicSet.find(topicPtr);
                UserApplicationPtr userApplicationPtr = std::make_shared<UserApplication>(requestPtr->getUid());
                PublisherPtr publisherPtr = std::make_shared<Publisher>(userApplicationPtr);
                publisherPtr->addTopic(topicPtr);
                publishers.addPublisher(publisherPtr);
                break;
        }

    }
    return 0;
}
