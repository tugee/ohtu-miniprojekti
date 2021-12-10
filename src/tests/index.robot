*** Settings ***
Resource  resource.robot
Resource  login.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Variables ***
${NEWVINKKI}  http://${SERVER}/uusivinkki
${LOGOUT}  http://${SERVER}/logout

*** Test Cases ***
Page Has Correct Text
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

*** Keywords ***
Execute Login
    Go To Login Page
    Set Username  Jonsku
    Set Password  8F6CwIE4
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
    Set Url  linkki
    Submit Credentials

Execute Logout
    Go To  ${LOGOUT}