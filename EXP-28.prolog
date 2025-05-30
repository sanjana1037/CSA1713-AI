symptom(fever).
symptom(cough).
diagnosis(flu) :- symptom(fever), symptom(cough).
QUERY:diagnosis(Disease). OR diagnosis(flu).
