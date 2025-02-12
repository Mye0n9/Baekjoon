#include <iostream>

int main(void){
    int sales;
    
    std::cout<<"What is your slaes price (-1 to end): ";
    std::cin>>sales;

    while (sales != -1){
        std::cout<<"This month's salary: "<<50+sales*0.12<<"won"<<std::endl;
        std::cout<<"What is your slaes price (-1 to end): ";
        std::cin>>sales;    
    }
    std::cout<<"End the program"<<std::endl;
}