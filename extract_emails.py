import re

list_of_emails = re.findall('\S+@\S+', "Witaj, proszę skontaktować się ze mną pod adresem email: john.doe@example.com. Możesz też napisać na adres support@company.pl. Oto jeszcze jeden adres: alice_smith123@gmail.com. Dziękuję!")
print(list_of_emails)