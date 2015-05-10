import requests
import json
import datetime #import timedelta


def getCitiBikeData(stationID):
	date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
	url ='http://www.citibikenyc.com/stations/json'
	r = requests.get(url)
	result =  (r.text).encode('ascii', 'ignore')
	result = json.loads(result)

	executionTime = result['executionTime']
	for item in result['stationBeanList']:
		if item['id'] == int(stationID):
			status = {
				'time': executionTime,
				'station': item['stationName'],
				'available': item['availableBikes']
			}
	return json.dumps(status)


def main():
	print getCitiBikeData(437)



if __name__ == "__main__":
	main()

