import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main(argv):
	date = []
	url = []
	md5 = []
	ip = []
	browser = webdriver.Firefox()
	website = 'http://vxvault.net'
	data = browser.get(website)
	for data in browser.find_elements_by_class_name(".TD"):
		print(data.text)


if __name__ == "__main__":
	main(sys.argv)