#include <QCoreApplication>
#include <etmcargo.h>
#include <etmdriver.h>
#include <etmorder.h>
#include <iostream>
using namespace std;

//prints menu for cargo owner giving the option to either create account or login
void print_menuC(void) {
    int optionC;
    etmcargo obj;
    etmorder obj2;

    cout << "==================================" << endl;
    cout << "E-Transport MarketPlace Interface " << endl;
    cout << "==================================" << endl;
    cout << "1:Create New Account" << endl;
    cout << "2:Login To Account" << endl;
    cout << "3:Exit" << endl;
    cin >> optionC;

    switch (optionC) {
    case 1:
        cout << "Create New Account" << endl;
        obj.newCargoO();
        obj2.OrderSys();
        break;

    case 2:
        cout << "Login To Account" << endl;
        obj.signinCargo();
        obj2.OrderSys();
        break;

    case 3:
        break;

    default:
        cout << "Choose one of the available options displayed in the menu." << endl;

    }
}

//prints menu for cargo driver giving the option to either create account or login
void print_menuD(void) {
    int optionD;
    etmdriver obj1;

    cout << "==================================" << endl;
    cout << "E-Transport MarketPlace Interface " << endl;
    cout << "==================================" << endl;
    cout << "1:Create New Account" << endl;
    cout << "2:Login To Account" << endl;
    cout << "3:Exit" << endl;
    cin >> optionD;

    switch (optionD) {
    case 1:
        cout << "Create New Account" << endl;
        obj1.newDriver();
        break;

    case 2:
        cout << "Login To Account" << endl;
        obj1.signinDriver();
        break;

    case 3:
        break;

    default:
        cout << "Choose one of the available options displayed in the menu." << endl;

    }
}

//prints menu for cargo transport comp giving the option to either create account or login
void print_menuTC(void) {
    int optionTC;
    etmtransportc obj3;


    cout << "==================================" << endl;
    cout << "E-Transport MarketPlace Interface " << endl;
    cout << "==================================" << endl;
    cout << "1:Create New Account" << endl;
    cout << "2:Login To Account" << endl;
    cout << "3:Exit" << endl;
    cin >> optionTC;

    switch (optionTC) {
    case 1:
        cout << "Create New Account" << endl;
        obj3.newTransportC();
        break;

    case 2:
        cout << "Login To Account" << endl;
        obj3.signinTransport();
        break;

    case 3:
        break;

    default:
        cout << "Choose one of the available options displayed in the menu." << endl;

    }
}

int main()
{   //Main menu where the user picks type
    bool checkuchoice = false;
    char uchoice;
    while (checkuchoice == false)
    {
        cout << "Welcome to E-Transport Marketplace" << endl;
        cout << "==================================" << endl;
        cout << "Pick your user type!\n" << endl;
        cout << "1:Cargo Owner" << endl;
        cout << "2:Driver" << endl;
        cout << "3:Transport Company" << endl;
        cout << "\n" << endl;
        cin >> uchoice;

        switch (uchoice)
        {
        case '1':
            cout << "e-TM Cargo Owner" << endl;
            print_menuC();
            checkuchoice = true;
            break;

        case '2':
            cout << "e-TM Driver" << endl;
            print_menuD();
            checkuchoice = true;
            break;

        case '3':
            cout << "e-TM Transport Company" << endl;
            //print_menuTC();
            checkuchoice = true;
            break;

        default:
            cout << "Please enter a valid input to proceed." << endl;
            checkuchoice = false;

        };

    };


};
