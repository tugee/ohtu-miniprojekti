*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  tolkien100 Tolkien22
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  tolkien Tolkien22
    Output Should Contain  error