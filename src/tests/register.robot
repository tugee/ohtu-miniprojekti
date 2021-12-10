*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
#Register With Valid Credentials
#    Set Username  tolkientest
#    Set Password  tolkientest
#    Submit Credentials
#    Register Should Succeed
#Käyttäjä pitää pystyä poistamaan, jotta tämä mahdollista testata joka kerta

*** Keywords ***
Register Should Succeed
    Login Page Should Be Open
