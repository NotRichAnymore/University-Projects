#include "etmtransportc.h"

//user signs into respective account
void etmtransportc::signinTransport()
{
    //initially a connection with the database needs to be established
    //allows inputs for QStrings
    QTextStream input(stdin);
    QString usernameLogin;

    //takes username to check if it is already present in the database
    std::cout << "Enter your username: " << std::endl;
    input >> usernameLogin;

    //connection to the database
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
        qry.prepare("SELECT usernameC FROM EtmCargoOData WHERE usernameC = :usernameC");
        qry.bindValue(":usernameC",usernameLogin);


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
                qryPassword.prepare("SELECT passwordC FROM EtmCargoOData WHERE passwordC = :passwordC");
                qryPassword.bindValue(":passwordC",userPassword);
                bool passwordFound = false;
                if(qryPassword.exec())
                {
                    passwordFound = qryPassword.next();
                    if(passwordFound == true)
                    {
                        QTextStream output(stdout);

                        output << "Welcome to E-TM,"<< usernameLogin << endl; //need to follow up with funcs here

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

void etmtransportc::newTransportC() {

    QTextStream input(stdin); // this will allow input for Qstrings

    transportCID = 0; // have set to auto increment in the database.


    std::cout << "Enter your first name: " << std::endl;
    input >> firstName;
    std::cout << "Enter your last name: "<< std::endl;
    input >> lastName;
    std::cout << "Enter a username: "<< std::endl;
    input >> usernameC;
    std::cout << "Enter your email: " << std::endl;
    input >> userEmail;
    std::cout << "Enter a password: "<< std::endl;
    input >> passwordC;
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

    std::cout << "Enter the verification code" << std::endl;
    std::cout << code << std::endl;
    int authenticated = 0;
    std::cin >> authenticated;

    if(authenticated == code)
    {
        //generating a verification code and if matches then data is saved on to the database
        auto database_connection = myphpdatabase();
        database_connection.init_database();
        QSqlDatabase db = database_connection.get_database();
        QSqlQuery query;

        if(!database_connection.database_status())
        {
            database_connection.init_database();
        }


//try and catch to insert data if not display not connected
        try {
            if(database_connection.database_status())
            {
                query.prepare("INSERT INTO EtmCargoOData (transportCID,FirstName,LastName,Username,Email,Password,UserAddress,StreetName,City,Postcode,PhoneNumber)"
                              "VALUES(:transportCID,:firstName,:lastName,:usernameC,:userEmail,:passwordC,:userAddress,:streetName,:cityName,:postCode,:phoneNumber)");

                query.bindValue(0,transportCID);
                query.bindValue(1,firstName);
                query.bindValue(2,lastName);
                query.bindValue(3,usernameC);
                query.bindValue(4,userEmail);
                query.bindValue(5,passwordC);
                query.bindValue(6,userAddress);
                query.bindValue(7,streetName);
                query.bindValue(8,cityName);
                query.bindValue(9,postCode);
                query.bindValue(10,phoneNumber);
                query.exec();
            }
        } catch(const std::exception& e)
        {
            std::cout << e.what();
        }

    }
    else
    {
        std::cout << "Not Connected to database" << std::endl;
    }
}

