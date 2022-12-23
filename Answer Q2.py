from logic import*

#(1) Maria reads logic programming book by author peter lucas.
#Answer: reads(Maria,logicprogrammingbook):- author(peter_lucas).
Maria = Symbol("Maria")
peter_lucas = Symbol("peter lucas")
read = Symbol("read(Maria,logic programming book)")
author = Symbol("author(peter_lucas)")
knowledge1=And(Implication(read,author))
print(knowledge1.formula())

#(2) Anyone likes shopping if she is a girl.
#Answer: likes(Anyone,shopping):- anyone(girl)
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
likes = Symbol("likes(x,shopping)")
knowledge2=And(Implication(is_girl,likes))
print(knowledge2.formula())

#(3) Who likes shopping?
#Answer: ?-likes(X,shopping)
who = Symbol("? likes(x,shopping)")
knowledge3=And(who)
print(knowledge3.formula())

#(4) kirke hates any city if it is big and crowdy.
#Answer: hates(kirke):-city(big,crowdy).
city = Symbol("city(x,big,crowdy)")
hates = Symbol("hates(kirke,x)")
knowledge4=And(Implication(city,hates))
print(knowledge4.formula())
