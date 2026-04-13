-- Hello kitty
SELECT origin, SUM(fans) AS vb_fans
FROM metal_bands
GROUP BY origin
ORDER BY vb_fans DESC;
