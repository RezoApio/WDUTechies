# Workflow Queries

| Table | Usage |
| --- | --- |
| S_ESCL_REQ | This table holds the potential matching requests caused by applications. |
| S_ESCL_STATE | This table holds the time-based policy matches. |
| S_ESCL_ACTN_REQ | Optional. This table holds the requests to execute actions. This is only used if you use Action Agent=TRUE. |
| S_ESCL_LOG | This table holds a history of base table rows that have matched policies. |
 
## Policies (DB Triggers)
```SQL

SELECT
 g.NAME,
 r.OBJECT_NAME,
 r.NAME "Rule",
 r.SUB_TYPE_CD,
 r.ACTIVATE_DT,
 r.EXPIRE_DT
FROM
 SIEBEL.S_ESCL_RULE r
 LEFT OUTER JOIN SIEBEL.S_ESCL_GROUP g ON (g.ROW_ID = r.GROUP_ID)
--WHERE
--r.ACTIVATE_DT IS NOT NULL
ORDER BY g.NAME, r.OBJECT_NAME, r.NAME, r.ACTIVATE_DT DESC
for read only with ur;
```

## Current Request Count S_ESCL_REQ (Trigger executed)

```SQL

SELECT
  req.GROUP_ID,
  G.NAME "Group",
  req.TBL_NAME,
  rul.NAME "Rule",
  COUNT(*) "Count",
  MIN(REQ_ID) "First Request ID",
  to_char(MIN(req.created),'YYYY-MM-DD HH24:MI:SS') "First",
  MAX(REQ_ID) "Last Request ID",
  to_char(MAX(req.created),'YYYY-MM-DD HH24:MI:SS') "Last"
FROM
    SIEBEL.S_ESCL_REQ req,
    SIEBEL.S_ESCL_GROUP G,
    SIEBEL.S_ESCL_RULE rul
WHERE
    G.ROW_ID = req.GROUP_ID AND
    rul.ROW_ID = req.RULE_ID
    -- AND to_char(req.created,'YYYY-MM-DD HH24:MI:SS') >= '2008-XX-XX 00:00:00'
GROUP BY
    req.GROUP_ID,G.NAME, req.TBL_NAME, rul.NAME
```

## Current Requests  S_ESCL_REQ (Trigger executed)

```SQL

SELECT req.GROUP_ID,G.NAME "Group",rul.NAME "Rule",
  req.TBL_NAME "Table",
  req.BT_ROW_ID "Tbl Row Id",
  to_char(req.created,'YYYY-MM-DD HH24:MI:SS') "Req Created",
  req.created_by,
  req.req_id
FROM
    SIEBEL.S_ESCL_REQ req,
    SIEBEL.S_ESCL_GROUP G,
    SIEBEL.S_ESCL_RULE rul
WHERE
    G.ROW_ID = req.GROUP_ID AND
    rul.ROW_ID = req.RULE_ID
    --AND to_char(req.created,'YYYY-MM-DD HH24:MI:SS') >= '2008-05-29 03:10:00'
ORDER BY
     req.CREATED DESC;
```

## Current Action Requests S_ESCL_ACTN_REQ (Action Agent=TRUE)

```SQL

SELECT
    G.NAME "Group",
    rul.NAME "Rule",
    act_req.*
FROM
    SIEBEL.S_ESCL_ACTN_REQ act_req,
    SIEBEL.S_ESCL_GROUP G,
    SIEBEL.S_ESCL_RULE rul
WHERE
    G.ROW_ID = rul.GROUP_ID AND
    rul.ROW_ID = act_req.RULE_ID
ORDER BY
    act_req.CREATED;
```

## Escalation LOG (History)

```SQL
select
  G.NAME "Group",
  rul.NAME "Rule",
  to_char(l.violated_dt,'yyyy-mm-dd HH24:MI') "Violated Dt",
  l.table_name "Table",
  l.bt_row_id "Table RowId",
  l.user_key
from SIEBEL.s_escl_log l, SIEBEL.S_ESCL_GROUP G, SIEBEL.S_ESCL_RULE rul
where
  rul.ROW_ID = l.RULE_ID AND
  G.ROW_ID = rul.GROUP_ID
  AND to_char(l.violated_dt,'yyyy-mm-dd HH24:MI') >= '2012-12-31 00:00'
```

# Repository Queries

## Scripted BCs

```SQL
select
       BC.NAME "BC",
       S.NAME "Name",
       S.SCRIPT "Script"
from
     S_BUSCOMP_SCRIPT S,
     S_BUSCOMP BC,
     S_REPOSITORY R
where
     S.BUSCOMP_ID = BC.ROW_ID (+) AND
     S.REPOSITORY_ID = R.ROW_ID (+) AND
     R.NAME = 'Siebel Repository' AND
     ( S.SCRIPT IS NOT NULL)
order by
      BC.NAME
```

## Local unlock:

```SQL
UPDATE siebel.S_PROJECT
SET LOCKED_FLG='N', LOCKED_DATE=NULL, LOCKED_BY=null
where
ROW_ID = '1-263Y-FRU';

update SIEBEL.S_BUSCOMP SET
OBJ_LOCKED_FLG = 'N',
OBJ_LOCKED_DATE = NULL
where ROW_ID = 'xxxxx';
```

## BC Properties

```SQL
select
       BC.NAME "BC",
       P.NAME "Property",
       P.PROPERTY,
       P.VALUE
from
     S_BUSCOMP_UPROP P,
     S_BUSCOMP BC
where
     BC.ROW_ID = P.BUSCOMP_ID (+) AND
     ( P.VALUE LIKE '%Courante%' OR P.VALUE LIKE '%PRC%osi%Calc%' OR
      P.NAME LIKE '%Courante%' OR P.NAME LIKE '%PRC%osi%Calc%')
order by
      BC.NAME
```

## BC Fields used on Applets

### Form Applet

```SQL
select a.buscomp_name "Business Component"
 , ctrl.field_name "Field"
 , a.name "Applet"
from SIEBEL.s_repository rep
 , SIEBEL.s_applet a
 , SIEBEL.s_control ctrl
where rep.name = 'Siebel Repository'
 and a.repository_id = rep.row_id
 and ctrl.repository_id = rep.row_id and ctrl.applet_id = a.row_id
 and a.buscomp_name = ''
 and ctrl.field_name = ''
```
### List Applet

```SQL
select a.buscomp_name "Business Component"
 , lst_col.field_name "Field"
 , a.name "Applet"
from SIEBEL.s_repository rep
 , SIEBEL.s_applet a
 , SIEBEL.s_list lst
 , SIEBEL.s_list_column lst_col
where rep.name = 'Siebel Repository'
 and a.repository_id = rep.row_id
 and lst.repository_id = rep.row_id and lst.applet_id = a.row_id
 and lst_col.repository_id = rep.row_id and lst.row_id = lst_col.list_id
 and a.buscomp_name = ''
 and lst_col.field_name = ''
```

## Add a user in DBA authentication

```SQL
create user FP13794 identified by "MySecurePwd";
grant SSE_ROLE to FP13794;
alter user FP13794 default tablespace D_CBB01;
alter user FP13794 temporary tablespace TMP01; 

```

## New Item

```SQL


```
