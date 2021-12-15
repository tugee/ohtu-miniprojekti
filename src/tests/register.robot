*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Credentials
    Set Username  tolkientest
    Set Password  tolkientest
    Submit Credentials
    Register Should Succeed
    Execute Login
    Login Should Succeed

*** Keywords ***
Register Should Succeed
    Login Page Should Be Open

Execute Login
    Go To Login Page
    Set Username  tolkien123
    Set Password  tolkien123
    Submit Credentials

Login Should Succeed
    Main Page Should Be Open
