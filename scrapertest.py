from bs4 import BeautifulSoup as bs # To parse the html page
import subprocess # To run a command to download pdf.
import requests # To Download the Html page of GGSIPU Results
import webbrowser


url = "http://164.100.158.135/ExamResults/ExamResultsmain.htm"
download_url= "http://164.100.158.135/ExamResults/"
branch = ''
sem = ''
fetch_url = ''
branch = raw_input('Enter Your Branch(eg: IT,CSE,ECE)')
sem = raw_input('Enter Your Semester(eg: 2nd, 4th, 6th)')


try:
    r = requests.get(url)
    soup = bs(r.text)
    start_branch = soup.find_all('td')
    
    for x in start_branch:
        if sem in x.get_text():
            if branch in x.get_text():
                print x.get_text()
                y = raw_input("\nWant to see next link? Y/N" )
                if (y == 'Y' or y=='y'):
                    continue
                else:
                    print ("found")
                    text = (x.get_text())
                    href = x.findNext('a')['href']
                    fetch_url = download_url+ href
                    print fetch_url
                    print('Starting Automatic Download , Please wait while Download finishes.')
                    command = ['wget', fetch_url]
                    output = subprocess.call(command)
		    print('Download Complete')		
                    break
except:
    print "Not found"
