*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/kirjautuminen
${REGISTER URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  Lukuvinkkikirjasto

Login Page Should Be Open
    Title Should Be  Lukuvinkkikirjasto kirjautuminen

Register Page Should Be Open
    Title Should Be  Lukuvinkkikirjasto rekisteröityminen

Go To Main Page
    Go To  ${HOME URL}

Go To Login Page
    Go To  ${LOGIN URL}

Go To Register Page
    Go To  ${REGISTER URL}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Credentials
    Submit Form
