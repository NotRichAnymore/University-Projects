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


double balance = 1000;
//Class contains the login details to be used in the int main//
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
    //A string is set to manage the details of the login infomation//
    string ch_AccountNumber = "47789521", ch_Pin = "4978";
    cout << "Welcome to the Richards ATM Banking System" << endl;
    cout << "1. Login Account" << endl;
    cout << "2. Create Account" << endl;
    cin >> choice;
    //Option choice to login to account//
    if (choice == 1) {
        cout << "Enter your account number: ";
        cin >> AccountNumber;
        cout << "Enter your pin: ";
        cin >> Pin;
        //Verify account details//
        if (AccountNumber == ch_AccountNumber && Pin == ch_Pin)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    //Create new account option//  
    else if (choice == 2) {
        //Opens the file to write data to//
        ofstream afile("accountdetails.txt");
        afile.open("accountdetails.txt", ios::out | ios::in);

        // Randomly creates an account number and pin for the new account//
        srand((unsigned)time(0));
        int randomAccountNumber;
        for (int index = 0; index < 1; index++) {
            randomAccountNumber = (rand() % 99999999) + 10000000;
            cout << "Your Account Number is: " << randomAccountNumber << endl;
           /* cin.getline(randomAccountNumber, sizeof(randomAccountNumber));*/
        }
        

        int randomPinNumber;
        for (int index = 0; index < 1; index++) {
            randomPinNumber = (rand() % 9999) + 1000;
            cout << "Your Pin is: " << randomPinNumber << endl;
        }
        //Saves account number and pin to file and closes it//
       /* cin.getline(randomPinNumber, sizeof(randomAccountNumber));*/
        afile.close();
    }
}

//Creates Menu to select atm option//
void print_menu(void) {
    cout << "Welcome to the Richards ATM Banking System" << endl;
    cout << "1. Withdrawal Funds" << endl;
    cout << "2. Check Balance" << endl;
    cout << "3. Deposit Funds" << endl;
    cout << "4. Exit" << endl;
    cin >> option;
}
//Controls the main functions of the atm using switch cases//
void menu() {
    do {
        switch (option) {

        case 1:
            cout << "Enter amount to withdraw: ";
            cin >> fundsToWithdraw;

            if (fundsToWithdraw > balance) {
                cout << "Insuffient Funds";
                cout << "\n\n Do you want another transaction?\nPress 1 to continue, Press 2 to exit" << endl;
                cin >> additionalTransaction;
            }
            else {
                balance = balance - fundsToWithdraw;
                cout << "Withdraw " << fundsToWithdraw << "Your balance after withdrawal: " << balance;
                cout << "\n\n Do you want another transaction?\nPress 1 to continue, Press 2 to exit" << endl;
                cin >> additionalTransaction;
            }
            break;
        case 2:
            cout << "Your Current Balance: " << balance << endl;
            cout << "\n\n Do you want another transaction?\nPress 1 to continue, Press 2 to exit "<< endl;
                cin >> additionalTransaction;
            break;

        case 3:
            balance = balance + deposit;
            cout << "Enter the amount to deposit: ";
            cin >> deposit;

            cout << "\nBalance after deposit: " << balance << endl;
            cout << "\n\n Do you want another transaction?\nPress 1 to continue, Press 2 to exit" << endl;
            cin >> additionalTransaction;
            break;
        case 4:
            return;
        }

        //Gives the user the option to return to menu or exit//
        if (additionalTransaction == 1) {
            print_menu();
        }
        else if (additionalTransaction == 2) {
            return;
        }

    } while (option < '1' || option>'4');
}
//Runs the login details and verifys them as well as running the 2 menu functions//
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
        cout << "\nAccount Details Correct\n\n";
    }

    print_menu();
    menu();
}

