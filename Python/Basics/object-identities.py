import datetime as dt
#Use 'is' comparison for identity comparison
a = range(10)
b = range(10)
#Compare values
print(a==b)
#Compare identities
print(a is b)
#Compare identities
print(id(a)==id(b))
#Compare identity with assigned object
c = a
print(a is c)