#ifndef ETMORDER_H
#define ETMORDER_H
#include <iostream>
#include <cmath>
#include <string>
#include <myphpdatabase.h>

using namespace std;

class etmorder
{
private:
    /* Generating Unique ID */
    unsigned long long orderID = ++lastGeneratedID;
    static unsigned long long lastGeneratedID;

    /* Location Variables */
    string source;
    string destination;

    /* Cargo Variables */
    double weight;
    double size;
    string condition;

    /* Finances */
    double shippingRate;
    double companyComission;

    /* Financial Calculations */
    double calculateShippingRate();
    double calculateCompanyComission();

public:
    void order(string source, string destination, double weight, double size, string condition);
    void OrderSys();
    void generateReceipt();
};

#endif // ETMSORDER_H
