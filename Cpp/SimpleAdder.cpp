#include <iostream>

int main(void){
    int val1;
    std::cout<<"first Num: ";
    std::cin>>val1;

    int val2;
    std::cout<<"Second Num: ";
    std::cin>>val2;

    int result = val1 + val2;
    std::cout<<"Result: "<<result<<std::endl;
    return 0;
}