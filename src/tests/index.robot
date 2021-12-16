*** Settings ***
Resource  resource.robot
Suite Setup  Execute Setup
Suite Teardown  Close Browser
Test Setup  Go To Main Page
Test Teardown  Execute Logout

*** Variables ***
${NEWVINKKI}  http://${SERVER}/uusivinkki
${LOGOUT}  http://${SERVER}/logout

*** Test Cases ***
Main Page Has Correct Text
    Page Should Contain  Lukuvinkkikirjasto

Read Lukuvinkkis Are Not Visible On User Page
    Execute Login
    Add New Vinkki  Testi1  https://fi.wikipedia.org/
    Go To User Page
    Set Vinkki As Read
    Element Should Not Be Visible  Testi1

Read Lukuvinkkis Can Be Toggled On User Page
    Execute Login
    Go To User Page
    Click Element  vinkki_toggle
    Page Should Contain  Testi1

Lukuvinkkis Are Listed Correctly When Logged In 
    Execute Login
    Add New Vinkki  Testi2  https://fi.wikipedia.org/
    Go To Main Page
    Page Should Contain  Testi2

Lukuvinkkis Are Listed Correctly When Logged Out 
    Execute Login
    Add New Vinkki  Testi3  https://fi.wikipedia.org/
    Go To Main Page
    Execute Logout
    Go To Main Page
    Page Should Contain  Testi3

Lukuvinkki Link Works
    Execute Login
    Add New Vinkki  Taru sormusten herrasta  https://fi.wikipedia.org/wiki/Taru_sormusten_herrasta
    Go To Main Page
    Click Link  Taru sormusten herrasta
    Title Should Be  Taru sormusten herrasta – Wikipedia

*** Keywords ***
Execute Setup
    Open And Configure Browser
    Create User

Create User
    Go To Register Page
    Set Username  tolkien123
    Set Password  tolkien123
    Submit Credentials
    Login Page Should Be Open
    Go To Main Page

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
    [Arguments]  ${nimi}  ${url}
    Go To New Vinkki Page
    Set Nimi  ${nimi}
    Set Url  ${url}
    Submit Credentials

Set Vinkki As Read
    Go To User Page
    Click Link  Merkitse luetuksi

Execute Logout
    Go To  ${LOGOUT}