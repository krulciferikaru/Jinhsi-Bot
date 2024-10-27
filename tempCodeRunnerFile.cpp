#include <iostream>
#include <string>
#include <unordered_map>
#include <stack>
#include <queue>

using namespace std;

const int MAX_EMPLOYEES = 100; 
string employeeIDs[MAX_EMPLOYEES]; 
int employeeCount = 0; 

struct Employee {
    string name;
    string id;
    string position;
    string contact_number;
    string address;
    float daily_rate;
    float tax;
    float sss;
    float pag_ibig;
    int no_days_work;
};

unordered_map<string, Employee> employeeMap;
stack<Employee> recentEmployees;
queue<Employee> employeeQueue;

float calculateSalary(const Employee& emp) {
    return emp.daily_rate * emp.no_days_work;
}

void deleteEmployee(const string& id);
void viewEmployeeByID(const string& id);
void editEmployee(const string& id);
void viewAllEmployees();

bool isValidNumber(const string& str) {
    if (str.length() > 11) {
        cout << "Invalid input. Please enter a number with 11 digits or less.\n";
        return false;
    }
    for (char ch : str) {
        if (!isdigit(ch) && ch != '.') {
            cout << "Invalid input. Please enter a valid number.\n";
            return false;
        }
    }
    return true;
}

float getValidNumberInput(const string& prompt) {
    string input;
    float number;
    bool valid = false;

    while (!valid) {
        cout << prompt;
        cin >> input;
        if (isValidNumber(input)) {
            number = stof(input);  
            valid = true;
        }
    }
    return number;
}

void displayEmployee(const Employee& emp) {
    float gross_pay = calculateSalary(emp);
    float total_deductions = emp.tax + emp.sss + emp.pag_ibig;
    float net_pay = gross_pay - total_deductions;

    cout << "\n====== EMPLOYEE DETAILS ======\n";
    cout << "Name: " << emp.name << endl;
    cout << "ID: " << emp.id << endl;
    cout << "Position: " << emp.position << endl;
    cout << "Contact Number: " << emp.contact_number << endl;
    cout << "Address: " << emp.address << endl;
    cout << "Daily Rate: Php " << emp.daily_rate << endl;
    cout << "Tax: Php " << emp.tax << endl;
    cout << "SSS: Php " << emp.sss << endl;
    cout << "Pag-IBIG: Php " << emp.pag_ibig << endl;
    cout << "Number of Days Worked: " << emp.no_days_work << endl;
    cout << "Gross Pay: Php " << gross_pay << endl;
    cout << "Total Deductions: Php " << total_deductions << endl;
    cout << "Net Pay: Php " << net_pay << endl;
    cout << "==============================\n";
}

void addEmployee() {
    Employee emp;
    cout << "\n===== ADD NEW EMPLOYEE =====\n";
    cout << "Enter Employee's Name: ";
    cin.ignore();
    getline(cin, emp.name);
    cout << "Enter the ID no.: ";
    getline(cin, emp.id);
    cout << "Enter Employee's Position: ";
    getline(cin, emp.position);
    cout << "Enter Contact Number: ";
    getline(cin, emp.contact_number);
    cout << "Enter Address: ";
    getline(cin, emp.address);

    emp.daily_rate = getValidNumberInput("Enter Daily Salary Rate (Php): ");

    do {
        emp.no_days_work = getValidNumberInput("Enter Number of Days Worked (1 to 30): ");
        if (emp.no_days_work < 1 || emp.no_days_work > 30) {
            cout << "Invalid number of days. Please enter a value between 1 and 30.\n";
        }
    } while (emp.no_days_work < 1 || emp.no_days_work > 30);

    emp.tax = getValidNumberInput("Enter Tax (Php): ");
    emp.sss = getValidNumberInput("Enter SSS Contribution (Php): ");
    emp.pag_ibig = getValidNumberInput("Enter Pag-IBIG Contribution (Php): ");

    employeeMap[emp.id] = emp;

    if (employeeCount < MAX_EMPLOYEES) {
        employeeIDs[employeeCount] = emp.id;
        employeeCount++;
    } else {
        cout << "Employee limit reached. Cannot add more employees.\n";
    }

    recentEmployees.push(emp);
    employeeQueue.push(emp);

    cout << "====================================" << endl;
    cout << "Employee added successfully!\n";
    cout << "====================================" << endl;
}

void deleteEmployee(const string& id) {
    auto it = employeeMap.find(id);
    if (it != employeeMap.end()) {
        
        Employee emp = it->second;
        stack<Employee> tempStack;
        while (!recentEmployees.empty()) {
            if (recentEmployees.top().id != id) {
                tempStack.push(recentEmployees.top());
            }
            recentEmployees.pop();
        }
        while (!tempStack.empty()) {
            recentEmployees.push(tempStack.top());
            tempStack.pop();
        }

        queue<Employee> tempQueue;
        while (!employeeQueue.empty()) {
            if (employeeQueue.front().id != id) {
                tempQueue.push(employeeQueue.front());
            }
            employeeQueue.pop();
        }
        employeeQueue = tempQueue;

        employeeMap.erase(it); 
        cout << "====================================" << endl;
        cout << "Employee with ID " << id << " deleted successfully!\n";
        cout << "====================================" << endl;
    } else {
        cout << "====================================" << endl;
        cout << "Employee with ID " << id << " not found.\n";
        cout << "====================================" << endl;
    }
}

void viewEmployeeByID(const string& id) {
    auto it = employeeMap.find(id);
    if (it != employeeMap.end()) {
        displayEmployee(it->second);
    } else {
        cout << "====================================" << endl;
        cout << "Employee with ID " << id << " not found.\n";
        cout << "====================================" << endl;
    }
}

void editEmployee(const string& id) {
    auto it = employeeMap.find(id);
    if (it != employeeMap.end()) {
        Employee& emp = it->second;
        cout << "\n===== EDIT EMPLOYEE =====\n";
        cout << "Enter new Employee's Name: ";
        cin.ignore();
        getline(cin, emp.name);
        cout << "Enter new I.D. no.: ";
        getline(cin, emp.id);
        cout << "Enter new Employee's Position: ";
        getline(cin, emp.position);
        cout << "Enter new Contact Number: ";
        getline(cin, emp.contact_number);
        cout << "Enter new Address: ";
        getline(cin, emp.address);
        
        emp.daily_rate = getValidNumberInput("Enter new Daily Salary Rate (Php): ");

        do {
            emp.no_days_work = getValidNumberInput("Enter new Number of Days Worked (1 to 30): ");
            if (emp.no_days_work < 1 || emp.no_days_work > 30) {
                cout << "Invalid number of days. Please enter a value between 1 and 30.\n";
            }
        } while (emp.no_days_work < 1 || emp.no_days_work > 30);

        emp.tax = getValidNumberInput("Enter new Tax (Php): ");
        emp.sss = getValidNumberInput("Enter new SSS Contribution (Php): ");
        emp.pag_ibig = getValidNumberInput("Enter new Pag-IBIG Contribution (Php): ");

        cout << "Employee details updated successfully!\n";
    } else {
        cout << "Employee with ID " << id << " not found.\n";
    }
}

void viewAllEmployees() {
    if (employeeMap.empty()) {
        cout << "No employees added yet.\n";
    } else {
        cout << "\n===== ALL EMPLOYEES =====\n";
        for (const auto& pair : employeeMap) {
            displayEmployee(pair.second);
        }
        cout << "=========================\n";
    }
}

int main() {
    cout << "\t===== EMPLOYEE'S PAYROLL SYSTEM =====\n\n";
    int choice;
    do {
        cout << "1. Add Employee\n";
        cout << "2. Delete Employee\n";
        cout << "3. View Employee by ID\n";
        cout << "4. Edit Employee\n";
        cout << "5. View All Employees\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice) {
            case 1:
                addEmployee();
                break;
            case 2: {
                string id;
                cout << "Enter the ID of the employee you want to delete: ";
                cin >> id;
                deleteEmployee(id);
                break;
            }
            case 3: {
                string id;
                cout << "Enter the ID of the employee you want to view: ";
                                cin >> id;
                viewEmployeeByID(id);
                break;
            }
            case 4: {
                string id;
                cout << "Enter the ID of the employee you want to edit: ";
                cin >> id;
                editEmployee(id);
                break;
            }
            case 5:
                viewAllEmployees();
                break;
            case 6:
                cout << "Exiting the system...\n";
                break;
            default:
                cout << "Invalid choice! Please enter a valid option.\n";
                break;
        }
        cout << endl;
    } while (choice != 6);

    return 0;
}