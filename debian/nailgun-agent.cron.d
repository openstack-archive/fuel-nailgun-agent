* * * * * root timeout -k 70 60 flock -w 0 -o /var/lock/nailgun-agent.lock -c "/usr/bin/nailgun-agent 2>&1 | tee -a /var/log/nailgun-agent.log  | /usr/bin/logger -t nailgun-agent"
