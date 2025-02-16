'''
An online shopping platform allows customers to pay using different payment methods (Credit Card, PayPal, Bitcoin). Implement a Factory Method to return the appropriate payment processor based on the user's choice.

'''
from abc import ABC, abstractmethod

# Step 1: Define an abstract class for Payment
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Step 2: Implement concrete classes for each payment method
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing Credit Card payment of ${amount}"

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        return f"Processing Bitcoin payment of ${amount}"

# Step 3: Implement the Factory Method with add and remove functionality
class PaymentFactory:
    available_methods = {}

    @staticmethod
    def get_payment_method(method):
        if method in PaymentFactory.available_methods:
            return PaymentFactory.available_methods[method]()
        else:
            raise ValueError("Invalid payment method")

    @staticmethod
    def add_payment_method(method_name, method_class):
        PaymentFactory.available_methods[method_name] = method_class

    @staticmethod
    def remove_payment_method(method_name):
        if method_name in PaymentFactory.available_methods:
            del PaymentFactory.available_methods[method_name]
        else:
            raise ValueError(f"Payment method {method_name} not found")

# Step 4: Client Code
if __name__ == "__main__":
    # Add payment methods
    PaymentFactory.add_payment_method("credit_card", CreditCardPayment)
    PaymentFactory.add_payment_method("paypal", PayPalPayment)
    PaymentFactory.add_payment_method("bitcoin", BitcoinPayment)

    # Try removing a payment method
    try:
        PaymentFactory.remove_payment_method("bitcoin")
        print("Bitcoin payment method removed.")
    except ValueError as e:
        print(e)

    # Try selecting a payment method after removal
    payment_method = input("Enter payment method (credit_card/paypal/bitcoin): ").strip().lower()
    try:
        payment = PaymentFactory.get_payment_method(payment_method)
        print(payment.process_payment(100))  # Example payment of $100
    except ValueError as e:
        print(e)
