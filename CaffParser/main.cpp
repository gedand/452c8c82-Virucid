#include <fstream>
#include "CustomByteArray.h"
#include "CIFFParser.h"
#include "CAFFParser.h"


/*
operatros to print a vector if want to debug

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
*/

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

        return cp.isValid() ? 1 : 0;
    }
    catch(...){
        return 0;
    };
}
