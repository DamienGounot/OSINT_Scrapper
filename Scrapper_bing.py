import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main(argv):
	browser = webdriver.Firefox()
	r = browser.get('https://www.bing.com')
	search = browser.find_element_by_id('sb_form_q')
	term = argv[1]
	search.send_keys(term)
	search.send_keys(Keys.ENTER)
	#for r in browser.find_elements_by_tag_name('cite'):
    	#print(r.text)

if __name__ == "__main__":
	main(sys.argv)