from weather import Weather  #importing the Weather api
weather = Weather()


def api_pro():
	location = weather.lookup_by_location("halifax")
	condition = location.condition()
	a = condition["temp"]
	b = condition["temp"]
	i =0
	for forecasts in location.forecast():
		if a < forecasts["high"]:
			q = forecasts["date"]
			a = forecasts['high']
		if b < forecasts['low']:
			b = forecasts['low']
			
	print ("The highest temperature in the next 5 days of forecast is : ", a)
	print ("the lowest temperature in the next 5 days of forecast is : ", b)

api_pro()
