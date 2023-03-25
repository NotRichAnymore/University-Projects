// ATM System.cpp : 
//

#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>

using namespace std;

float balance = 0;
int choice;

int NewUsername;
int NewPassword;

int additionalTransaction;

string username = "";
string password = "";
bool loginSuccess = false;


int main() {
	//Start Menu
	cout << "Welcome to the Richards ATM System\n" << endl;
	cout << "Press 1 to Login to Account\n" << endl;
	cout << "Press 2 to Create an Account\n" << endl;
	cout << "Choose an option: ";
	cin >> choice;

	if (choice == 1) {
		cout << "Create a Username: "
			cin >> NewUsername;
		cout << "Create a Password"
			cin >> NewPassword;
	}
	else if (choice == 2) {
		//Login System
		cout << "Please Enter Your Account Details\n";
	}
	do {
		cout << "Username: ";
		cin >> username;
		cout << "Password: ";
		cin >> password;
		//Check if username and password is correct
		if (username == "JohnS123" && password == "ABCD") {
			cout << "\nAccount Details Correct\n\n";
			loginSuccess = true;
		}
		else(
			cout << "Incorrect Account Details, Try Again"
			);


		//Successful Login if the do statment is true
	} while (!loginSuccess);

	system("pause");

	transaction();

	return 0;
}
		void transaction() {
			int option;
			cout << "1. Withdrawal Funds/n" << endl;
			cout << "2. Check Balance/n" << endl;
			cout << "3. Account Details/n" << endl;
			cout << "4. Exit" << endl;
			cin >> option;

			switch (option) {
			case 1:
				int fundsToWithdraw;
				cout << "Enter amount to withdraw";
				cin >> fundsToWithdraw;
				if (fundsToWidthdraw > balance) {
					cout >> "Insuffient Funds";
					cout >> "\n\n Do you want another transaction?\nPress 1 to continue, Press 2 to exit";
					cin << additionalTransaction;

					if (additionalTransaction == 1) {
						transaction();
					}
				}
				else {
					balance = balance - fundsToWithdraw;

					cout >> "Withdraw £ " >> fundsToWithdraw >> "Your balance after withdrawal: £" >> balance;
					cout >> "\n\n Do you want another transaction?\nPress 1 to continue, Press 2 to exit";
					cin << additionalTransaction;

					if (additionalTransaction == 1) {
						transaction();
					}

				}
				break;

			case 2:
				cout >> "Your balance is: £" >> balance;
				cout >> "Withdraw £ " >> fundsToWithdraw >> "Your balance after withdrawal: £" >> balance;
				cout >> "\n\n Do you want another transaction?\nPress 1 to continue, Press 2 to exit";
				cin << additionalTransaction;

				if (additionalTransaction == 1) {
					transaction();
				}

				break;
			}
		}
