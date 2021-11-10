#ifndef CIFFPARSER_H_INCLUDED
#define CIFFPARSER_H_INCLUDED

#include "CustomByteArray.h"

class CiffParser{
    int fixPart = 4+8+8+8+8; /*magic+headerSize+contentSize+width+height*/
    CustomByteArr headerSize;
    CustomByteArr contentSize;
    CustomByteArr width;
    CustomByteArr height;
    std::vector<unsigned char> pixels{};
    std::vector<unsigned char> caption{};
    std::vector<const unsigned char*> tags{};
    bool valid = false;
public:
    CiffParser(std::vector<unsigned char> const & buffer);
    bool isValid();
    int tagLen();
};



#endif // CIFFPARSER_H_INCLUDED
