import time
import webbrowser as wb

total_breaks = 3
break_count = 0

print('This program started on '+time.ctime())

while break_count < total_breaks:
    time.sleep(10)
    wb.open('https://www.youtube.com')
    break_count+=1

print('This program ended on '+time.ctime())
