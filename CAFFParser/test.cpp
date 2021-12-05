#include <iostream>
#include <fstream>
#include "CustomByteArray.h"
#include "CIFFParser.h"
#include "CAFFParser.h"

std::vector<unsigned char> load_file(std::string const& filepath)
{
    std::ifstream input( filepath, std::ios::binary );

    // copies all data into buffer
    std::vector<unsigned char> buffer(std::istreambuf_iterator<char>(input), {});
    return buffer;
}

int main(){
    {//caff parser header check
        std::cout<<"-------------"<<std::endl;
        std::cout << "caff parser header test:" << std::endl;
        const char* fp= "caff_header.caff";
        auto buffer = load_file(fp);
        CaffParser cp{};
        auto curr = buffer.begin();
        cp.checkHeader(curr, CustomByteArr{std::vector<unsigned char>{buffer.begin()+1,buffer.begin()+9}});
        std::cout << "Expected everything as 1: Magic: " << cp.getMagic() << " HeaderLen: " << cp.getHeaderLenOkay() << " HeaderValid:  "
        << cp.getHeaderValid() <<std::endl;
        std::cout << "caff parser header test completed" << std::endl;
    }

    {//caff parser credit check
        std::cout<<"-------------"<<std::endl;
        std::cout << "caff parser credit check:" << std::endl;
        const char* fp= "caff_credits.caff";
        auto buffer = load_file(fp);
        CaffParser cp{};
        auto curr = buffer.begin();
        cp.checkCredits(curr, CustomByteArr{std::vector<unsigned char>{buffer.begin()+1,buffer.begin()+9}});
        std::cout << "CreditValid: " << cp.getCreditValid() << std::endl;
        std::cout << "caff parser credit test completed" << std::endl;
    }

    {//caff parser animation check
        std::cout<<"-------------"<<std::endl;
        std::cout << "caff parser animation check:" << std::endl;
        const char* fp= "caff_animation.caff";
        auto buffer = load_file(fp);
        CaffParser cp{};
        auto curr = buffer.begin();
        cp.checkAnimation(curr, CustomByteArr{std::vector<unsigned char>{buffer.begin()+1,buffer.begin()+9}}, buffer.end());
        std::cout << "Every Animation Valid: " << cp.getEveryAnimValid() << std::endl;
        std::cout << "caff parser animation test completed" << std::endl;
    }

    {//caff parser total check
        std::cout<<"-------------"<<std::endl;
        std::cout << "caff parser total check:" << std::endl;
        const char* fp= "1.caff";
        auto buffer = load_file(fp);
        CaffParser cp{buffer};
        std::cout << "CAFF VALID expected(1): " << cp.isValid() << std::endl;
        std::cout << "magic expected(1): " << cp.getMagic() << std::endl;
        std::cout << "CAFF headerLenOkay expected(1): " << cp.getHeaderLenOkay() << std::endl;
        std::cout << "CAFF getAnimNumOkay expected(1): " << cp.getAnimNumOkay() << std::endl;
        std::cout << "CAFF getHeaderValid expected(1): " << cp.getHeaderValid() << std::endl;
        std::cout << "CAFF getCreditValid expected(1): " << cp.getCreditValid() << std::endl;
        std::cout << "CAFF getEveryAnimValid expected(1): " << cp.getEveryAnimValid() << std::endl;
        std::cout << "CAFF getNoExtraThing expected(1): " << cp.getNoExtraThing() << std::endl;
        std::cout << "caff parser total check completed" << std::endl;
    }

    {//ciff parser total check
        std::cout<<"-------------"<<std::endl;
        std::cout << "ciff parser total check:" << std::endl;
        const char* fp= "ciff.ciff";
        auto buffer = load_file(fp);
        CiffParser cp{buffer};
        std::cout << "CIFF VALID expected(1): " << cp.isValid() << std::endl;
        std::cout << "magic expected(1): " << cp.getMagic() << std::endl;
        std::cout << "CIFF getContentsOkay expected(1): " << cp.getContentsOkay() << std::endl;
        std::cout << "CIFF getCaptionOkay expected(1): " << cp.getCaptionOkay() << std::endl;
        std::cout << "CIFF getHadZero expected(1): " << cp.getHadZero() << std::endl;
        std::cout << "CIFF getHeaderOkay expected(1): " << cp.getHeaderOkay() << std::endl;
        std::cout << "CIFF getPixelNumOkay expected(1): " << cp.getHeaderOkay() << std::endl;
        std::cout << "ciff parser total check completed" << std::endl;
    }

    {//custom byte array check
        std::cout<<"-------------"<<std::endl;
        std::cout << "CustomByteArray test:" << std::endl;
        std::vector<unsigned char> bytes;
        bytes.push_back('D'); //68
        bytes.push_back('W'); //87
        CustomByteArr cba{bytes};
        //68+87*16^2
        std::cout << "Value expected(22340): " << cba.getValue() << std::endl;
    }
    return 0;
}
