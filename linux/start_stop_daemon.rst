Introduction
~~~~~~~~~~~~

This document describes Linux task. It **costs 10 bonus points**.

Task
~~~~

Create start-stop daemon, which has: *start, stop, status* states.
After starting it via **daemon start** command, it should create `.pid` file
with PID of started daemon.

**daemon stop** command should stop daemon and remove `.pid` file.

**daemon status** command should show a status of *daemon*.
If it is still running, this command should print PID of daemon.
If daemon is stopped, it should print appropriate message.


Daemon responsibilities
~~~~~~~~~~~~~~~~~~~~~~~

1. If daemon was started, it should runs as a background process,
without command line interaption.

2. Daemon should runs forever until **daemon stop** command is executed.

2. Daemon should reads some logging file.
   (e.g. some system logging, syslog, custom logging, etc.)

3. Daemon should parse logging file in real time and find separately:
    **ERROR**, **INFO**, **DEBUG** messages.

4. Daemon should writes parsed messages into separate appropriate files.
   For example: `error.log`, `debug.log`, `info.log`.


Useful information
~~~~~~~~~~~~~~~~~~

Links which may helps for this task:

1. Start-stop daemon skeleton:

https://gist.github.com/shawnrice/11076762

2. What is start-stop daemon. (rus documentation):

http://help.ubuntu.ru/wiki/start-stop-daemon

3. Daemons (rus):

http://citforum.ck.ua/programming/unix/daemons/

4, What is PID and how to use it:

https://ru.wikipedia.org/wiki/Идентификатор_процесса

https://www.digitalocean.com/community/tutorials/how-to-use-ps-kill-and-nice-to-manage-processes-in-linux

5. Start process in background:

https://linuxaria.com/article/how-to-run-commands-background-nohup-disown

6. Linux logs: location and how to view:

https://www.cyberciti.biz/faq/linux-log-files-location-and-how-do-i-view-logs-files/

7. Read logging file in real time on Linux:

https://www.howtogeek.com/howto/ubuntu/a-live-view-of-a-logfile-on-linux/
