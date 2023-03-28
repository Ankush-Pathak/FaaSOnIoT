//
// Created by ankush on 3/26/23.
//

#include "Publishers.h"

Publishers::Publishers() {}

void Publishers::addPublisher(std::shared_ptr<Publisher> &publisherPtr) {
    publishers.insert(publisherPtr);
}
