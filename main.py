# This is a simulation for bank account 
# using Python Object Oriented Programming.
# It will allows user to withdraw and place deposit.
# Beside, it also allows user to create new account.
# For normal user, not for admin usage.


# Important:
# Use xampp mysql for this program, for database.


import os
import bcrypt
import random
from datetime import datetime
import sqlite3
import smtplib
import pyotp
import qrcode


class BankAccount:
    def __init__(self, name, age, identity_number, address, initial_deposit, email, password):
        self._name = name
        self._age = age
        self._identity_number = identity_number
        self._address = address
        self._balance = initial_deposit
        self._email = email
        self._password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.minimum_deposit = 50
        self._account_no = random.randint(1000000000,9999999999)
        self.amount = 0
        self.failed_attempts = 0
        self.last_failed_attempt_time = None

        self.welcome_page()
        self.save_account_details()

    def authenticate(self, password):
        if self.failed_attempts >= 3 and self.last_failed_attempt_time is not None:
            elapsed_time = datetime.now() - self.last_failed_attempt_time
            if elapsed_time < datetime.timedelta(minutes=5):
                remaining_time = datetime.timedelta(minutes=5) - elapsed_time
                # raise Exception(f"Account locked due to too many failed attempts. Please try again after {remaining_time.seconds // 60} minutes.")
                print(f"Account locked due to too many failed attempts. Please try again after {remaining_time.seconds // 60} minutes.")
            else:
                self.failed_attempts = 0

        if bcrypt.checkpw(password.encode('utf-8'), self._password):
            self.failed_attempts = 0
            self.last_failed_attempt_time = None
            return True
        else:
            self.failed_attempts += 1
            self.last_failed_attempt_time = datetime.now()
            if self.failed_attempts >= 3:
                # raise Exception("Too many failed attempts. Account locked for 5 minutes.")
                print("Too many failed attempts. Account locked for 5 minutes.")
                self.lock_account()
            else:
                # raise Exception("Incorrect password. Please try again.")
                print("Incorrect password. Please try again.")

    def send_lockout_email(self):
        # create an SMTP server object
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # login with your email account and password
        server.login('example@gmail.com', 'gmail_app_passwore')
        # create the email message
        message = f"""Subject: Account Lockout Notification

        Dear {self.get_name()},

        We are writing to inform you that your Bank account has been locked due to multiple failed login attempts.

        Please contact our customer support team to unlock your account.

        Thank you for choosing our bank.

        Best regards,
        The Bank Team

        """
        # send the email
        server.sendmail('example@gmail.com', self._email, message)
        # close the SMTP server
        server.quit()

    def lock_account(self):
        self.locked = True
        self.last_lock_time = datetime.now()
        self.send_lockout_email()
        print("Your account has been locked due to multiple failed login attempts. Please contact our customer support team to unlock your account.")
        
    def save_account_details(self):
        conn = sqlite3.connect('account.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO accounts (account_number, name, balance, pin) VALUES (?, ?, ?, ?)', (self.get_account_number(), self.get_name(), self.get_balance(), self.get_password()))

        # commit the changes to the database
        conn.commit()

        # close the cursor and the connection
        cur.close()
        conn.close()

    # Getter functions
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_identity_number(self):
        return self._identity_number
    
    def get_address(self):
        return self._address
    
    def get_balance(self):
        return self._balance
    
    def get_password(self):
        return self._password
    
    def get_account_number(self):
        return self._account_no

    # Setter functions
    def set_name(self, name):
        self._name = name
    
    def set_age(self, age):
        self._age = age
    
    def set_identity_number(self, identity_number):
        self._identity_number = identity_number
    
    def set_address(self, address):
        self._address = address
    
    def set_balance(self, balance):
        self._balance = balance
    
    def set_password(self, new_password):
        self._password = new_password

    # make a deposit, for own account and other account
    def make_deposit(self):
        authenticated = False
        while not authenticated:
            pin_entered = str(input("PIN: "))
            authenticated = self.authenticate(pin_entered)
        
        amount = int(input("How much would you like to deposit? "))
        self._balance += amount
        self.account_inquiry()


    # make a withdraw, for a specific amount
    def withdraw(self):
        authenticated = False
        while not authenticated:
            pin_entered = str(input("PIN: "))
            authenticated = self.authenticate(pin_entered)
            if not authenticated:
                print("Incorrect PIN. Please try again.")
        
        amount = int(input("How much would you like to withdraw? "))
        if amount > self.get_balance():
                raise ValueError("Insufficient balance in account.")
        self._balance -= amount
        self.account_inquiry()

    # account inquiry
    def account_inquiry(self):
        print("\n")
        print("Receipt :")
        # datetime object containing current date and time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(dt_string)
        print("Name \t\t: ", self.get_name())
        print("Identity Number : ", self.get_identity_number())
        print("Account Number \t: ", self.get_account_number())
        print("Current account balance : " + str(self.get_balance()))
        print("\n")

    # change pin
    def change_pin(self, new_password):
        print("\n")
        print("Old pin : ", self.get_password())
        self.set_pin(new_password)
        print("Pin changed successfully.")
        print("New pin", self.get_password())
        print("\n")

    def welcome_page(self):
        print("Welcome to your bank account!")
        while True:
            print("What would you like to do?")
            print("1. Make a deposit")
            print("2. Withdraw money")
            print("3. Check account balance")
            print("4. Change PIN")
            print("5. Quit")
            choice = input("Enter the number of your choice: ")
            if choice == "1":
                self.make_deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.account_inquiry()
            elif choice == "4":
                new_pin = input("Enter new PIN: ")
                self.change_pin(new_pin)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    
if __name__ == "__main__":
    person1 = BankAccount("Lee Ah Kau", 18, "011225018888", "Malaysia.", 1000, "leeahkau@gmail.com", "000000")
