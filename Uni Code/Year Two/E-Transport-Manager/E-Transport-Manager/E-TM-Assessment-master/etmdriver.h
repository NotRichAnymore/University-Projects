#ifndef ETMDRIVER_H
#define ETMDRIVER_H
#include <QtSql>
#include <QSqlDatabase>
#include <QRegularExpression>
#include <iostream>

#include "myphpdatabase.h"


class etmdriver: public myphpdatabase
{
    int driverID;
    QString firstName;
    QString lastName;
    QString usernameD;
    QString userEmail;
    QString passwordD;
    QString userAddress;
    QString streetName;
    QString cityName;
    QString postCode;
    int phoneNumber;
    QString driverLicence;
    QString dimensionsLorry;
    int weightLorry;
    int code = (rand() % 69866)+89560;

public:
   bool authenticatingDriverLicence(QString);
   void newDriver();
   void signinDriver();

};

#endif // ETMDRIVER_H
