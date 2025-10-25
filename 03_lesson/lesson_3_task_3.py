from address import Address
from mailing import Mailing

to_address = Address(751, "Питер", "Ленина", 1, 1)
from_address = Address(752, "Москва", "Ленина", 2, 2)

mailing = Mailing(from_address, to_address, cost=500, track="12")

print(mailing)
