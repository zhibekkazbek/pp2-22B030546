"""
Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
"""

a = 5
print(type(a))

"""
x = "Hello World"	                           str	
x = 20	                                       int	
x = 20.5	                                   float	
x = 1j	                                       complex	
x = ["apple", "banana", "cherry"]	           list	
x = ("apple", "banana", "cherry")	           tuple	
x = range(6)	                               range	
x = {"name" : "John", "age" : 36}	           dict	
x = {"apple", "banana", "cherry"}	           set	
x = frozenset({"apple", "banana", "cherry"})   frozenset	
x = True	                                   bool	
x = b"Hello"	                               bytes	
x = bytearray(5)	                           bytearray	
x = memoryview(bytes(5))	                   memoryview	
x = None	                                   NoneType
"""

x = "Hello World"
print(type(x))

y = 20.5
print(type(y))

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))