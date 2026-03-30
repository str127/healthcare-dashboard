-- Average satisfaction per service
SELECT service, AVG(satisfaction)
FROM patients
GROUP BY service;

-- Heart disease count
SELECT target, COUNT(*)
FROM heart
GROUP BY target;

-- Age vs heart disease
SELECT target, AVG(age)
FROM patients
JOIN heart ON patients.patient_id = heart.patient_id
GROUP BY target;