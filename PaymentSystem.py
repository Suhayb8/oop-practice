from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing €{amount} via Credit Card.")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing €{amount}via PayPal.")


credit = CreditCardPayment()
paypal = PayPalPayment()
credit.process_payment(250)
paypal.process_payment(140)

