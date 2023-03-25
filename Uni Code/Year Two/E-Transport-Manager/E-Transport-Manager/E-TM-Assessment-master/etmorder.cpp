#include "etmorder.h"

unsigned long long etmorder::lastGeneratedID = 1000;

/* Initalise Order Object
etmorder::newOrder(string sourceLocation, string destinationLocation, double cargoWeight, double cargoSize, string cargoCondition) :
    source(sourceLocation), destination(destinationLocation), weight(cargoWeight), size(cargoSize), condition(cargoCondition)
{
    shippingRate = calculateShippingRate();
    companyComission = calculateCompanyComission();
}*/

/* Calculate Shipping Rate using Cargo Variables */
double etmorder::calculateShippingRate() {

    double conditionRate;

    if (!condition.empty()) {
        conditionRate = 1.1;
    }
    else {
        conditionRate = 1;
    }

    return round(weight * size * conditionRate * 100.0) / 100.0;
}

/* Calculate Company Comission as percentage of Shipping Rate */
double etmorder::calculateCompanyComission() {
    return round(shippingRate * 0.05 * 100.0) / 100.0;
}

/* Display Visual Receipt of Order */
void etmorder::generateReceipt() {
    cout << "\n\n--- ORDER RECEIPT ---\n\n";
    cout << "Order ID: #" << orderID;
    cout << "\n\nSource: " << source << "\nDestination: " << destination;
    cout << "\n\nShipping Rate: " << shippingRate << "\ne-TM Commission: " << companyComission << "\n\nTotal Price: " << shippingRate + companyComission;
}


void etmorder::OrderSys() {

    cout << "------ e-TM ORDER SYSTEM ------" << endl;
    cout << "=============================== \n\n" << endl;

    bool running = true;
    while (running) {

        string sourceLocation, destinationLocation, cargoCondition;
        double cargoWeight, cargoSize;

        cout << "Source Location: ";
        getline(std::cin, sourceLocation);

        cout << "Destination: ";
        getline(std::cin, destinationLocation);

        cout << "\nCargo Weight(kg): ";
        cin >> cargoWeight;

        cout << "Cargo Size(cm^3): ";
        cin >> cargoSize;

        string conditionRequired;
        cout << "Require special cargo condition maintenance? (y/n): ";
        cin >> conditionRequired;
        if (conditionRequired == "y") {
            cout << "Cargo Condition (10% Surcharge): ";
            cin >> cargoCondition;
        }

        //etmorder newOrder(sourceLocation, destinationLocation, cargoWeight, cargoSize, cargoCondition);
        //newOrder.generateReceipt();

        string again;
        cout << "\n\nWould you like to make another order? (y/n): ";
        cin >> again;
        if (again == "n") {
            running = false;
        }
    }
}
