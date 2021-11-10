#include "CAFFParser.h"
#include "CIFFParser.h"

CaffParser::CaffParser(std::vector<unsigned char>& buffer){
    std::vector<unsigned char>::iterator curr = buffer.begin();
    if((int)*curr != 1){
        return;
    }

    bool magic = false; //done
    bool headerLenOkay = false;//done
    bool animNumOkay = false;//done
    bool headerValid = false;//done
    bool creditValid = false;//done
    bool everyAnimValid = true;//done
    bool noExtraThing = true;//done

    CustomByteArr blockLen{};
    int processedAnim = 0;

    while(curr < buffer.end()){
        std::vector<unsigned char> preBlock{curr+1,curr+9};
        blockLen = CustomByteArr{preBlock};
        switch(*curr){
            case 1:
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
                break;
            case 2:{
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
                break;
                }
            case 3:{
                curr += initBlockLen;
                if(everyAnimValid){
                    CiffParser cp{std::vector<unsigned char>{curr+8,curr+blockLen.getValue()}};
                    everyAnimValid = cp.isValid();
                }
                curr += blockLen.getValue();
                ++processedAnim;
                if(processedAnim == animNum.getValue()){
                    animNumOkay = true;
                }else{
                    animNumOkay = false;
                }
                break;
                }
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

bool CaffParser::isValid() {return valid;}
