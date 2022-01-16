### 12-ci tapşırıq: 
# dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"} 
# Verilen dictionary-e esasen asgidaki suallari cavablandirmaq ucun ekrana sualin cavabiniz yazdirin. 
# Bunun ucun userden input alin. 
# Eger user “born”, “when” sozlerini daxil etse program texmin etsin ki user ne sorushmaq isteyir.
# Meselen born ve when sozleri varsa cumlede user cox guman ki “When was Plato born?” sualina cavab axtarir. 
# Proqram o sozleri gorub sorushsun ki, “Maybe did you mean “When was Plato born?” 
# “. Bu suali sorushduqda yes ve no secimleri verin. 
# Eger yes yazsa dictionarydeki datadan istifade ederek Platonun doguldugu ili usere gosterin.
# Meselen country daxil etse proqram texmin etsin ki user platonun doguldugu yeri axtarir ve siz de ele proqram yazin ki ona uygun cavab qaytarin. 
# Eger mentiqsiz soz daxil edilse not found verin ekrana.

dict={ "name": "Plato", 
       "country": "Ancient Greece", 
       "born": -427, 
       "teacher": "Socrates", 
       "student": "Aristotle"
       }
user  = input('sual ve cavab: ')

if user == ('born'):
    print(dict.get('born'))
else:
    print('not found')
if user == ("born when"):
    print('When was Plato born')
    print('Maybe did you mean “When was Plato born')
    cavab = input('yes or no: ')
    if cavab == ('yes'):
        print('Platonun doguldugu il:', dict.get('born'))
        
if user == ('country'):
    print("where was Plato born")
    print('Maybe did you mean “Where was Plato born')
    cavab = input('yes or no: ')
    if cavab == ('yes'):
        print('Plato doguldugu yer:',dict.get('country'))
