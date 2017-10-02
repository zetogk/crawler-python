import requests
import io
from bs4 import BeautifulSoup

class Crawler:

    @staticmethod
    def addContentToFile(filename, content):
        with open(filename, 'a+') as f:
            f.write(str(content)+'\n')
            f.close()

    @staticmethod
    def getLinksFromOneWeb(web, outputFile = ''):
        request = requests.get(web)
        #print(request.text)
        soup = BeautifulSoup(request.text, 'html.parser')

        if outputFile == '':
            print 'The data wont be saved'
            for link in soup.find_all('a'):
                print(link.get('href'))
        else:
            print 'The data will be saved'
            for link in soup.find_all('a'):
                Crawler.addContentToFile(outputFile, link.get('href'))

    @staticmethod
    def getLinksFromSeveralsWeb(filename, outputFile = ''):
        with io.open(filename, 'rt', newline='') as f:
            lines = f.readlines()

        if outputFile == '':
            print 'The data wont be saved'

            for line in lines:
                request = requests.get(line.strip('\r\n').strip('\r').strip('\n'))
                soup = BeautifulSoup(request.text, 'html.parser')

                for link in soup.find_all('a'):
                    print(link.get('href'))

        else:
            print 'The data will be saved'
            
            for line in lines:
                request = requests.get(line.strip('\r\n').strip('\r').strip('\n'))
                soup = BeautifulSoup(request.text, 'html.parser')

                for link in soup.find_all('a'):
                    Crawler.addContentToFile(outputFile, link.get('href'))

Crawler.getLinksFromOneWeb('http://www.mundoenlaces.com', 'result.dat')
Crawler.getLinksFromSeveralsWeb('source.dat', 'several-result.dat')
