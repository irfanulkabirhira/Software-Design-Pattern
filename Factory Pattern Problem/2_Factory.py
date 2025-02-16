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

# Step 3: Implement the Factory Method without using lists or dictionaries
class PaymentFactory:
    @staticmethod
    def get_payment_method(method):
        if method == "credit_card":
            return CreditCardPayment()
        elif method == "paypal":
            return PayPalPayment()
        elif method == "bitcoin":
            return BitcoinPayment()
        else:
            raise ValueError("Invalid payment method")

    @staticmethod
    def remove_payment_method(method):
        raise NotImplementedError("Remove method functionality not supported without list or dictionary")

# Step 4: Client Code
if __name__ == "__main__":
    # Example of adding a payment method
    payment_method = input("Enter payment method (credit_card/paypal/bitcoin): ").strip().lower()

    try:
        payment = PaymentFactory.get_payment_method(payment_method)
        print(payment.process_payment(100))  # Example payment of $100
    except ValueError as e:
        print(e)
