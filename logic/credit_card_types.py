from enum import Enum


class CreditCardType(Enum):
    VISA = "visa"
    MASTERCARD = "mastercard"
    AMEX = "amex"
    DISCOVER = "discover"
    JCB = "jcb"
    DINERS_CLUB = "dinersclub"
    UNIONPAY = "unionpay"
    MAESTRO = "maestro"