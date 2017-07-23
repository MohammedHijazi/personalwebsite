


def creat_dict():
	country_capital = {
	"Palestine":"Jerusalem",
	"Egypt":"Cairo",
	"USA":"DC",
	"Germany":"Berlin"}

	return country_capital




def main ():
	dectionary = creat_dict()
	country= raw_input ("Enter Your Country or enter to quit :")
	while (country != "" ):
		if country in dectionary:
			out_put(dectionary,country)
		else:
			print "No country is found"
		country= raw_input ("Enter Your Country or enter to quit :")




def out_put(dectionary,country):
	print "The capital of " + country + " is " + dectionary[country]





if __name__ == "__main__":
	main()

