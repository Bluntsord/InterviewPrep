import requests

base_url = 'http://127.0.0.1:5000'

def main():
    while True:
        print('Welcome to AwesomeGIC Bank! What would you like to do?')
        print('[D]eposit')
        print('[W]ithdraw')
        print('[P]rint statement')
        print('[Q]uit')

        choice = input().lower()

        if choice == 'd':
            amount = float(input('Please enter the amount to deposit: '))
            response = requests.post(f'{base_url}/deposit', json={'amount': amount}).json()
            print(f"Thank you. ${response['balance']:.2f} has been deposited to your account.")
        elif choice == 'w':
            amount = float(input('Please enter the amount to withdraw: '))
            response = requests.post(f'{base_url}/withdraw', json={'amount': amount}).json()
            print(f"Thank you. ${response['balance']:.2f} has been withdrawn.")
        elif choice == 'p':
            response = requests.get(f'{base_url}/statement').json()
            print("Date                  | Amount  | Balance")
            balance = 0
            for t in response:
                balance += t['amount']
                print(f"{t['date']} | {t['amount']:7.2f} | {balance:7.2f}")
        elif choice == 'q':
            print("Thank you for banking with AwesomeGIC Bank.")
            print("Have a nice day!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
