*** Settings ***
Library	OperatingSystem
Library 	HelloWorldLib.py

*** Test Cases ***
Program output is correct
	HelloWorldLib.Run
	Check	Hello World!

