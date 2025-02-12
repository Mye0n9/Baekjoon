#include <iostream>

int main(void){
    char name[100];
    char lang[200];

    std::cout<<"What is your name? ";
    std::cin>>name;

    std::cout<<"What is your favorite Programming Language? ";
    std::cin>>lang;

    std::cout<<"My name is "<<name<<std::endl;
    std::cout<<"My favorite programming language is "<<lang<<std::endl;
}