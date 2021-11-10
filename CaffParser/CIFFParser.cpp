#include "CIFFParser.h"
#include <string.h>

CiffParser::CiffParser(std::vector<unsigned char> const & buffer){
    auto curr = buffer.begin();
    bool magic = false;
    if(*curr == 'C' && *(curr+1) == 'I' && *(curr+2) == 'F' && *(curr+3) == 'F'){
        magic = true;
    }
    curr += 4;
    headerSize = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};

    curr += 8;
    contentSize = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};
    curr += 8;
    width = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};
    curr += 8;
    height = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};
    curr += 8;

    bool contentsOkay = true;
    if(contentSize.getValue() != height.getValue()*width.getValue()*3){
        contentsOkay = false;
        //throw std::length_error("CONTENTS SIZE NOT EQUAL WITH HEIGHT*WIDTH*3");
    }

    bool captionOkay = true;
    for(auto i = curr; i<curr-fixPart+headerSize.getValue(); ++i){
        if(*i == '\n'){
            caption = std::vector<unsigned char>{curr, i};
            curr = ++i;
            break;
        }
        if(i+1 == curr-fixPart+headerSize.getValue()){
            captionOkay = false;
        }
    }

    bool hadZero = false;
    for(auto i = curr; i < buffer.begin()+headerSize.getValue(); ++i){
        if(*i == '\0'){
            tags.push_back(&(*curr));
            curr = ++i;
            hadZero = true;
        }
    }

    bool headerOkay = true;
    if(headerSize.getValue() != fixPart + (int)caption.size() + tagLen()+1){
        headerOkay = false;
        //throw std::length_error("HEADER SIZE NOT EQUAL WITH THE HEADER'S SIZE");
    }

    pixels = std::vector<unsigned char>{curr, buffer.end()};

    bool pixelNumOkay = true;
    if(contentSize.getValue() != (int)pixels.size()){
        pixelNumOkay = false;
        //throw std::length_error("CONTENTS SIZE NOT EQUAL WITH NUM OF PIXELS");
    }
    if(pixelNumOkay && headerOkay && hadZero && captionOkay && contentsOkay && magic){
        valid = true;
    }else{
        valid = false;
    }
}

bool CiffParser::isValid(){return valid;}

int CiffParser::tagLen(){
    int len = 0;
    for(auto a: tags){
        len += strlen((const char*)a);
    }
    return len+tags.size();
}
