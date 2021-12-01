*** Settings ***


*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application