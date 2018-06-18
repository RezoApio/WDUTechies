# Slow Time in Oracle

```SQL
SELECT
	sid,
	serial#,
	username,
	osuser,
	machine,
	program,
	status,
	last_call_et,	/* Durée traitement en cours en secondes */
	ses.sql_id,
	event,		/* type d'attente en cours ENQ = LOCK ... */
	sql_text,	/* 1000 premiers caractéres de la requête, utiliser la colonne SQL_FULLTEXT pour le texte complet */
	executions AS EXECS,	/* nombre d'exécutions totale de cette requêtes sur la base */
	rows_processed AS ROWSS,
	round(elapsed_time / 1000000) AS ELAPS_SECONDS,
	first_load_time 	/* Date de derniére montée dans le cache */
FROM
	v$session ses  ,
	v$sql sql
WHERE
	type = 'USER'
	and (status IN ('ACTIVE','KILLED') 	/* Requêtes ACTIVES OU KILLED */
	or last_call_et < 1) 			/* OU Requêtes traitées il y a moins d'une seconde */
	and sql_hash_value = hash_value(+)
	and sql_child_number = child_number(+)
ORDER BY
	ses.status ASC,
	ses.LAST_CALL_ET DESC
/

```

# New Item