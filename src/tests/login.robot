*** Settings ***
Resource  resource.robot
Test Setup  Register With Username And Password

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  tolkien Tolkien22
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  tolkien Tolkien
    Output Should Contain  error

Login With Nonexistent Username
    Input Credentials  tkien Tolkien22
    Output Should Contain  error

*** Keywords ***
Register With Username And Password
    Create User  tolkien Tolkien22
    Input Login Command