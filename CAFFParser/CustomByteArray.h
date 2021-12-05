#ifndef CUSTOMBYTEARRAY_H_INCLUDED
#define CUSTOMBYTEARRAY_H_INCLUDED

#include <vector>


class CustomByteArr {
    int value;
public:
    CustomByteArr();
    CustomByteArr(std::vector<unsigned char> const& bytes);
    int getValue() const ;
};



#endif // CUSTOMBYTEARRAY_H_INCLUDED
