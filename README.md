python3 main.py -f logs/access.log -g logs/access.log

1. read lines
2. statistics to show:
- Every 10s, display in the console the sections of the web site with the most hits
- restponse status count
- location by timezone
- users loged in
- Whenever total traffic for the past 2 minutes exceeds a certain number on average, add a message saying that “High traffic generated an alert - hits = {value}, triggered at {time}”
- Whenever the total traffic drops again below that value on average for the past 2 minutes, add another message detailing when the alert recovered
- Make sure all messages showing when alerting thresholds are crossed remain visible on the page for historical reasons.
- users/ip who are most active
- errors in the past time
