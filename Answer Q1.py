from logic import*

#(1) color(carrots, orange).
#Answerwer: carrots color is orange.
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge1=And(Implication(carrots,orange))
print(knowledge1.formula())

#(2) likes(Person, carrots):-vegetarian(Person).
#Answer: person likes carrots if person is vegetarian.
person = Symbol("person")
vegetarian = Symbol("vegetarian(person)")
like = Symbol("like")
personLikeCarrots = Symbol("like(person,carrots)")
knowledge2=And(Implication(personLikeCarrots,vegetarian))
print(knowledge2.formula())

#(3) pass(Student) study_hard(Student).
#Answer: Student pass if student study hard
passExam = Symbol("pass(student)")
study_hard = Symbol("study_hard(Student)")
knowledge3=And(Implication(passExam,study_hard))
print(knowledge3.formula())

#(4) ?- pass(Who).
#Answer: who will pass?
Pass = Symbol("?- pass(Who)")
knowledge4=And(Pass)
print(knowledge4.formula())

#(5) ?- teaches(professor, Course).
#Answer: Which course professor teaches?
teaches = Symbol("teaches(professor, Course)")
knowledge5=And(teaches)
print(knowledge5.formula())

#(6) enemies(X, Y) hates(X, Y), fights(X, Y).
#Answer: If X & Y are enemies then X hates Y and X fights Y.
enemies = Symbol("enemies(X, Y)")
hates = Symbol("hates(X, Y)")
fights = Symbol("fights(X, Y)")
knowledge6=And(Implication(enemies,And(hates,fights)))
print(knowledge6.formula())