*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Login With Correct Credentials
    Set Username  testikayttaja
    Set Password  testisalasana
    Submit Credentials
    Login Should Succeed

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Submit Credentials
    Click Button  submit

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
