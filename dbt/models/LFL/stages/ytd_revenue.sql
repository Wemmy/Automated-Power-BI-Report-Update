{{
  config(
    materialized='incremental',
    unique_key = ['gldate', 'businessunit', 'objectaccount', 'jeexplanation']
  )
}}

SELECT 
  top 100
FROM 