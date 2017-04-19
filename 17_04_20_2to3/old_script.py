print "Starting script"

a = 2
b = 3

print "a = %d, b = %d" % (a, b)
print "a/b = %.2f" % (a / b,)

s = "This is a \"normal\" string"
us = u"This is a unicode string"

print s, "of type", type(s)
print us, "of type", type(us)

irange = xrange(5)
print "iterator type from xrange:", type(irange)

squares = map(lambda x: x ** 2, range(1, 6))
print "squares:", squares
