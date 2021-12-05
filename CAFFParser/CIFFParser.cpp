#include "CIFFParser.h"
#include <string.h>
#include <iostream>
#include <fstream>
#include <errno.h>

CiffParser::CiffParser(std::vector<unsigned char> const & buffer){
    auto curr = buffer.begin();

    checkMagic(curr);

    checkContentSize(curr);

    checkCaption(curr);

    checkTag(curr, buffer);

    checkHeader(curr);

    checkPixels(curr, buffer);

}

bool CiffParser::isValid(){return pixelNumOkay && headerOkay && hadZero && captionOkay && contentsOkay && magic;}

int CiffParser::tagLen(){
    int len = 0;
    for(auto a: tags){
        len += strlen((const char*)a);
    }
    return len+tags.size();
}

void CiffParser::writePixels(){
    char title[caption.size()+1+4];

    int i;
    for(i = 0; caption.begin()+i < caption.end(); ++i){
        title[i] = caption.at(i);
    }
    title[i] = '\0';
    const char dat[5] = ".dat";

    strncat(title,dat,4);

    std::cout<<title<<std::endl;
    std::ofstream wf(title, std::ios::out | std::ios::binary);

    wf<<width.getValue()<<std::endl;
    wf<<height.getValue()<<std::endl;
    for(auto it = pixels.begin(); it < pixels.end() && pixels.size()>0; it++){
        wf << (*it);
    }
    wf.close();
}

void CiffParser::checkMagic(std::vector<unsigned char>::const_iterator& curr){
    if(*curr == 'C' && *(curr+1) == 'I' && *(curr+2) == 'F' && *(curr+3) == 'F'){
        magic = true;
    }
    curr += 4;
}

void CiffParser::checkContentSize(std::vector<unsigned char>::const_iterator& curr){

    headerSize = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};
    curr += 8;
    contentSize = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};
    curr += 8;
    width = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};
    curr += 8;
    height = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};
    curr += 8;

    if(contentSize.getValue() != height.getValue()*width.getValue()*3){
        contentsOkay = false;
        //throw std::length_error("CONTENTS SIZE NOT EQUAL WITH HEIGHT*WIDTH*3");
    }
}
void CiffParser::checkCaption(std::vector<unsigned char>::const_iterator& curr){
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
}

void CiffParser::checkTag(std::vector<unsigned char>::const_iterator& curr, std::vector<unsigned char>const & buffer){
    for(auto i = curr; i < buffer.begin()+headerSize.getValue(); ++i){
        if(*i == '\0'){
            tags.push_back(&(*curr));
            curr = ++i;
            hadZero = true;
        }
    }
}

void CiffParser::checkHeader(std::vector<unsigned char>::const_iterator& curr){
    if(headerSize.getValue() != fixPart + (int)caption.size() + tagLen()+1){
        headerOkay = false;
        //throw std::length_error("HEADER SIZE NOT EQUAL WITH THE HEADER'S SIZE");
    }
}

void CiffParser::checkPixels(std::vector<unsigned char>::const_iterator& curr, std::vector<unsigned char>const & buffer){
    pixels = std::vector<unsigned char>{curr, buffer.end()};
    if(contentSize.getValue() != (int)pixels.size()){
        pixelNumOkay = false;
        //throw std::length_error("CONTENTS SIZE NOT EQUAL WITH NUM OF PIXELS");
    }
}

bool CiffParser::getMagic(){return magic;}
bool CiffParser::getContentsOkay(){return contentsOkay;}
bool CiffParser::getCaptionOkay(){return captionOkay;}
bool CiffParser::getHadZero(){return hadZero;}
bool CiffParser::getHeaderOkay(){return headerOkay;}
bool CiffParser::getPixelNumOkay(){return pixelNumOkay;}

