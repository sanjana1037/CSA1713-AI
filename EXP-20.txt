% Facts about planets
planet(mercury, 0.39, 4879, rocky).
planet(venus, 0.72, 12104, rocky).
planet(earth, 1.00, 12756, rocky).
planet(mars, 1.52, 6792, rocky).
planet(jupiter, 5.20, 142984, gas_giant).
planet(saturn, 9.58, 120536, gas_giant).
planet(uranus, 19.18, 51118, ice_giant).
planet(neptune, 30.07, 49528, ice_giant).

% Rule to find nearby planets within a distance threshold
nearby_planets(Planet1, Planet2, Threshold) :-
    planet(Planet1, Distance1, _, _),
    planet(Planet2, Distance2, _, _),
    Planet1 \= Planet2,
    Diff is abs(Distance1 - Distance2),
    Diff =< Threshold.

% Rule to find planets by type
planet_type(Name, Type) :-
    planet(Name, _, _, Type).

% Rule to find large planets (diameter > threshold)
large_planet(Name) :-
    planet(Name, _, Diameter, _),
    Diameter > 50000.
