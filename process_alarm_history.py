import json

with open('alarm_history.json') as json_file:
    data = json.load(json_file)
    for item in data['AlarmHistoryItems']:
        # if statement catches only state changes where alarm gets triggered
        if(item['HistorySummary']=="Alarm updated from OK to ALARM"):
        	print(item['AlarmName'] +','+ item['Timestamp'] +','+ item['HistorySummary'])


