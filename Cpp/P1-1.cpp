#include <iostream>

int main(void){
    int val1, val2, val3, val4, val5;
    int result = 0;

    std::cout<<"first intger: ";
    std::cin>>val1;

    std::cout<<"second intger: ";
    std::cin>>val2;

    std::cout<<"third intger: ";
    std::cin>>val3;

    std::cout<<"fourth intger: ";
    std::cin>>val4;

    std::cout<<"fifth intger: ";
    std::cin>>val5;

    result = val1+val2+val3+val4+val5;

    std::cout<<"Sum: "<<result<<std::endl;
    return 0;
}