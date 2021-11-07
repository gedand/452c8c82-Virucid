#include <iostream>
#include <fstream>
#include <vector>
#include <cstddef>
#include <math.h>
#include <string.h>

using namespace std;


std::ostream& operator << (std::ostream& os, const std::vector<unsigned char>& v)
{
    os << "[";
    for (typename std::vector<unsigned char>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        os << " " << (int)*ii;
    }
    os << "]" << std::endl;
    return os;
}

std::ostream& operator << (std::ostream& os, const std::vector<const unsigned char*>& v)
{
    os << "[";
    for (typename std::vector<const unsigned char*>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        os << " " << *ii;
    }
    os << "]" << std::endl;
    return os;
}


class CustomByteArr {
    int value;
public:
    CustomByteArr(): value(0){}
    CustomByteArr(std::vector<unsigned char> const& bytes){
        value = 0;
        for(size_t i = 0; i < bytes.size(); ++i){
            value += bytes[i] * pow(16,i*2);
        }
    }
    int getValue() const {return value;}
};

std::ostream& operator <<(std::ostream& os, const CustomByteArr& c){
    os.precision(9);
    os << c.getValue() << std::endl;
    return os;
}

class CiffParser{
    int fixPart = 4+8+8+8+8; /*magic+headerSize+contentSize+width+height*/
    CustomByteArr headerSize;
    CustomByteArr contentSize;
    CustomByteArr width;
    CustomByteArr height;
    std::vector<unsigned char> pixels{};
    std::vector<unsigned char> caption{};
    std::vector<const unsigned char*> tags{};
    bool valid = true;
public:
    CiffParser(std::vector<unsigned char> const & buffer){
        auto curr = buffer.begin();
        bool magic = false;
        if(*curr == 'C' && *(curr+1) == 'I' && *(curr+2) == 'F' && *(curr+3) == 'F'){
            magic = true;
        }
        curr += 4; // skip magic
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
    bool isValid(){return valid;}
    int tagLen(){
        int len = 0;
        for(auto a: tags){
            len += strlen((const char*)a);
        }
        return len+tags.size();
    }
};

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
    bool valid;
public:
    CaffParser(std::vector<unsigned char>& buffer){
        vector<unsigned char>::iterator curr = buffer.begin();
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
                        curr += headerLen;
                    }
                    break;
                case 2:{
                    curr += initBlockLen;
                    CustomByteArr Year{std::vector<unsigned char>{curr, curr+2}};
                    curr += 2;
                    //cout << "M: " << (int)*curr << "D: " << (int)*(curr+1) << "h: " << (int)*(curr+2) << "m: " << (int)*(curr+3);
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
                    cout << "\nSULLYEDUNK FATER\n";
                    noExtraThing = false;
            }
        }

        if(magic && headerLenOkay && animNumOkay && headerValid && creditValid && everyAnimValid && noExtraThing){
            valid = true;
        } else {
            valid = false;
        }

        /*
        initBlocks[0].insert(initBlocks[0].end(), curr, curr+initBlockLen);
        curr += initBlockLen;


        initBlocks[1].insert(initBlocks[1].end(), curr, curr+initBlockLen);
        curr += initBlockLen;

        measure = CustomByteArr{std::vector<unsigned char> {initBlocks[1].begin()+1, initBlocks[1].begin()+9}};
        credits.insert(credits.end(), curr, curr+measure.getValue());
        curr += measure.getValue();

        initBlocks[2].insert(initBlocks[2].end(), curr, curr+initBlockLen);
        curr += initBlockLen;

        measure = CustomByteArr{std::vector<unsigned char> {initBlocks[2].begin()+1, initBlocks[2].begin()+9}};
        animation.insert(animation.end(), curr, curr+measure.getValue());
        curr += measure.getValue();

        cout <<"curr next value, expected: 3 - " << (int)*curr <<endl;

        CiffParser ciffp{vector<unsigned char>{animation.begin()+8, animation.end()}};
        cout << "ciff is valid: " << ciffp.isValid()<<endl;*/
        /*animation.reserve(measure.getValue());
        for(auto b = curr; b < curr+measure.getValue(); ++b){
                cout<<"H ";
            animation.push_back(*b);
        }
        cout << "measure : " <<measure;*/
    }
    bool isValid() {return valid;}
};


std::vector<unsigned char> load_file(std::string const& filepath)
{

    std::ifstream input( filepath, std::ios::binary );

    // copies all data into buffer
    std::vector<unsigned char> buffer(std::istreambuf_iterator<char>(input), {});
    return buffer;
}


int main()
{
    const char* fp= "1.caff";

    auto buffer = load_file(fp);

    CaffParser cp{buffer};

    std::cout << "DOES THE GIVEN CAFF VALID? " << cp.isValid() <<std::endl;

    //const char* fp= "../../caff_files/3.caff";
    /*const char* a= "../../caff_files/AAA.txt";



    const int initBlockLen = 9;
    const int headerLen = 20;
    const int credit_fix_len = 14;
    const int animation_fix_len = 8;

    int len = 8;
    std::vector<unsigned char> vec;
    vec.push_back(193);
    vec.push_back(136);
    vec.push_back(30);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(0);
    CustomByteArr cba(vec);*/
    /*
    std::ifstream rf("../../caff_files/1.caff", std::ios::out | std::ios::binary);

    if(!rf) {
      std::cout << "Cannot open file!" << std::endl;
      return 1;
      }*/

//    vector<unsigned char>::iterator curr = buffer.begin();
/*

    std::cout << "INIT BLOCK 1: " << std::vector<unsigned char>(curr, curr+initBlockLen) << std::endl;

    curr += initBlockLen;
    std::cout << "HEADER: " << std::vector<unsigned char>(curr, curr+headerLen) << std::endl;
    curr += headerLen;
    std::cout << "INIT BLOCK 2: " << std::vector<unsigned char>(curr, curr+initBlockLen) << std::endl;
    vec.clear();
    vec.insert(vec.end(), curr+1,curr+9);
    CustomByteArr c1{vec};
    std::cout << c1;
    curr += initBlockLen;*/
    /*preprop needed cuz creator_len*//*
    std::cout << "CREDITS: " << std::vector<unsigned char>(curr, curr+c1.getValue()) << std::endl;

    curr += c1.getValue();
    std::cout << "INIT BLOCK 3: " << std::vector<unsigned char>(curr, curr+initBlockLen) << std::endl;
    vec.clear();
    vec.insert(vec.end(), curr+1,curr+9);
    c1 = CustomByteArr{vec};
    std::cout << c1;

    curr += initBlockLen;
    //std::cout << "ANIMATION: " << std::vector<unsigned char>(curr, curr+c1.getValue()) << std::endl;
*/


//    std::cout <<  <<std::endl;
    return 0;
}
