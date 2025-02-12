#include <iostream>

int main(void){
    int val;

    std::cout<<"Give the base number: ";
    std::cin>>val;

    for(int i=1;i<11;i++){
        std::cout<<val<<" x "<<i<<" = "<<val*i<<std::endl;
    }
    return 0;
}