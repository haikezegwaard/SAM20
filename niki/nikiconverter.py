import requests
import logging


#Class to convert Niki data to the numbers needed
class NikiConverter:
    #static for now, should be replaced by oauth security model
    oauth_token = "90302891-25b2-43cb-8ef9-3dd4bc0955be"
    api_url = "https://api.niki.nl"
    #projectResource = "/projects/54/AMVP9518"
    availability = []

    #https://api.niki.nl/projects/54/AMVP9518
    def getProject(self, project):
        return self.apiRequest(project)

    def getHousesForSaleOrRent(self, project):
        self.getAvailability(project)
        return self.availability[0]

    def getHousesUnderOption(self, project):
        self.getAvailability(project)
        return self.availability[1]

    def getHousesSoldOrRented(self, project):
        self.getAvailability(project)
        return self.availability[2]

    def getAvailability(self, project):
        projectType = self.getProjectSaleRentType(project)
        self.availability = [0,0,0] #reset counters [forsale/rent, option, sold/rented]
        #get housetypes of project
        for housetype in self.apiRequest(project+"/housetypes"):
            #get number for sale/for rent
            forSaleOrRent = housetype.get('houses').get(projectType)
            if(forSaleOrRent is not None):
                self.availability[0] += int(forSaleOrRent)
            #get number of houses under option
            underOption = housetype.get('houses').get('option')
            if(underOption is not None):
                self.availability[1] += int(underOption)
            #get number of houses sold or rented
            soldRentedStr = 'sold'
            if(projectType == 'for-rent'):
                soldRentedStr = 'rented'
            soldRented = housetype.get('houses').get(soldRentedStr)
            if(soldRented is not None):
                self.availability[2] += int(soldRented)
        return self.availability

    def getProjectSaleRentType(self, project):
        projectJson = self.apiRequest(project)
        saleRent = 'for-sale'
        if(projectJson.get('type') == 'huur'):
            saleRent = 'for-rent'
        return saleRent

    def apiRequest(self, resource):
        """do the request, append oauth token"""
        if(isinstance(resource, int)):
            logging.error("int: {}".format(resource))
        url = self.api_url+resource+ "?oauth_token=" + self.oauth_token
        logging.warn("api call to: "+ url)
        r = requests.get(url)
        return r.json()
