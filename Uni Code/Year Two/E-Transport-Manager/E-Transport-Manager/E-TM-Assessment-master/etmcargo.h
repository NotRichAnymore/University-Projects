#ifndef ETMCARGO_H
#define ETMCARGO_H
#include <QtSql>
#include <QSqlDatabase>
#include <iostream>

#include "etmorder.h"
#include "myphpdatabase.h"


class etmcargo: public myphpdatabase
{
    int cargoOID;
    QString firstName;
    QString lastName;
    QString usernameC;
    QString userEmail;
    QString passwordC;
    QString userAddress;
    QString streetName;
    QString cityName;
    QString postCode;
    int phoneNumber;
    //generates random code for verification purposes
    int code = (rand() % 69866)+89560;

public:
   void print_menuC();
   void newCargoO();
   void signinCargo();
   QString cargoConnectionToDatabase();
};

#endif // ETMCARGO_H
