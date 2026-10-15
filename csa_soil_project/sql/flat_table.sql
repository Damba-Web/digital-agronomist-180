SELECT o.profile_id, o.layer_id,
       o.value_avg AS organic_carbon,
       p.value_avg AS ph,
       c.value_avg AS clay,
       s.value_avg AS sand
FROM wosis_orgc AS o
LEFT JOIN wosis_phaq AS p ON o.layer_id = p.layer_id
LEFT JOIN wosis_clay AS c ON o.layer_id = c.layer_id 
LEFT JOIN wosis_sand AS s ON s.layer_id = o.layer_id 
WHERE o.country_name = 'Ghana';
