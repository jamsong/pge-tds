<h1>songPower Reader</h1>  
Read usage data from Portland General Electric to create a CSV file that shows the daily power usage into five Time of Day segments: 00:00-06:59 (Off Peak AM), 07:00-11:59 (Mid Peak AM), 12:00-16:59 (Mid Peak PM), 17:00-20-59 (On Peak) and 21:00-23:59 (Off Peak PM).

<h2>Usage</h2>
Run ./songPower pgn_filename.csv optional_output_filename

<h2>Example Output</h2>
Date,DayOfWeek,00:00-06:59,07:00-11:59,12:00-16:59,17:00-20:59,21:00-23:59,Total<br>
2021-01-01,Fri,10.11,7.0,38.88,8.88,5.12,69.99<br>
2021-01-02,Sat,9.32,10.95,9.59,11.57,5.23,46.66<br>
2021-01-03,Sun,8.94,7.45,9.45,9.04,5.02,39.9
