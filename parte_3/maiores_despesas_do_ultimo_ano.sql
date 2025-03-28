-- Operadoras que teve mais despesas no último ano
SELECT o.registro_ans, 
       o.razao_social, 
       SUM(REPLACE(d.vl_saldo_final, ',', '.')::numeric) AS total_despesas
FROM despesas d
JOIN operadoras o ON d.reg_ans = o.registro_ans
WHERE (d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS%' 
       OR d.descricao ILIKE '%AVISADOS DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR%')
  AND d.data >= '2024-01-01'
  AND d.data <= '2024-12-31'
GROUP BY o.registro_ans, o.razao_social
ORDER BY total_despesas DESC
LIMIT 10;