# ___Okyanus___ # Search Engine

### Project Description

_insert description here_

### *Modules*

##### API - Code Functionality API from query to result

- [API.py](API/API.py) - Site Functionality API from query to result.
  

- - QueryType class - detects if query is an Email Address/IP Address/Phone number/Username and formats accordingly.
      Returns if the query is legal and its format.  
      Each QueryType type object has a "query" property (a string that contains the query that the user inputs), a
      boolean "state" property (that is changed from False to True if the query is legal), and a "data" property (a list
      that contains the query's format).


- - Site class - returns the responses for the query from the sites , based on the query's type.  
      Each Site type object has a "data" property (a list that contains the query type and format), and a "response"
      property (a string that contains the responses received from the sites).
    

- - TypeSearch class - determines the sites that will be used (according to the query's type), and can return a
      response from a single site or from all sites.  
      Each TypeSearch type object has a "data" property (a list that contains the query type and format), a "sites"
      property (a list that contains the sites that will be used, depending on the query's type), and a "responses"
      property (a list that contains the response/s generated for the query).
    

- - Response class - returns an "error response" message or "no response" message if needed.  
      Each Response type object contains a "query" property (a string that contains the query that the user inputs), and a "responseType" property (a string that contains the type of response recieved).


- [Responses](API/Responses.py) - Response Classes for Output use
  

- - ErrorResponse class - sends an error message to the user.  
      each ErrorResponse type object contains an "exception" property (a string that contains the type of error that occurred), and a "message" property (a string that contains the error message).


- - NoResponse class - sends a message to the user saying there were no responses for his query. 
      
      each NoResponse type object contains a "queryType" property (a string that contains the type of data of the query), and a "siteList" property(a list that contains the sites that were used while the
      program was running).
    

- - PhoneResponse class - sends a message to the user containing the name and address related to the inputted phone number 
      
      each PhoneResponse type object contains a "name" property, and an "address" property (two strings that contain the name and address related to the phone number, respectively).
    

- - IpResponse class - sends a message to the user containing all of the data that we recieved for the inputted IP address.
      
      each IpResponse type object contains the properties "hostname", "city", "region", "loc", "isp", "org", and "as_" (strings that contain the data mentioned in their names).
     

##### Input - QueryType classes for legality checking and formatting from query input.
- EMail class from [EMail.py](Input/EMail.py) - used to check if the query is an email address, if its legal or not (raises a ValueError accordingly), and format accordingly (\[PREFIX, DOMAIN, ENDING]).


- IPAddress class from [IPAddress.py](Input/IPAddress.py) - used to check if the query is an IP address, decide its type, if its legal or not (raises a ValueError accordingly), and format accordingly (\[IP_TYPE, IP_ADDRESS]).


- PhoneNumber class from [PhoneNumber.py](Input/PhoneNumber.py) - used to check if the query is a phone number, decide its type, and format accordingly (\[PHONE TYPE, (PREFIXES), DIGITS]).


- Username class from [Username.py](Input/Username.py) - used to check if the query is a username, decide if its legal or not (raises a ValueError accordingly), and format accordingly (splits the string into a list containing every substring between the symbols '.' , ' ,' , '-' , '_').


- RegExAnalyser class from [RegExAnalyser.py](Input/RegExAnalyzer.py) - uses all of the classes in the Input folder to get a query and decide its type (from the types named above), decides if its legal or not, and formats accordingly

##### Output - Site classes for generating responses for queries.
- [IPAddress.py](Output/IPAddress.py) - Generates responses for IP addresses
- - IPinfo class - makes a dictionary containing all of the data received for the IP address from the site ["IP Info"](https://ipinfo.io/) and puts it in a dictionary.
    
- - IPApi class - makes a dictionary containing all of the data received for the IP address from the site ["IP API"](https://ip-api.com/) and puts it in a dictionary.
    
- - searchIp function - uses the two classes and returns the combination of the two dictionaries.
    
    
- [PhoneNumber.py](Output/PhoneNumber.py) - Generates responses for home phone numbers
- - Phonenumber441 class - used to return the name and address related to the phone number by using the site ["441il"](https://441il.com/)
    
- - searchPhoneNumber function - uses the class above to return a dictionary with the name and address related to the phone number.
    

- SearchEngine class from [SiteSearch.py](Output/SiteSearch.py) - does not inherit from the Site class.

    Uses the above modules (and the 2 related Response classes) to get responses for IP addresses (of types IPv4 and IPv6) and home phone numbers and generate them on the Okyanus server.


