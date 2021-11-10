#include "CustomByteArray.h"
#include <iostream>
#include <math.h>

CustomByteArr::CustomByteArr(){ value = 0;}

CustomByteArr::CustomByteArr(std::vector<unsigned char> const& bytes){
    value = 0;
    for(std::size_t i = 0; i < bytes.size(); ++i){
        value += bytes[i] * pow(16,i*2);
        }
}

CustomByteArr::getValue() const { return value;}

std::ostream& operator <<(std::ostream& os, const CustomByteArr& c){
    os.precision(9);
    os << c.getValue() << std::endl;
    return os;
}
