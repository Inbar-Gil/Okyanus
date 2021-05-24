# ___Okyanus___ # Search Engine

### Project Description

_insert description here_

### *Modules*

##### API - Code Functionality API from query to result

- [API.py](.API/API.py) - Site Functionality API from query to result.
-
    - QueryType class - detects if query is an Email Address/IP Address/Phone number/Username and formats accordingly.
      Returns if the query is legal and its format.  
      Each QueryType type object has a "query" property (a string that contains the query that the user inputs), a
      boolean "state" property (that is changed from False to True if the query is legal), and a "data" property (a list
      that contains the query's format).

-
    - Site class - returns the responses for the query from the sites , based on the query's type.  
      Each Site type object has a "data" property (a list that contains the query type and format), and a "response"
      property (a string that contains the responses received from the sites).
-
    - TypeSearch class - determines the sites that will be used (according to the query's type), and can return a
      response from a single site or from all sites.  
      Each TypeSearch type object has a "data" property (a list that contains the query type and format), a "sites"
      property (a list that contains the sites that will be used, depending on the query's type), and a "responses"
      property (a list that contains the response/s generated for the query).
-
    - Response class - returns an "error response" message or "no response" message if needed.  
      Each Response type object contains a "query" property (a string that contains the query that the user inputs).


- [Responses](API/Responses.py) - Response Classes for Output use
-
    - ErrorResponse class - each ErrorResponse type object contains a "
      query" property (a string that contains the query that the user inputs), an "exception" property (a string that contains the type of error that occured), and a "message" property (a string that contains the error message).

-
    - NoResponse class - each NoResponse type object contains a "query" property (a string that contains the query that the user inputs),
      an "queryType" property (a string that contains the type of data of the query), and a "siteList" property(a list that contains the sites that were used while the
      program was running).

##### Input - QueryType classes for legality checking and formatting from query input.
- EMail class - checks if the query is an email address, if its legal or not (raises a ValueError accordingly), and formats accordingly ([PREFIX, DOMAIN, ENDING]).

- IPAddress class - checks if the query is an IP address, decides its type, if its legal or not (raises a ValueError accordingly), and formats accordingly ([IP_TYPE, IP_ADDRESS]).

- PhoneNumber class - checks if the query is a phone number, decides its type, and formats accordingly ([PHONE TYPE, (PREFIXES), DIGITS]).

- Username class - checks if the query is a username, decides if its legal or not (raises a ValueError accordingly), and formats accordingly (splits the string into a list containg every substring between the symbols '.' , ' ,' , '-' , '_').

- RegExAnalyser class - uses the all of the classes in the Input folder to get a query and decide its type (from the types named above), decides if its legal or not, and formats accordingly

##### Output - Site classes for generating responses for queries.
- 


QueryID.py - RegEx query analyzer  
SiteSearch.py - Automatically searches different Sites  
Server.py - Django API to contact server  
README.md  
