# Bank Account Simulation

This is a simulation of a bank account using Python Object-Oriented Programming (OOP). It allows users to perform various actions such as making deposits, withdrawing money, checking account balances, changing PINs, and more. This simulation is intended for normal users and is not designed for administrative usage.

## Features

1. **Account Creation**: Users can create bank accounts by providing their personal details, initial deposit, and setting a password.

2. **Deposit**: Users can make deposits into their accounts.

3. **Withdrawal**: Users can withdraw money from their accounts, provided they have sufficient balance.

4. **Account Inquiry**: Users can check their account balance and receive a receipt with relevant information.

5. **PIN Change**: Users can change their account PIN for added security.

## Prerequisites

Before running the simulation, make sure you have Python installed on your system. This simulation uses Python's built-in libraries and does not require any external dependencies.

## How to Run

To run the bank account simulation on your local machine, follow these steps:

1. **Download or Clone Repository**: Start by downloading or cloning this repository to your computer. You can use the following command if you have Git installed:

   ```bash
   git clone https://github.com/shisian512/Bank-Account-Simulation.git
   ```

2. Open a terminal or command prompt and navigate to the project directory.

   ```bash
   cd /Bank-Account-Simulation
   ```
   
4. Run the following command to execute the simulation:

   ```bash
   python main.py
   ```

5. Follow the on-screen instructions to interact with the bank account simulation.

## Usage

1. **Creating an Account**: When you run the simulation, it will prompt you to create a bank account. Provide the required information such as name, age, identity number, address, initial deposit, email, and password.

2. **Menu Options**: After creating an account, you'll be presented with a menu containing various options:
   - **Make a Deposit**: Deposit money into your account.
   - **Withdraw Money**: Withdraw money from your account.
   - **Check Account Balance**: View your account balance and receive a receipt.
   - **Change PIN**: Change your account PIN for security.
   - **Quit**: Exit the simulation.

3. **Interacting with the Simulation**: Choose an option by entering the corresponding number. Follow the prompts to perform the selected action.

## Notes

- The simulation uses Object-Oriented Programming (OOP) principles to model the bank account and its functionalities.
- Passwords are securely hashed using the bcrypt library to ensure data security.
- Failed login attempts are tracked, and the account can be temporarily locked after multiple failed attempts.
- Account information is stored in an SQLite database for persistent storage.

## Disclaimer

This simulation is designed for educational purposes and is not intended for actual financial transactions. The security measures implemented in this simulation may not reflect real-world banking standards. Always use secure and tested libraries for handling sensitive information in real applications.

## Author

This simulation was created by Shi Sian as a programming exercise.

Feel free to modify, extend, or improve upon this simulation as you see fit!
