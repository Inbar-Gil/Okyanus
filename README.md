# ___Okyanus___ # Search Engine

### Project Description
_insert description here_


### *Modules*

##### API - Code Functionality API from query to result
  - [API.py](.API/API.py) - Site Functionality API from query to result.  
  - -    QueryType class - detects if query is an Email Address/IP Address/Phone number/Username and formats accordingly. Returns if the query is legal and its format.  
      Each QueryType type object has a "query" propery (contains the query that the user inputs), a boolean "state" propery (depending if the query is legal or not) and a "data" property (a list that contains the query's format)  

  - -  Site class - returns the responses for the query from the sites , based on the query's type.  
  Each Site type object has a "data" property (a list that contains the query type and format) and a "response" property (contains the responses received from the sites).
  - -  TypeSearch class - determines the sites that will be used (according to the query's type), and can return a response from a single site or from all sites.  
  Each TypeSearch type object has a "data" property (a list that contains the query type and format), a "sites" property (a list that contains the sites that will be used, depending on the query's type) and a "responses" property (a list that contains the response/s generated for the query)
  - -  Response class - returns an "error response" message or "no response" message if needed.  
  Each Response type object contains a "query" property (contains the query that the user inputs).
       

- [Responses](API/Responses.py) - Response Classes for Output use



  
QueryID.py - RegEx query analyzer  
SiteSearch.py - Automatically searches different Sites  
Server.py - Django API to contact server  
README.md  
