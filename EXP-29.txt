fact(a).
rule(b) :- fact(a).
rule(c) :- rule(b).
QUERY: rule(b).
