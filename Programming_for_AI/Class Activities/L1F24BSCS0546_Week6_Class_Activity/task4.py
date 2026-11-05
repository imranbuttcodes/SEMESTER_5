from asyncio import sleep
from contextlib import AbstractAsyncContextManager
from abc import ABC, abstractmethod


class PaymentProvider:
    
    @abstractmethod
    def authorize():
        pass

    @abstractmethod

    def settle():
        pass


class CreditCardPay(PaymentProvider):
    def __init__(self, holder_name, card_number, exp_date, fee):
        self.holder_name = holder_name
        self.fee = fee
        self.card_number = card_number
        self.exp_date = exp_date


class StripePay(PaymentProvider):

    def authorize(self, api_key):

        self.fee -= (self.fee * 0.025)
    
    
