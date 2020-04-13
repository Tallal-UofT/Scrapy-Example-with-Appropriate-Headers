# -*- coding: utf-8 -*-
import scrapy



class Github_Example(scrapy.Spider):
    name = 'Example'
    allowed_domains = ['URL']
    
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    start_urls = ['URL={number}'.format(number=number)
                  for number in range(X,Y)]
    
    def parse(self, response):

            
        ActualRecords = response.css("p *::text").getall()
        print(ActualRecords)
        del ActualRecords[0]
        del ActualRecords[0]

        del ActualRecords[0]
       
#Combining pairs of records in a list 
        ActualRecords1 = [ActualRecords[i] + ActualRecords[i+1] for i in range(0,len(ActualRecords),2)]
        print(ActualRecords1)
        result1 = ActualRecords1
 
#Creating Balanced and rectangularized data set       
        if 'Surname' not in result1[0]:
            result1.insert( 0, 'Surname:')
    
        if 'Given Name' not in result1[1]:
            result1.insert( 1, 'Given Name:')
    
        if 'Gender' not in result1[2]:
            result1.insert( 2, 'Gender:')
    
        if 'Age' not in result1[3]:
            result1.insert( 3, 'Age:')
    
    
        if 'Birth Year' not in result1[4]:
            result1.insert( 4, 'Birth Year:')
    
        if 'Birth Month' not in result1[5]:
            result1.insert( 5, 'Birth Month:')
    
        if 'Marital Status' not in result1[6]:
            result1.insert( 6 ,'Marital Status:')
    
        if 'Place of Birth' not in result1[7]:
            result1.insert( 7, 'Place of Birth:')
    
        if 'Relationship' not in result1[8]:
            result1.insert( 8, 'Relationship:')
    
        if 'Ethnic Origin' not in result1[9]:
            result1.insert( 9, 'Ethnic Origin:')
    
        if 'Year of Immigration' not in result1[10]:
            result1.insert( 10, 'Year of Immigration:')
    
        if 'Province' not in result1[11]:
            result1.insert(11, 'Province:')
    
        if 'District Name' not in result1[12]:
            result1.insert( 12, 'District Name:')
    
        if 'District Number' not in result1[13]:
            result1.insert( 13, 'District Number:')
                
        if 'Sub-District Name' not in result1[14]:
            result1.insert( 14, 'Sub-District Name:')
                        
        if 'Sub-District Number' not in result1[15]:
            result1.insert( 15, 'Sub-District Number:')
                        
        if 'Sub-District Description' not in result1[16]:
            result1.insert( 16, 'Sub-District Description:')
    
        if 'Family Number' not in result1[17]:
            result1.insert( 17, 'Family Number:')
                
        
        scraped_info = {}
        for i in range(len(result1)):
            scraped_info.update({i : result1[i]})
        
        print(scraped_info)
       
        return scraped_info
