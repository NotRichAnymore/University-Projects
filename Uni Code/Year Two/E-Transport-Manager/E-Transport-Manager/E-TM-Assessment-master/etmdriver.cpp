#include "etmdriver.h"

//boolean to check if the drivers licence matches the right format. Regular expressions is used for this.
bool etmdriver::authenticatingDriverLicence(QString driverLicence)
{
    //follows the UK driving licence pattern XXXXX 000000 XXX00
    QRegularExpression driverIDPattern("(([A-Z]{5})([0-9]{6})([A-Z0-9]{5}))");
    QRegularExpressionMatch check = driverIDPattern.match(driverLicence);
    if(check.hasMatch())
    {
        std::cout << "Verification succesfull" << std::endl;
        return true;
    }
    else
    {
        std::cout << "invalid license";
        return  false;
    }



}

//user signs into respective account
void etmdriver::signinDriver()
{
    QTextStream input(stdin);
    QString usernameLogin;

    //user enters username to get it verfied and log in
    std::cout << "Enter your username: " << std::endl;
    input >> usernameLogin;


    auto database_connection = myphpdatabase();
    database_connection.init_database();

    if(!database_connection.database_status())
    {
        std::cout << "database offline";
        database_connection.init_database();
    }


    if(database_connection.database_status())
    {
        std::cout << "database online" << std::endl;

        QSqlQuery qry;
        qry.prepare("SELECT usernameD FROM EtmDriverData WHERE usernameD = :usernameD");
        qry.bindValue(":usernameD",usernameLogin);


        bool  usernameMatched = false;

        if(qry.exec())
        {
            usernameMatched = qry.next();

            if(usernameMatched == true)
            {
                QString userPassword;
                std::cout << "Enter your password: " << std::endl;
                input >> userPassword;


                QSqlQuery qryPassword;
                qryPassword.prepare("SELECT passwordD FROM EtmDriverData WHERE passwordD = :passwordD");
                qryPassword.bindValue(":passwordD",userPassword);
                bool passwordFound = false;
                if(qryPassword.exec())
                {
                    passwordFound = qryPassword.next();
                    if(passwordFound == true)
                    {
                        QTextStream output(stdout);

                        output << "Welcome to E-TM,"<< usernameLogin << endl;

                    }
                    else
                    {
                        std::cout << "password is incorrect";
                    }
                }
            }
            else
            {
                std::cout << "Email could not be found" << std::endl;
            }
        }
    }
    else
    {
        std::cout << "Not Connected to database" << std::endl;
    }
}

void etmdriver::newDriver()
{
    QTextStream input(stdin);

    driverID = 0; // auto increment has been initialized to the database and acts as the primary key
    std::cout << "Enter your first name: " << std::endl;
    input >> firstName;
    std::cout << "Enter your last name: "<< std::endl;
    input >> lastName;
    std::cout << "Enter a username: "<< std::endl;
    input >> usernameD;
    std::cout << "Enter your email: " << std::endl;
    input >> userEmail;
    std::cout << "Enter a password: "<< std::endl;
    input >> passwordD;
    std::cout << "Enter your home/business address: "<< std::endl;
    input >> userAddress;
    std::cout << "Enter your street name: "<< std::endl;
    input >> streetName;
    std::cout << "Enter your City: "<< std::endl;
    input >> cityName;
    std::cout << "Enter your postcode: "<< std::endl;
    input >> postCode;
    std::cout << "Enter your phone number: "<< std::endl;
    input >> phoneNumber;

    //driver licence details obtained
    std::cout << "-----Driver Licence Details-----" << std::endl;
    try
    {
        std::cout << "Enter your driver license: "<< std::endl;
        input >> driverLicence;
        bool driverCheck = authenticatingDriverLicence(driverLicence);
        if(!driverCheck)
        {
            throw(driverCheck);
        }
    } catch (bool driverInvalid)
    {
        std::cout << "Please enter a valid driver licence" << std::endl;
    }

    //obtaining driver's lorry details
    std::cout << "-------Lorry Details-----" << std::endl;
    std::cout << "Enter the dimensions of your lorry: " << std::endl;
    input >> dimensionsLorry;
    std::cout << "Enter the weight of the lorry: "<<std::endl;
    input >> weightLorry;

    std::cout << "Enter the verification code" << std::endl;
    std::cout << code << std::endl;

    int authenticated = 0;
    std::cin >> authenticated;

    if(authenticated == code)
    {
        auto database_connection = myphpdatabase();
        database_connection.init_database();
        QSqlDatabase db = database_connection.get_database();
        QSqlQuery query;

        if(!database_connection.database_status())
        {
            database_connection.init_database();
        }

            if(database_connection.database_status())
            {
                query.prepare("INSERT INTO EtmDriverData(driverID,Firstname,Lastname,Username,Email,Password,UserAddress,StreetName,City,Postcode,PhoneNumber,DriverLicence,LorryDimensions,LorryWeight)"
                              "VALUES(:driverID,:firstName,:lastName,:usernameD,:userEmail,:passwordD,:userAddress,:streetName,:cityName,:postCode,:phoneNumber,:driverLicence,:dimensionsLorry,:weightLorry)"
                              );

                query.bindValue(0,driverID);
                query.bindValue(1,firstName);
                query.bindValue(2,lastName);
                query.bindValue(3,usernameD);
                query.bindValue(4,userEmail);
                query.bindValue(5,passwordD);
                query.bindValue(6,userAddress);
                query.bindValue(7,streetName);
                query.bindValue(8,cityName);
                query.bindValue(9,postCode);
                query.bindValue(10,phoneNumber);
                query.bindValue(11,driverLicence);
                query.bindValue(12,dimensionsLorry);
                query.bindValue(13,weightLorry);
                if(!query.exec())
                {
                    std::cout << "Did not executed"  << std::endl;
                }
            }
    }
    else
    {
        std::cout << "Not Connected to database" << std::endl;
    }
}

