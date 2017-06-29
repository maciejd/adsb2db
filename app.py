import requests,json,sqlite3,time

url = 'http://127.0.0.1/dump1090/data/aircraft.json'
conn = sqlite3.connect('app.db')

while True:
    response = requests.get(url)

    if (response.ok):
        data = json.loads(response.content)
        for aircraft in data['aircraft']:
            c = conn.cursor()
            c.execute("INSERT OR REPLACE INTO aircrafts('hex','flight','timestamp') VALUES (?,?,?)", (aircraft['hex'],aircraft['flight'] if 'flight' in aircraft else "",time.time()))            	        
	    conn.commit()
    else:
        response.raise_for_status()
    time.sleep(1)
