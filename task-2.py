from weather import Weather  #importing the Weather api
weather = Weather()


def api_pro():
	location = weather.lookup_by_location("halifax")
	condition = location.condition()
	a = condition["temp"]
	b = condition["temp"]
	w = " "
	q = " "
	i =0
	for forecasts in location.forecast():
		if a < forecasts["high"]:
			q = forecasts["date"]
			a = forecasts['high']
		if b < forecasts["low"]:
			b = forecasts["low"]
			w = forecasts["date"]
	print ("The highest temperature in the next 5 days of forecast is  ", a, " and the day is " , q)
	print ("the lowest temperature in the next 5 days of forecast is  ", b, " and the day is ", w)


api_pro()
