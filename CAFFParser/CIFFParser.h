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
    bool magic = false;
    bool contentsOkay = true;
    bool captionOkay = true;
    bool hadZero = false;
    bool headerOkay = true;
    bool pixelNumOkay = true;
public:
    CiffParser(std::vector<unsigned char> const & buffer);
    bool isValid();
    int tagLen();
    void writePixels();
    void checkMagic(std::vector<unsigned char>::const_iterator& curr);
    void checkContentSize(std::vector<unsigned char>::const_iterator& curr);
    void checkCaption(std::vector<unsigned char>::const_iterator& curr);
    void checkHeader(std::vector<unsigned char>::const_iterator& curr);
    void checkTag(std::vector<unsigned char>::const_iterator& curr, std::vector<unsigned char>const & buffer);
    void checkPixels(std::vector<unsigned char>::const_iterator& curr, std::vector<unsigned char>const & buffer);
    bool getMagic();
    bool getContentsOkay();
    bool getCaptionOkay();
    bool getHadZero();
    bool getHeaderOkay();
    bool getPixelNumOkay();
};



#endif // CIFFPARSER_H_INCLUDED
