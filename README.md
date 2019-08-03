# Repo: Device-Testing-PDF-Generator (Generic)
# Author: Connor Burk
# Description: My ever-so-cleverly named application, Device-Testing-PDF-Generator,
#               helped friends reduce redundancy in form-filing by 95%. By querying Django's ORM
#                 for data based on customer address and test date, it pre-populates 19 out of the 20 pages
#                   in the test document.

## Built with Python, Django and PostgreSQL

## Applications
1.  accounts
* Allowed for session-based authentication and restricted access to web application
2.  test_forms
* Where the magic happens
* Django's form wizard allows users to select an address (query ORM) and fill (insert) forms
