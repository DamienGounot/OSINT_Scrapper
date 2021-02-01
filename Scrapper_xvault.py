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
	r = browser.get(website)
	for r in browser.find_element_by_css_selector('td'):
    	print(r)

if __name__ == "__main__":
	main(sys.argv)