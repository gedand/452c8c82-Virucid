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

int main(int argc, const char *argv[]){

    try{
        const char* fp= "";
		
		fp = argv[1];
        auto buffer = load_file(fp);
        CaffParser cp{buffer};

        if(cp.isValid()){
            std::cout << "Correct format" << std::endl;
            return 1;
        }
        else{
            std::cout <<"Bad format" << std::endl;
            return 0;
        }
    }
    catch(...){
        return 0;
    };
}
