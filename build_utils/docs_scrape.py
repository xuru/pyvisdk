'''
Created on Jul 4, 2011

@author: eplaster
'''
import urllib2, sys
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import Tag
from pprint import pprint, pformat

class DocScrapper(object):
    '''
    Class to scrape the VMware vSphere web services API documentation and insert method doc strings.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.base_url = "http://www.vmware.com/support/developer/vc-sdk/visdk41pubs/ApiReference/"
        self.method_index = self.base_url + "index-methods.html"
        self.mo_types_index = self.base_url + "index-mo_types.html"
        self.fd = None
        
        
    def scrape(self):
        page = urllib2.urlopen(self.mo_types_index)
        soup = BeautifulSoup(page)
        self.fd = open("docs_dict.py", "w")
        
        data = {}
        for link in soup('a', target="classFrame"):
            href = link['href']
            name = link.text
            mo = self.scrape_MO(href, name)
            data[name] = mo
                 
        self.fd.write("API_docs = " + self.clean(pformat(data)))
        self.fd.close()
            
    def scrape_MO(self, href, name):  
        print "Fetching info on %s... [%s]" % (name, self.base_url + href)
        
        page = urllib2.urlopen(self.base_url + href)
        soup = BeautifulSoup(page)
        
        mo = {
            'name': name,
            'desc': self.get_MO_description(soup),
            'methods': [],
        }
        
        methods = soup.findAll('h1')[1:]
        for method in methods:
            mo['methods'].append( self.get_method_description(method))
            
        return mo
        
    def get_MO_description(self, soup):
        desc = ''
        mo_description = soup.find('h2')
        end = soup.find('a', id="field_detail")
        
        gen = mo_description.next.next.next.nextGenerator()
        obj = gen.next()
        while end != obj:
            if isinstance(obj, Tag):
                desc += " "+str(obj)+" "
            else:
                desc += obj.string.strip()
            obj = gen.next()
        return desc
            
    def get_method_description(self, method):
        desc = ''
        name = method.string
        end = method.find('p', id="table-title")
        
        gen = method.next.next.next.nextGenerator()
        obj = gen.next()
        while end != obj:
            if isinstance(obj, Tag):
                desc += " "+str(obj)+" "
            else:
                desc += obj.string.strip()
            obj = gen.next()
        return (name, desc)
            
    def clean(self, text):
        text = text.replace('\t', '')
        text = text.replace('\r', '')
        text = text.replace('\n', '')
        return text
            
ds = DocScrapper()
ds.scrape()