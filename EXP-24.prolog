% Define diseasesAdd commentMore actions
disease(diabetes).
disease(hypertension).
disease(anemia).
disease(obesity).
disease(cardiac).

% Recommended foods for each disease
recommended_food(diabetes, oats).
recommended_food(diabetes, green_vegetables).
recommended_food(diabetes, brown_rice).
recommended_food(diabetes, lentils).
recommended_food(diabetes, nuts).

recommended_food(hypertension, banana).
recommended_food(hypertension, beetroot).
recommended_food(hypertension, low_fat_yogurt).
recommended_food(hypertension, oatmeal).
recommended_food(hypertension, spinach).

recommended_food(anemia, red_meat).
recommended_food(anemia, spinach).
recommended_food(anemia, beans).
recommended_food(anemia, tofu).
recommended_food(anemia, eggs).

recommended_food(obesity, cucumber).
recommended_food(obesity, apple).
recommended_food(obesity, salad).
recommended_food(obesity, boiled_vegetables).
recommended_food(obesity, green_tea).

recommended_food(cardiac, salmon).
recommended_food(cardiac, walnuts).
recommended_food(cardiac, olive_oil).
recommended_food(cardiac, berries).
recommended_food(cardiac, avocado).

% Restricted foods for each disease
restricted_food(diabetes, sugar).
restricted_food(diabetes, white_rice).
restricted_food(diabetes, soda).
restricted_food(diabetes, white_bread).

restricted_food(hypertension, salt).
restricted_food(hypertension, pickles).
restricted_food(hypertension, processed_foods).
restricted_food(hypertension, canned_soups).

restricted_food(anemia, tea).
restricted_food(anemia, coffee).
restricted_food(anemia, dairy_products).

restricted_food(obesity, junk_food).
restricted_food(obesity, sugary_drinks).
restricted_food(obesity, fried_food).
restricted_food(obesity, processed_meat).

restricted_food(cardiac, red_meat).
restricted_food(cardiac, butter).
restricted_food(cardiac, cheese).
restricted_food(cardiac, fried_food).

% Main rule to suggest diet
suggest_diet(Disease) :-
    disease(Disease),
    write('For '), write(Disease), write(', you should eat:'), nl,
    recommended_food(Disease, Food),
    write('- '), write(Food), nl,
    fail.

suggest_diet(Disease) :-
    disease(Disease),
    write('Avoid these foods:'), nl,
    restricted_food(Disease, Food),
    write('- '), write(Food), nl,
    fail.

suggest_diet(_).  % To succeed after failure-driven loop
