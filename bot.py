import getpass
import requests
from lxml import html
import json

with requests.Session() as s:

	fL = s.get("https://www.footlocker.com/account/default.cfm")
	html_fL = html.fromstring(fL.content)

	requestKeys =  html_fL.xpath('//input[@name="requestKey"]/@value')

	username = raw_input("Input Account Username/Email: ")
	password = raw_input("Type Password: ")
	size = raw_input("Input Size: ")

	login_url = "https://www.footlocker.com/account/default.cfm?action=accountSignIn"
	payload = { 'companyCode': '21', 'requestKey': requestKeys[1], 'email' : username, 'password' : password }

	result = s.post(login_url, data=payload)

	is_not_yet_added = True
	# print result.text
	while is_not_yet_added:
		cart_url = "http://www.footlocker.com/catalog/miniAddToCart.cfm?secure=0&"
		cart_payload = { 'requestKey' : requestKeys[1], 'storeNumber':'00000', 'qty': 1, 'size': size, 'the_model_nbr':'254106', 'sku':'BB1826', 'inlineAddToCart':'0', 'coreMetricsCategory':'blank', 'hasXYPromo':'false', 'BV_TrackingTag_Review_Display_Sort':'http://footlocker.ugc.bazaarvoice.com/8001/91246/reviews.djs?format=embeddedhtml', 'rdo_deliveryMethod':'shiptohome', 'fulfillmentType':'SHIP_FROM_STORE' }

		# cart_payload = { 'requestKey' : requestKeys[1], 'storeNumber':'00000', 'qty': 1, 'size': size, 'the_model_nbr':'184587', 'sku':'A18AHD47', 'inlineAddToCart':'0', 'coreMetricsCategory':'blank', 'hasXYPromo':'false', 'BV_TrackingTag_Review_Display_Sort':'http://footlocker.ugc.bazaarvoice.com/8001/91246/reviews.djs?format=embeddedhtml', 'rdo_deliveryMethod':'shiptohome', 'fulfillmentType':'SHIP_FROM_STORE' }
		

		print cart_payload;
		cart = s.post(cart_url, data=cart_payload)

		cart_html = html.fromstring(cart.content)
		cart_res = cart_html.xpath('//span[@class="error"]/@text')

		c_details = json.loads(cart.content)
		print c_details['success']
		if c_details['success'] == False:
			is_not_yet_added = True
		else:
			print "Tangina"
			is_not_yet_added = False
	
