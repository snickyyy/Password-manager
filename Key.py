from random import randint, sample
import cryptocode
from wmi import WMI
import re

class Key:
    """
    Class for working with keys and passwords.
    """
    def getHwid(self):
        """
Gets the HWID (Hardware Identifier) ​​of the current device.

 Returns:
 str: HWID of the current device.
        """
        return WMI().Win32_ComputerSystemProduct()[0].UUID

    def password_checker(self, password):
        """
Checks the strength of the password.

 A password is considered strong if:
 - 8 characters length or more
 - 1 digit or more
 - 1 symbol or more
 - 1 uppercase letter or more
 - 1 lowercase letter or more

 Args:
 password (str): Password for verification.

 Returns:
 list: A list containing the result of the test and the criteria that were not met.
         """

        length_error = len(password) < 8

        digit_error = re.search(r"\d", password) is None

        uppercase_error = re.search(r"[A-Z]", password) is None

        lowercase_error = re.search(r"[a-z]", password) is None

        symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

        password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)

        return [password_ok, length_error, digit_error, uppercase_error, lowercase_error, symbol_error]


    def encryptHwid(self):
        """
Encrypts the HWID for use as a password encryption key.

 Returns:
 str: Encrypted HWID.
        """
        hwid = list(self.getHwid())
        pas = ""
        for i in range(0, 30):
            c = hwid[int(round((28 + len(hwid)) / len(hwid)))]
            pas += str(c)
            hwid.pop(0)
        return pas

    def encryptPass(self, str):
        """
Encrypts the given password using the encrypted HWID as the key.

 Args:
 str (str): Password for encryption.

 Returns:
 str: Encrypted password.
        """
        ke = Key.encryptHwid(self)
        return cryptocode.encrypt(str, ke)

    def decrypt(self, str):
        """
Decrypts the given password using the encrypted HWID as the key.

 Args:
 str(str): Encrypted password.

 Returns:
 str: Decrypted password.
        """
        ke = self.encryptHwid()
        return cryptocode.decrypt(str, ke)

    def generatePass(self):
        """
Generates a strong password of a given length (14 to 25 characters).

 Returns:
 str: Generated password.
        """
        pasLong = randint(14, 25)
        simbols = list('/NnQ~JjR%,bw&<;=g+TMVuWKZPEъX(k){@}sSaB>hL!G"d?^o[y:Ye*lzHvt_OU№xDiIq$F.cpA]r-m#f1234567890')
        pasNew = sample(simbols, pasLong)
        return "".join(set(list(pasNew)))


