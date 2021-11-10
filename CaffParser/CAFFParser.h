#ifndef CAFFPARSER_H_INCLUDED
#define CAFFPARSER_H_INCLUDED

#include "CustomByteArray.h"

class CaffParser {
    std::vector<std::vector<unsigned char>> initBlocks{4};
    std::vector<unsigned char> header;
    std::vector<unsigned char> credits;
    std::vector<unsigned char> animation;
    std::vector<unsigned char> creator;
    const int initBlockLen = 9;
    const int headerLen = 20;
    CustomByteArr animNum;
    CustomByteArr creatorLen;
    CustomByteArr measure;
    bool valid =false;
public:
    CaffParser(std::vector<unsigned char>& buffer);
    bool isValid();
};

#endif // CAFFPARSER_H_INCLUDED
