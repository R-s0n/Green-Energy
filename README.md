# Green Energy

This tool is designed to scan either a single URL or list of URLs for Prototype Pollution

Methodology based on Tomnomnom's Video from NahamCon2021 found [Here](https://www.youtube.com/watch?v=Gv1nK6Wj8qM)  
For ideas to exploit and build impact, [read this article by Portswigger](https://portswigger.net/daily-swig/prototype-pollution-the-dangerous-and-underrated-vulnerability-impacting-javascript-applications)  

******************************************************************************************************
             I AM NOT RESPONSABLE FOR HOW YOU USE THIS TOOL.  DON'T BE A DICK!                     
******************************************************************************************************

### Install

    python3 install.py
    
### Usage

##### Single URL
            python3 greenenergy.py [-h] [-u | --url] [URL] [-v | --verbose]
                Example: python3 greenenergy.py -u "http://example.com"

##### URL List
            python3 greenenergy.py [-h] [-uL | --ulist] [FILE] [-v | --verbose]
                Example: python3 greenenergy.py -ul /tmp/url-list.txt -v
------------------------------------------------------------------------------------------------------
|  Short  |    Long    |  Required  |                               Notes                             |
|---------|------------|------------|-----------------------------------------------------------------|
|   -u    |  --url     |     no     |                         Scan a single URL                       |
|   -uL   |  --ulist   |     no     |                   Scan a list of URLs from a file               |
|   -v    |  --verbose |     no     |                       Include verbose output                    |
-------------------------------------------------------------------------------------------------------
