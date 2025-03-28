-- Operadoras e total de despesas no último trimestre de 2023
SELECT o.registro_ans, 
       o.razao_social,
       SUM(REPLACE(d.vl_saldo_final, ',', '.')::numeric) AS total_despesas
FROM operadoras o
JOIN despesas d ON o.registro_ans = d.reg_ans
WHERE (d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS%' 
       OR d.descricao ILIKE '%AVISADOS DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR%')
  AND d.data >= '2023-10-01'
  AND d.data <= '2023-12-31'
  AND d.vl_saldo_final IS NOT NULL
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC;