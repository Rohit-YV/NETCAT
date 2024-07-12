# NETCAT
ITS a clone tool of Netcat..just made for understanding the concept


USEAGE --->

/ranja/python/black_hat$ python3 NetcatV1.py --h
usage: NetcatV1.py [-h] [-c] [-e EXECUTE] [-l] [-p PORT] [-u UPLOAD] [-t TARGET]

BHP Net TOOL

options:
  -h, --help            show this help message and exit
  -c, --command         command shell
  -e EXECUTE, --execute EXECUTE
                        execute command
  -l, --listen          listen
  -p PORT, --port PORT  specified port
  -u UPLOAD, --upload UPLOAD
                        upload file
  -t TARGET, --target TARGET
                        specified IP address

example:
            netcat.py -t 192.168.1.1 -p 5555 -l -c #command shell
            netcat.py -t 192.168.1.1 -p 5555 -l -c -e='cat /etc/passwd' #execute command
            netcat.py -t 192.168.1.1 -p 5555 -l -c -u=my_test.txt #upload file
            echo 'ABC' | netcat.py -t 192.168.1.1 -p 5555  #echo text to server
            netcat.py -t 192.168.1.1 -p 5555 #connect to server



============================================================
 python netcat.py -t 192.168.1.203 -p 5555 -l -c
-------------------------------------------------------------------------
 python netcat.py -t 192.168.1.203 -p 5555
CTRL-D
<BHP:#> ls -la
total 23497
drwxr-xr-x 1 502 dialout 608 May 16 17:12 .
drwxr-xr-x 1 502 dialout 512 Mar 29 11:23 ..
-rw-r--r-- 1 502 dialout 8795 May 6 10:10 mytest.png
-rw-r--r-- 1 502 dialout 14610 May 11 09:06 mytest.sh
-rw-r--r-- 1 502 dialout 8795 May 6 10:10 mytest.txt
-rw-r--r-- 1 502 dialout 4408 May 11 08:55 netcat.py
<BHP: #> uname -a
----------------------------------------------------------------------------
 python netcat.py -t 192.168.1.203 -p 5555 -l -e="cat /etc/passwd"
 ---------------------------------------------------------------------------
 python netcat.py -t 192.168.1.203 -p 5555
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
We could also use netcat on the local machine:
% nc 192.168.1.203 5555
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin

---------------------------------------------------------------
 echo -ne "GET / HTTP/1.1\r\nHost: reachtim.com\r\n\r\n" |python ./netcat.py -t reachtim.com
-p 80

Server: nginx
Date: Mon, 18 May 2020 12:46:30 GMT
Content-Type: text/html; charset=iso-8859-1
Content-Length: 229
Connection: keep-alive
Location: https://reachtim.com/
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="https://reachtim.com/">here</a>.</p>
</body></html>
