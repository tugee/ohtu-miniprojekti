*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/kirjautuminen

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  Lukuvinkkikirjasto

Login Page Should Be Open
    Title Should Be  Lukuvinkkikirjasto kirjautuminen

Go To Main Page
    Go To  ${HOME URL}

Go To Login Page
    Go To  ${LOGIN URL}
