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
    int processedAnim = 0;
    CustomByteArr animNum;
    CustomByteArr creatorLen;
    CustomByteArr measure;
    bool valid =false;
    bool magic = false;
    bool headerLenOkay = false;
    bool animNumOkay = false;
    bool headerValid = false;
    bool creditValid = false;
    bool everyAnimValid = true;
    bool noExtraThing = true;
public:
    CaffParser();
    CaffParser(std::vector<unsigned char>& buffer);
    void checkHeader(std::vector<unsigned char>::iterator& curr, CustomByteArr blockLen);
    void checkCredits(std::vector<unsigned char>::iterator& curr, CustomByteArr blockLen);
    void checkAnimation(std::vector<unsigned char>::iterator& curr, CustomByteArr blockLen, std::vector<unsigned char>::iterator const & dernier);
    bool isValid();
    bool getMagic();
    bool getHeaderLenOkay();
    bool getAnimNumOkay();
    bool getHeaderValid();
    bool getCreditValid();
    bool getEveryAnimValid();
    bool getNoExtraThing();
//    void setAnimNum(CustomByteArr value){animNum = value;}
};

#endif // CAFFPARSER_H_INCLUDED
