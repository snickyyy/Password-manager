# Password manager
___
##  **Reception:**
### My app is an easy way to store passwords securely. It also has a beautiful and clear interface.

___
## **Functional:**
* **create record**
    * creating a record
    * Generating a strong password
    * Password verification

* **get record**
    * get password
    * copy password

* **update password**
    * replace password
    * delete password
    * checking new password
___
## What are the advantages of my application 
* **data security**
    * all passwords are encrypted before being sent to the database
    * authorization system
* **beautiful design**
* **simplicity of the interface**
* **ease of use**
* **few settings before use**
#### and many others
___
## Before use
### Before use, you must register an account in the database, this can be done through a script in the "creatorAccount" file, or through an application in the archive with the same name. 

___
## Button info
### in order to configure the information button (in the upper left corner) you need to find the method in the design file in class "Ui_MainWindow": 
``` python
    def openTG(self):
        """Method for opening a link using a button"""
        TgInfo_url = QUrl('Enter link')
        QDesktopServices.openUrl(TgInfo_url)
```
### replace "Enter link" with your link
>Example: 
>> TgInfo_url = QUrl('Enter link') >>  TgInfo_url = QUrl('https://github.com/snickyyy')

### And now when you click on the information button you will be transferred to your link
____

## For use exe 
### Add an account to the database. To use the application as an exe file, you need to unzip the files from the archive into 1 folder and check the presence of all files in the "cfg" folder.

___
## Encryption key
### I took the computer's mixed hvid as the main encryption key

___
## Support
### found a mistake? you can send information about an error or bug to me, and I will personally review and help solve the problem.

[![Telegram](https://img.shields.io/badge/-telegram-black?style=for-the-badge&logo=telegram&logoColor=blue)](https://t.me/snickyyy)
[![discord](https://img.shields.io/badge/-discord-black?style=for-the-badge&logo=discord&logoColor=blue)](https://discordapp.com/users/994294160750293103/)
