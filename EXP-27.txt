edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).

bestfirst(a, d, [a,b,d]).
QUERY:bestfirst(a, d, Path).
