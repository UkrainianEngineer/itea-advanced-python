#!/bin/bash


 advanced_syslog() {
   function log {
        while read LINE; do
                  if [[ $LINE == "6"* ]]; then
                          echo $LINE >> info.log
                  elif [[ $LINE == "7"* ]]; then
                          echo $LINE >> debug.log
                  elif [[ $LINE == "4"* ]]; then
                          echo $LINE >> warning.log
                  elif [[ $LINE == "3"* ]]; then
                          echo $LINE >> error.log

                  fi
             done
     }

    tail -f /var/log/syslog | log
 }
advanced_syslog
