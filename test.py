from datetime import date

class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def age(self):
        # find the difference between today and the user's date of birth
        difference = date.today() - self.date_of_birth
        # timedelta object returned, does not have 'years' property so use days and a floor division to get age
        return difference.days // 365

    def next_birthday(self):
        # find the user's birthday for the current year
        bday = self.date_of_birth.replace(year=date.today().year)
        # check if they have had their birthday this year (or if it is today, which I am counting as current therfore next)
        if bday >= date.today():
            # if not, return that date
            return bday
        else:
            # if so, return their birthday next year
            return bday.replace(year=bday.year+1)



tests = [
    date(1986, 1, 1),
    date(1988, date.today().month, date.today().day),
    date(1998, 12, 30)
]

for date in tests:
    user = User("Test", date)
    print(f"{date} => {user.age()}")

for date in tests:
    user = User("Test", date)
    print(f"{date} => {user.next_birthday()}")