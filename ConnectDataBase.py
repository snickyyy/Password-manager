from peewee import *
db = SqliteDatabase(r"cfg\EncryptionPassword.db")


class Tables:
    """Class describing models of tables from the database"""
    class Account(Model):
        """
'Account' table model containing user data.

 Attributes:
 AccountId (AutoField): Primary key.
 Login (CharField): User login, unique.
 Password (CharField): User password, unique.
 AccountHwid (CharField): User HWID, unique.
         """
        AccountId = AutoField(primary_key=True)
        Login = CharField(max_length=144, unique=True)
        Password = CharField(unique=True)
        AccountHwid = CharField(unique=True)

        def __str__(self):
            return f"{self.Password}"

        class Meta:
            database = db
            table_name = 'Account'

    class Passwords(Model):
        """
A model of the 'Passwords' table containing user data.

 Attributes:
 PasswordId (AutoField): Primary key.
 Sotnet (CharField): Cell network
 LoginSotNet (CharField): Login to the cell network
 Password (CharField): Password, unique.
         """
        PasswordId = AutoField(primary_key=True)
        Sotnet = CharField(max_length=144)
        LoginSotNet = CharField(max_length=144)
        Password = CharField(unique=True)

        def __str__(self):
            return f"{self.Password}"

        class Meta:
            database = db
            table_name = 'Passwords'


# Tables.Passwords.create_table()
# Tables.Account.create_table()


