*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page
Test Teardown  Execute Logout

*** Variables ***
${NEWVINKKI}  http://${SERVER}/uusivinkki
${LOGOUT}  http://${SERVER}/logout

*** Test Cases ***
Main Page Has Correct Text
    Page Should Contain  Lukuvinkkikirjasto

Lukuvinkkis Are Listed Correctly When Logged In 
    Execute Login
    Add New Vinkki
    Go To Main Page
    Page Should Contain  vinkinnimi

Lukuvinkkis Are Listed Correctly When Logged Out 
    Execute Login
    Add New Vinkki
    Go To Main Page
    Execute Logout
    Go To Main Page
    Page Should Contain  vinkinnimi

#Lukuvinkki Link Works
#    Execute Login
#    Add New Vinkki
#    Go To Main Page
#    Click Link  Taru sormusten herrasta
#    Title Should Be  Taru sormusten herrasta – Wikipedia
#Tarvitsee hyperlinkin otsikoksi

*** Keywords ***
Execute Login
    Go To Login Page
    Set Username  tolkien123
    Set Password  tolkien123
    Submit Credentials

Set Nimi
    [Arguments]  ${nimi}
    Input Text  nimi  ${nimi}

Set Url
    [Arguments]  ${url}
    Input Text  url  ${url}

Go to New Vinkki Page
    Go To  ${NEWVINKKI}

Add New Vinkki
    Go To New Vinkki Page
    Set Nimi  vinkinnimi
    Set Url  https://fi.wikipedia.org/wiki/Taru_sormusten_herrasta
    Submit Credentials

Execute Logout
    Go To  ${LOGOUT}