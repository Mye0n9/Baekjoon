#include <iostream>

int main(void){
    char name[100];
    char phone[100];

    std::cout<<"What is your name? ";
    std::cin>>name;

    std::cout<<"What is your phone number? ";
    std::cin>>phone;

    std::cout<<"My name is "<<name<<std::endl;
    std::cout<<"My phone number is "<<phone<<std::endl;

    return 0;
}