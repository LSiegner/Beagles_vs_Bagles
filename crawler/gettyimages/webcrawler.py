# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' 
This crawler uses the getty images API and code examples from the github page
to find the suitable images used later in training and testing

github page:
https://github.com/gettyimages/gettyimages-api/tree/main
with their respective authors    

'''


import requests
import json


class creative_image_list:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret= api_secret 

    def _search_for_creative_images(phrase, orientations, number_of_people, oauth):
        """Search for creative images given a search phrase and some filters"""
        url = "https://api.gettyimages.com/v3/search/images/creative"
        query_params = {"phrase": phrase, "orientations": orientations, "number_of_people": number_of_people}  
        headers = {
            "Api-Key": oauth["api_key"],
            "Authorization": f"Bearer {oauth['access_token']}"
        }
        response = requests.get(url, params=query_params, headers=headers)
        return response

    def _get_client_credentials_token(self):
        """Get an access token using client credentials grant"""
        url = "https://api.gettyimages.com/v4/oauth2/token"
        payload = f"grant_type=client_credentials&client_id={self.api_key}&client_secret={self.api_secret}"
        headers = {"content-type": "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers)
        oauth = json.loads(response.content)
        return oauth

    def get_bagles(self,number_of_people):
        '''searches getty images to find all the pictures given they are tagged with bagles
        and saves them as a txt file for later use, to minimize duplicates
        '''
        oauth = self._get_client_credentials_token(self.api_key,self.api_secret)
        oauth["api_key"] = self.api_key
        search_response_bagles = self._search_for_creative_images("bagles", "square,vertical", number_of_people, oauth)
        
        with open("search_bagles.txt", "w") as output:
            output.write(search_response_bagles.txt)
            output.close()
            
        with open("search_keywords_bagles.txt", "w") as output:
            output.write("beagle, number_of_people \n")
            output.write(f"0,{number_of_people}")
            output.close()
                 
        
    def get_beagles(self, number_of_people):
        '''searches getty images to find all the pictures given they are tagged with beagles
        and saves them as a txt file for later use, to minimize duplicates
        '''
        oauth = self._get_client_credentials_token(self.api_key,self.api_secret)
        oauth["api_key"] = self.api_key
        search_response_beagles = self._search_for_creative_images("beagles", "square,vertical", number_of_people, oauth)
        
    
        with open("search_beagles.txt","w") as output:
            output.write(search_response_beagles.txt)
        
        with open("search_keywords_bagles.txt", "w") as output:
            output.write("beagle, number_of_people \n")
            output.write(f"1,{number_of_people}")
            output.close()
            

'''
oauth = get_client_credentials_token(api_key, api_secret)
oauth["api_key"] = api_key
search_response = search_for_creative_images("office workers", "square,vertical", 3, oauth)
print(search_response.text)
'''

        
        
        
        
    



