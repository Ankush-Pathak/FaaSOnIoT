//
// Created by ankush on 3/26/23.
//

#ifndef DATA_XCHANGE_PUBLISHERS_H
#define DATA_XCHANGE_PUBLISHERS_H


#include <unordered_map>
#include "UserApplication/UserApplication.h"
#include "Publisher.h"

class Publishers {
    std::unordered_map<Publisher, std::string> publisher_to_topic;

};


#endif //DATA_XCHANGE_PUBLISHERS_H
