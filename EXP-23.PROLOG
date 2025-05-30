parent(john, mary).
parent(john, tom).
parent(mary, alice).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
Query:parent(john,mary).
