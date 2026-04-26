
# Improting an Entire Module
import cake

# Importing Specific Functions 
from cake import make_cake, print_msg

# Using as to Give a Function an Alias
from cake import make_cheesecake as mk

# Giving the module an alias
import cake as ck

# Improting All Funcs in a Module (using *) --> too risky 
# for the modules you didn't write
from cake import *

cake.make_cake(9,'cream cheese','strawberry','apple')
ck.make_cake(10, 'cheese','something else')

make_cake(6,*['Ice Cream','caramel'])

print_msg('hello')

cheese_cake = mk(size=8, color='green', filling='strawberry')
print(cheese_cake)




