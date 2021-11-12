import PatentData
import pymongo
from PatentData import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Configuration_Data
import MongoDBStore
from pymongo import collection
import time
import json
import os
import logging

#Contains all the functions and called in main when required
class Scrapper:

    #Function to fetch data for the given application number
    def GetBiblioData(driver): 

        try:
            logging.info("Starting Data scrapping")
            #Mapping the fetched Application Number to Application Number data in ContinuityDatum class in PatentData
            ApplicationNumberObj=ContinuityDatum()
            ApplicationNumberObj.application_number=driver.find_element_by_xpath(Configuration_Data.app_no_obj).text

            #Mapping the fetched Filing Date and Patent Status to Filing Date and Patent Status data in PatentCaseMetaData class in PatentData
            biblioObj1=PatentCaseMetaData()   
            biblioObj1.filing_date=driver.find_element_by_xpath(Configuration_Data.filing_date_obj).text
            biblioObj1.patent_status=driver.find_element_by_xpath(Configuration_Data.status).text
        
            #Mapping the fetched Publication Date and Number to Publication Date and Number data in PatentPublicationIdentification class in PatentData
            PublicationObj=PatentPublicationIdentification()
            PublicationObj.publication_date=driver.find_element_by_xpath(Configuration_Data.publication_date_obj).text
            PublicationObj.publication_number=driver.find_element_by_xpath(Configuration_Data.publication_no_obj).text
            biblioObj1.patent_publication_identification=PublicationObj

            #Mapping the fetched Inventor(s) to Inventor data in Parties class in PatentData
            InventorObj=Parties()
            Inventor=Applicant()
            Inventor.full_name=driver.find_element_by_xpath(Configuration_Data.inventor_obj).text
            """Since the applicants field is a list, creating an empty list and appending the name of the inventors in"""
            InventorObj.inventors=[]
            InventorObj.inventors.append(Inventor)
            biblioObj1.parties=InventorObj

            #Mapping the fetched CPC_Classification to Classifications_CPC data in TechnicalData class in PatentData
            ClassificationObj=TechnicalData()
            ClassificationObj.classifications_cpc=driver.find_element_by_xpath(Configuration_Data.cpc_obj).text
            biblioObj1.technical_data=ClassificationObj
        
            logging.info("Data scrapping completed successfully")
            return biblioObj1

        except Exception as e: 
            print("Error retrieving data")
            logging.error("Error occured during Data scrapping")
            driver.quit()
           
    #Function which parses through the webpage from where the data needs to be extracted    
    def navigate(driver):

        driver.switch_to.window(driver.window_handles[0])
        
        try:
            logging.info("Starting the parsing through the webpage")

            #Places the cursor the Application Number text field     
            search=driver.find_element_by_xpath(Configuration_Data.application_field)  

            #Clearing the text field of the previous Application Number so that the next number can be entered
            search.clear()
            
            #Enters the application number(s) (from the textfile) in the specified field
            search.send_keys(app_no)

            time.sleep(2)

            #Clicks on the search button at the end of the page        
            driver.find_element_by_xpath(Configuration_Data.search_button).click()

            time.sleep(2)

            logging.info("Parsing done successfully")

            return driver

        except Exception as e:
            print("Parsing cannot be done")
            logging.error("Error occured during webpage parsing")
            driver.quit()

    #Function which converts the extracted python object into a JSON object
    def toJSON(reference):
        logging.info("Starting JSON conversion")
        logging.info("JSON conversion successful")
        return json.dumps(reference, default=lambda o: o.__dict__,sort_keys=False, indent=4)  


    
if __name__=='__main__':

    try:

        #Creating a logger file to keep track of the steps
        logging.basicConfig(filename='EUScrape.log', level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

        logging.info("Opening and reading the text file")
        #Reading the text file which contains the required application numbers
        os.chdir(r'C:\Users\ojus.g_maxval\OjusG\Europe Scrape')
        f1=open('appnos.txt', 'r')

        #Read the application numbers from the text file 'appnos.txt'
        appno=f1.readlines() 

        logging.info("Automation starts")
        #Setting up the webdriver to read the EU Patent website
        driver= webdriver.Chrome(r"C:\\Users\\ojus.g_maxval\\Downloads\\chromedriver.exe")
        driver.get("https://register.epo.org/advancedSearch?lng=en")

        time.sleep(2)

        #To run the process in loop for multiple appication numbers
        for i in appno:

            logging.info("Main process starts")            
            #Strips the application number from unnecessary spaces inserted by readlines or manually
            app_no=i.strip()        

            #Calling the navigate funtion under the Scapper class to execute                     
            Scrapper.navigate(driver)

            #Calling the GetBiblioData funtion under Scapper class to execute
            o=Scrapper.GetBiblioData(driver)   

            #Calling the toJSON function under Scapper class to execute
            jsonstr=Scrapper.toJSON(o)

            time.sleep(2)
            driver.close()
            print(jsonstr)

            #Creating a separate JSON file for each application number
            with open(app_no+ '.json', 'w') as f:
                logging.info("Creating JSON")
                f.write(jsonstr)
                f.close

            #To push the JSON file into MongoDB
            with open(app_no+ '.json', 'r') as f1:

                logging.info("Pushing JSON data into MongoDB")

                file_data = json.load(f1)

                #Establishing connection with MongoDB
                mongo=MongoDBStore.Mongo(Configuration_Data.connection_string)

                #Getting database and collection name to insert data in desired collection in the database
                col=mongo.getCol('Europe','JSON_Data')
    
                #Inserting document into MongoDB
                mongo.insertOne(file_data,col)

                logging.info("Data successfully pushed into MongoDB")
    
    except Exception as e:
        print("Error, please check the code.")
        logging.error('Exception error occurred',exc_info=True)
        driver.quit()