![Header](https://thumbs.gfycat.com/AromaticMemorableAnemonecrab-max-1mb.gif)

# Django_Flashcards:nerd_face:
[![Flutter](https://img.shields.io/badge/-Link_to_this_app_on_heroku-000000?style=for-the-badge&)](https://webgame198890201.herokuapp.com/)

## *Languages and tools*

![](https://img.shields.io/static/v1?label=&message=PYTHON&color=black&style=for-the-badge&logo=python&logoColor=yellow)
![](https://img.shields.io/static/v1?label=&message=DJANGO&color=black&style=for-the-badge&logo=Django&logoColor=green)
![](https://img.shields.io/static/v1?label=&message=PosgreSQL&color=black&style=for-the-badge&logo=Postgresql&logoColor=3399ff)
![](https://img.shields.io/static/v1?label=&message=SQLITE&color=black&style=for-the-badge&logo=SQLITE&logoColor=red)
![](https://img.shields.io/static/v1?label=&message=Docker&color=black&style=for-the-badge&logo=Docker)

>APP INFO
> >This app is designed for learning foreign languages in a playful way. Its logic is simple, you need to create a card in one of the 5 boxes. This card must have a question and an answer. You can create as many cards as you want, depending on the difficulty.
Then you start the game. You are randomly assigned a card from the box you choose. If you give the right answer, then the card goes to the next box. Thus you should send all cards to the 5th box. If the answer is wrong, the card goes back to the beginning.
___
## Technical points
>Creating a manger to create Custom User
>>*This code performs the function of redefining fields for User, for Name email and password, in my case.*
```python
from django.contrib.auth.base_user import BaseUserManager 
from django.contrib.auth.hashers import make_password

class CardUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)
```
___
>Logic that allows you to shuffle the cards
>>*If the variable solved is True, then 1 is added to the box number. If the result is not in the range or ansver False , then it is reset to the first box.*
```python
def move(self, solved):
    new_box = self.box + 1 if solved and self.box + 1 <= 5 else BOXES[0]

    self.box = new_box
    self.save()
    
    return self
```
___
## Tests
![](C:/Users/Vova/Desktop/win.png)