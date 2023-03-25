#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <time.h>

using namespace std;

int option;
int fundsToWithdraw;
int additionalTransaction;
int deposit;
int exitNow;
int inpin;
int inAccountNumber;
int choice;


float balance = 1000;

class Login {
public:

    string AccountNumber, Pin;
    Login()
    {
        AccountNumber = "\0";
        Pin = "\0";
    };
    bool IsLogIn();
};


bool Login::IsLogIn()
{
    string ch_AccountNumber = "47789521", ch_Pin = "4978";
    cout << "Welcome to the Richards ATM Banking System" << endl;
    cout << "1. Login Account" << endl;
    cout << "2. Create Account" << endl;
    cin >> choice;

    if (choice == 1) {
        cout << "Enter your account number: ";
        cin >> AccountNumber;
        cout << "Enter your pin: ";
        cin >> Pin;

        if (AccountNumber == ch_AccountNumber && Pin == ch_Pin)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
   
    else if (choice == 2) {

        ofstream afile("accountdetails.txt");
        afile.open("accountdetails.txt");
        
        
            srand((unsigned)time(0));
            int randomAccountNumber;
            for (int index = 0; index < 1; index++) {
                randomAccountNumber = (rand() % 99999999) + 10000000;
                cout << "Your Account Number is: " << randomAccountNumber << endl;
            }
            afile << randomAccountNumber;

            int randomPinNumber;
            for (int index = 0; index < 1; index++) {
                randomPinNumber = (rand() % 9999) + 1000;
                cout << "Your Pin is: " << randomPinNumber << endl;
            }
            afile << randomPinNumber;
            afile.close();
    }
}


void print_menu(void) {
    cout << "Welcome to the Richards ATM Banking System" << endl;
    cout << "1. Withdrawal Funds" << endl;
    cout << "2. Check Balance" << endl;
    cout << "3. Deposit Funds" << endl;
    cout << "4. Exit" << endl;
    cin >> option;
}

void menu() {
    do {
        switch (option) {

        case 1:
            cout << "Enter amount to withdraw: ";
            cin >> fundsToWithdraw;

            if (fundsToWithdraw > balance) {
                cout << "Insuffient Funds";
                cout << "\n\n Do you want another transaction?\nPress 1 to continue" << endl;
                cin >> additionalTransaction;
            }
            else {
                balance = balance - fundsToWithdraw;
                cout << "Withdraw " << fundsToWithdraw << "Your balance after withdrawal: " << balance;
                cout << "\n\n Do you want another transaction?\nPress 1 to continue" << endl;
                cin >> additionalTransaction;
            }
            break;
        case 2:
            cout << "Your Current Balance: " << balance << endl;
            cout << "\n\n Do you want another transaction?\nPress 1 to continue" << endl;
            cin >> additionalTransaction;
            break;

        case 3:
            balance = balance + deposit;
            cout << "Enter the amount to deposit: ";
            cin >> deposit;

            cout << "\nBalance after deposit: " << balance << endl;
            cout << "\n\n Do you want another transaction?\nPress 1 to continue" << endl;
            cin >> additionalTransaction;
            break;
        case 4:
            return;
        }


        if (additionalTransaction == 1) {
            print_menu();
        }
    } while (option < '1' || option>'4');
}
int main()
{
    Login l1;
    bool status = l1.IsLogIn();
    if (!status)
    {
        cout << "\nIncorrect Account Details\n";
        return 1;
    }
    else
    {
        cout << "\nAccount Details Correct\n";
    }

    print_menu();
    menu();
}

