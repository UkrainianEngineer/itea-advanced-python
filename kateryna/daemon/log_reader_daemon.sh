#!/bin/sh
SCRIPT=./parsing_logs.sh
RUNAS=root
PIDFILE=./my_command.pid
LOGFILE=./my_command.log

start() {
   if [ -f "$PIDFILE" ] && kill -0 $(cat "$PIDFILE"); then
   echo 'Service already running' >&2
    return 1
  fi
  echo 'Starting service…' >&2
  echo $$  > "$PIDFILE"
  local CMD="$SCRIPT &> \"$LOGFILE\" & echo \$!"
  su -c "$CMD" $RUNAS > "$PIDFILE"
  echo 'Service started' >&2
}

stop() {
  if [ ! -f "$PIDFILE" ] || ! kill -0 $(cat "$PIDFILE"); then
    echo 'Service not running' >&2
    return 0
  fi
  echo 'Stopping service...' >&2
  pkill -TERM -P $(cat "$PIDFILE") && rm -f "$PIDFILE"
  echo 'Service stopped' >&2
}
status() {
    if [ ! -f  "$PIDFILE" ] || ! kill -0 $(cat "$PIDFILE"); then
	    echo "Service not running" >&2
	    return 0
    else
	    echo "Service is running"
	    return 1
    fi
    exit 0

      	
}
case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;

  restart)
    stop
    start
    ;;
    status)
     status
     ;;
  *)
    echo "Usage: $0 { start | stop | restart | status}"
esac
