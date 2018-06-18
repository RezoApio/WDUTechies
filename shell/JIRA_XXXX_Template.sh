#!/usr/bin/ksh

##
## Script Template for Jira Data Recovery
## WDU 17/01/17
## For usage help, please check https://mtwiki.michelin.com/xns/display/BIB/Data+Recovery+Development
## Normally a change&replace XXXX with your number will be enough
## 
## This script will do the following DR:
##
## *****************************************************************************
##

_DEBUG="off"
DEBUG ()
{
	[ "$_DEBUG" == "on" ] && $@
}

PAUSE ()
{
	#debugging function to allow stopping process
	#will finish with an arbitrary 99 code
	DEBUG echo "Debug Pause. Any key to continue or Q to quit with exit 99"
	while true
	do
		DEBUG read vPause
		if [ "$vPause""a" = "Qa" ]; then fin 99; else break; fi
	done
}

SMGR ()
{
	#set -vx
	$CBB_SRVRMGR_CMD /g $CBB_GATEWAY /e $CBB_ENTERPRISE_SERVER /u $LOGIN_SADMIN /p $MDP_SADMIN /k "|" "$@"
}


EIM ()
{
	#This function assumes the file to be w/o the ifb extension
	file=$1
	DEBUG echo $file
	
	log "Running EIM for file: $file"
	if [ ! -f $IFB_DIR/${file}.ifb ]; then log "File not found : ${file}.ifb"; fin 1; fi

	cmd="run task for comp eim with config=${IFB_DIR}/${file}.ifb,ErrorFlags=1, TraceFlags=1, SQLFlags=8, LogDir=${B2B_LOG_FOLDER}"
		
	DEBUG echo "SMGR -s $CBB_SIEBEL_SERVER -c $cmd -o ${B2B_LOG_IFB_FOLDER}/CBB_eim_${file}_${Dlancement}.log"
	PAUSE
	
	SMGR -s $CBB_SIEBEL_SERVER -c "$cmd" -o ${B2B_LOG_IFB_FOLDER}/CBB_eim_${file}_${Dlancement}.log

}


SQL ()
{
	#This function assumes the file to contain the .sql
	#set -vx
	file=$1
	
	if [ ! -f $SQL_DIR/$file ]; then log "Missing file "$file; fin 1
	else
		log "Starting SQL for : "$file
		$B2B_SQLP_EXE -s $B2B_ORA_USER/$B2B_ORA_PASS@$B2B_ORA_BASE @$SQL_DIR/$file 1>>/tmp/$$sqlout 2>&1
		ret=$?
		if [ $ret -eq 0 ]; then log "SQL Exec OK for: "$file; 
		else 
			log "SQL Exec with return code "$ret" for "$file; 
			cat /tmp/$$sqlout >> $LogFile
			fin 1
			#on bloque le traitement si un SQL est en erreur
		fi
	fi	
	#set +vx
}

GatherStats ()
{
	#This function assumes the file to be w/o the ifb extension
	file=$1
	DEBUG echo $file
	
	log "Making SQL file for Gather Stats"
	grep "TABLE[ ]*=" $IFB_DIR/${file}.ifb | awk -F "=" '{print $2}' | sed 's/ //g' > /tmp/$$gather
	
	
	echo "WHENEVER SQLERROR EXIT 1\nWHENEVER OSERROR EXIT 1" > $SQL_DIR/gather.sql

	while read table
	do
		echo "execute DBMS_STATS.GATHER_TABLE_STATS(ownname => 'CBB_DBA', tabname => '$table');" >> $SQL_DIR/gather.sql
		echo "/" >> $SQL_DIR/gather.sql
	done < /tmp/$$gather
	
	echo "exit 0;" >> $SQL_DIR/gather.sql
	
	PAUSE
	
	SQLDBA gather.sql
}

SQLDBA ()
{
	#set -vx
	#This function will run the Gather stats before running the SQL
	#The Gather Stats script will be auto generated.
	#This function assumes the file to contain the .sql
	#set -vx
	file=$1
	
	if [ ! -f $SQL_DIR/$file ]; then log "Missing file "$file; fin 1
	else
		log "Starting SQL for : "$file
		$B2B_SQLP_EXE -s $LOGIN_DBO/$MDP_DBO@$B2B_ORA_BASE @$SQL_DIR/$file 1>>/tmp/$$sqlout 2>&1
		ret=$?
		if [ $ret -eq 0 ]; then log "SQL Exec OK for: "$file; 
		else 
			log "SQL Exec with return code "$ret" for "$file; 
			cat /tmp/$$sqlout >> $LogFile
			fin 1
			#on bloque le traitement si un SQL est en erreur
		fi
	fi	
	#set +vx	
	
}


HISTORIZE ()
{
	HISTO_DIR=$B2B_LOG_FOLDER/$Dlancement
	#making sure we can create by using -p
	mkdir -p $HISTO_DIR
	mv -f $B2B_LOG_FOLDER/*.log $HISTO_DIR
}

log ()
{
	timestamp=`date "+%H:%M:%S"`
	echo $timestamp"==>"$@ | tee -a $LogFile
}

usage ()
{
	echo "usage: JIRA_XXXX.sh"
}

fin ()
{

	rm -f /tmp/$$*
	
	echo "Script log file: "$LogFile
	
    exit $1
	
}

################################ BEGINNING OF THE SCRIPT ###############################"

Dlancement=`date "+%y%m%d_%H%M"`
CUR_DIR=$(cd `dirname $0` && pwd)

CFG_DIR=$(cd $CUR_DIR/../cfg && pwd)
IFB_DIR=$(cd $CUR_DIR/../ifb && pwd)
SQL_DIR=$(cd $CUR_DIR/../sql && pwd)

LogFile=$CUR_DIR/tmp.log


log "Sourcing CBB Environment"
if [ -f $HOME/CBB_ENV.sh ]; then . $HOME/CBB_ENV.sh 1>/dev/null 2>&1; else log "Not a CBB env. Cannot run Migration Script"; fin 1; fi
log "Sourcing Purge Interface Environment"
if [ -f $CFG_DIR/CBB_VAR.cfg ]; then . $CFG_DIR/CBB_VAR.cfg 1>/dev/null 2>&1; else log "Missing CBB_VAR.cfg file. Please correct before running script again"; fin 1; fi

#Now Folder are sourced correctly
#so we can switch log
TmpLogFile=$LogFile
LogFile=$B2B_LOG_FOLDER/JIRA_XXXX_$Dlancement.log
cat $TmpLogFile > $LogFile
rm $TmpLogFile


log "Step 1: Loading EIM table"
SQL DataRecovery_XXXX.sql

PAUSE

log "Step 2: Running EIM to update lines"
GatherStats DataRecovery_XXXX
EIM DataRecovery_XXXX

PAUSE

log "Step 3: Moving files to history folder"
HISTORIZE

fin 0