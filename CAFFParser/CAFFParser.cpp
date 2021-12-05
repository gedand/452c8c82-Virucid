#include "CAFFParser.h"
#include "CIFFParser.h"
#include <iostream>

CaffParser::CaffParser(){};

CaffParser::CaffParser(std::vector<unsigned char>& buffer){
    std::vector<unsigned char>::iterator curr = buffer.begin();
    if((int)*curr != 1){
        return;
    }
    CustomByteArr blockLen{};
    while(curr < buffer.end()){
        std::vector<unsigned char> preBlock{curr+1,curr+9};
        blockLen = CustomByteArr{preBlock};
        switch(*curr){
            case 1:
                checkHeader(curr, blockLen);
                break;
            case 2:
                checkCredits(curr, blockLen);
                break;
            case 3:
                checkAnimation(curr, blockLen, buffer.end());
                break;
            default:
                ++curr;
                noExtraThing = false;
                return;
        }
    }

    if(magic && headerLenOkay && animNumOkay && headerValid && creditValid && everyAnimValid && noExtraThing){
        valid = true;
    } else {
        valid = false;
    }
}

bool CaffParser::isValid() {return magic && headerLenOkay && animNumOkay && headerValid && creditValid && everyAnimValid && noExtraThing;}

void CaffParser::checkHeader(std::vector<unsigned char>::iterator& curr, CustomByteArr blockLen){

    curr += initBlockLen;
    if(header.empty()){
        header.insert(header.end(), curr, curr+headerLen);
        if(*curr == 'C' && *(curr+1) == 'A' && *(curr+2) == 'F' && *(curr+3) == 'F'){
            magic = true;
        }

        CustomByteArr h{std::vector<unsigned char>{header.begin()+4, header.begin()+12}};
        if(h.getValue() == blockLen.getValue() && blockLen.getValue() == headerLen){
            headerLenOkay = true;
            headerValid = true;
        }

        animNum = CustomByteArr{std::vector<unsigned char>{header.begin()+12, header.begin()+20}};
    }
    curr += headerLen;
}

void CaffParser::checkCredits(std::vector<unsigned char>::iterator& curr, CustomByteArr blockLen){
    curr += initBlockLen;
    CustomByteArr Year{std::vector<unsigned char>{curr, curr+2}};
    curr += 2;
    curr += 4;
    creatorLen = CustomByteArr{std::vector<unsigned char>{curr, curr+8}};
    curr += 8;
    creator = std::vector<unsigned char>{curr, curr+creatorLen.getValue()};
    curr += creatorLen.getValue();
    if(creatorLen.getValue()+14 == blockLen.getValue()){
        creditValid = true;
    }
}

void CaffParser::checkAnimation(std::vector<unsigned char>::iterator& curr, CustomByteArr blockLen, std::vector<unsigned char>::iterator const& dernier){
    curr += initBlockLen;
    if(everyAnimValid){
        int i;
        for( i = 0; curr+8+i!=dernier; ++i);
        if(i+8 >= blockLen.getValue())
        {
            CiffParser cp{std::vector<unsigned char>{curr+8,curr+blockLen.getValue()}};
            everyAnimValid = cp.isValid();
            if(processedAnim == 0){
                cp.writePixels();
            }
        }else{
            everyAnimValid=false;
        }
    }
    curr += blockLen.getValue();
    ++processedAnim;
    if(processedAnim == animNum.getValue()){
        animNumOkay = true;
    }else{
        animNumOkay = false;
    }

}
bool CaffParser::getMagic(){return magic;}
bool CaffParser::getHeaderLenOkay(){return headerLenOkay;}
bool CaffParser::getAnimNumOkay(){return animNumOkay;}
bool CaffParser::getHeaderValid(){return headerValid;}
bool CaffParser::getCreditValid(){return creditValid;}
bool CaffParser::getEveryAnimValid(){return everyAnimValid;}
bool CaffParser::getNoExtraThing(){return noExtraThing;}
