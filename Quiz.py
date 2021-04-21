#Geography Quiz
#Final Project
#Adam Fire
#5/11/2020
print("Hello friend, welcome to the ultimate world capitals quiz!")
print("For this quiz, you will need knowledge of country capitals with perfect spelling.")
print("Make sure to include correct punctuation like periods and dashes when applicable. No accents will be necessary.")
#Score increments
def fun1():
    global score
    score=score+1

def fun2():
    global score
    score = score + 2

def fun3():
    global score
    score=score+3

#question function
def main():
    global score
    score=0
    def question(count,cap,hint1):
        global score
        ans=input("What is the capital of "+ count+"? ").lower()
        if ans != cap:
            print("Incorrect")
            print("Hint 1: ", hint1)
            ans2 = input("What is the capital of "+ count+"? ").lower()
            if ans2 != cap:
                print("Incorrect")
                print("Hint 2: The capital begins with the letter:", cap[0])
                ans3 = input("What is the capital of "+ count+ "? ").lower()
                if ans3 != cap:
                    print("Incorrect, you receive zero points for this question.")
                else:
                    print("Correct!")
                    fun1()
                    print("+1 point")
            else:
                print("Correct!")
                fun2()
                print("+2 points")
        else:
            print("Correct!")
            fun3()
            print("+3 points")

    #countries with two capitals
    def question2caps(count,cap1,cap2,hint1):
        global score
        ans=input("What is one of the capitals of "+ count+"? ").lower()
        if ans != cap1 and ans != cap2:
            print("Incorrect")
            print("Hint 1: ", hint1)
            ans2 = input("What is one of the capitals of "+ count+"? ").lower()
            if ans2 != cap1 and ans2 != cap2:
                print("Incorrect")
                print("Hint 2: One of the capitals begins with the letter:", cap1[0])
                ans3 = input("What is one of the capitals of "+ count+ "? ").lower()
                if ans3 != cap1 and ans3 != cap2:
                    print("Incorrect, you receive zero points for this question.")
                else:
                    print("Correct!")
                    fun1()
                    print("+1 point")
            else:
                print("Correct!")
                fun2()
                print("+2 points")
        else:
            print("Correct!")
            fun3()
            print("+3 points")

     #countries with three capitals
    def question3caps(count, cap1, cap2, cap3, hint1):
        global score
        ans = input("What is one of the capitals of " + count + "? ").lower()
        if ans != cap1 and ans != cap2 and ans != cap3:
            print("Incorrect")
            print("Hint 1: ", hint1)
            ans2 = input("What is one of the capitals of " + count + "? ").lower()
            if ans2 != cap1 and ans2 != cap2 and ans2 != cap3:
                print("Incorrect")
                print("Hint 2: One of the capitals begins with the letter:", cap1[0])
                ans3 = input("What is one of the capitals of " + count + "? ").lower()
                if ans3 != cap1 and ans3 != cap2 and ans3 != cap3:
                    print("Incorrect, you receive zero points for this question.")
                else:
                    print("Correct!")
                    fun1()
                    print("+1 point")
            else:
                print("Correct!")
                fun2()
                print("+2 points")
        else:
            print("Correct!")
            fun3()
            print("+3 points")

    import random
    continent=eval(input("To Begin, Pick a continent : Press 1 for Europe, 2 for North America, 3 for South America, 4 for Asia, 5 for Africa, and 6 for Australia/Oceania: "))
    #Make sure input is valid
    while continent != 1 and continent != 2 and continent != 3 and continent != 4 and continent != 5 and continent != 6:
        print("Error: Please enter a valid number")
        continent = eval(input("Press 1 for Europe, 2 for North America, 3 for South America, 4 for Asia, 5 for Africa, and 6 for Australia/Oceania: "))
    #if statement for the actual quiz and for keeping score
    if continent == 1:
        print("You have chosen Europe")
        eur = [("France", "paris", "Eiffel Tower"),
               ("United Kingdom", "london", "Big Ben"),
               ("Italy", "rome", "The Colosseum is here"),
               ("Albania", "tirana", "Skanderbeg Square"),
               ("Andorra", "andorra la vella", "Skiing resorts"),
               ("Austria", "vienna", "Palaces"),
               ("Belarus", "minsk", "SvislaÄ and the Nyamiha Rivers"),
               ("Belgium", "brussels", "Vegetable"),
               ("Bosnia and Herzegovina", "sarajevo", "Miljacka River"),
               ("Bulgaria", "sofia", "Girl's name"),
               ("Croatia", "zagreb", " St. Markâ€™s Church"),
               ("Czech Republic", "prague", "the City of a Hundred Spires"),
               ("Denmark", "copenhagen", "Colorful houses"),
               ("Estonia", "tallinn", "Enemies in Overwatch"),
               ("Finland", "helsinki", "Baltic Herring Fair"),
               ("Germany", "berlin", "Wall"),
               ("Hungary", "budapest", "Bisected by the River Danube"),
               ("Iceland", "reykjavik", " geothermal Blue Lagoon spa"),
               ("Ireland", "dublin", "famous castle"),
               ("Kosovo", "pristina", "large Albanian population"),
               ("Latvia", "riga", "old town"),
               ("Liechtenstein", "vaduz", "Rhine River"),
               ("Luxembourg", "luxembourg", "Same"),
               ("Malta", "valletta", "tiny"),
               ("Moldova", "chisinau", "Triumphal Arch"),
               ("Monaco", "monaco", "Same"),
               ("Montenegro", "podgorica", "Millennium Bridge"),
               ("Netherlands", "amsterdam", "Canals"),
               ("North Macedonia", "skopje", "Kale Fortress"),
               ("Norway", "oslo", "Viking Ship Museum"),
               ("Poland", "warsaw", "Old town"),
               ("Portugal", "lisbon", "beaches"),
               ("Romania", "bucharest", "Palatul Parlamentului government building"),
               ("Russia", "moscow", "Kremlin"),
               ("San Marino", "san marino", "Same"),
               ("Serbia", "belgrade", "Beogradska TvrÄ‘ava"),
               ("Slovakia", "bratislava", "Borders 2 other countries"),
               ("Slovenia", "ljubljana", "Museum of Modern Art"),
               ("Spain", "madrid", "portico-lined Plaza Mayor"),
               ("Sweden", "stockholm", "14 islands"),
               ("Switzerland", "bern", "fire"),
               ("Ukraine", "kiev", "Dnieper River"),
               ("Vatican City", "vatican city", "Same")]
        random.shuffle(eur)
        for i in eur:
            question(i[0], i[1], i[2])
        score=(score/(3*len(eur))) * 100
        print("Your score is",round(score,2),"%")
    elif continent ==2:
        print("You have chosen North America")
        na = [("Antigua and Barbuda", "saint john's", "Key port of the island"),
              ("Bahamas", "nassau", "Sounds similar to a famous space agency"),
              ("Barbados", "bridgetown", "17th century garrison"),
              ("Belize", "belmopan", "Near Mountain Pine Forest Reserve"),
              ("Canada", "ottawa", "In Ontario"),
              ("Costa Rica", "san jose", "the capital of the province of the same name"),
              ("Cuba", "havana", "popular song name"),
              ("Dominica", "roseau", "Southwest coast"),
              ("Dominican Republic", "santo domingo", "1st cathedral built in the new world"),
              ("El Salvador", "san salvador", "Founded by Pedro de Alvarado"),
              ("Grenada", "saint george's", "Fort Matthew"),
              ("Guatemala", "guatemala city", "near Pacaya Volcano"),
              ("Haiti", "port-au-prince", "Notre Dame de l'Assomption Cathedral"),
              ("Hondura", "tegucigalpa", "valley"),
              ("Jamaica", "kingston", "Bob Marley"),
              ("Mexico", "mexico city", "Aztec Temple"),
              ("Nicaragua", "managua", "Plaza of the Revolution"),
              ("Panama", "panama city", "pretty important canal"),
              ("St. Kitts & Nevis", "basseterre", "Independence Square"),
              ("St. Lucia", "castries", "Vigie Beach"),
              ("St. Vincent & the Grenadines", "kingstown", " Botanical Gardens"),
              ("Trinidad & Tobago", "port-of-spain", "carnival"),
              ("United States", "washington d.c.", "Pentagon"),]
        random.shuffle(na)
        for i in na:
            question(i[0], i[1], i[2])
        score = (score / (3*len(na))) * 100
        print("Your score is", round(score,2), "%")
    elif continent ==3:
        print("You have chosen South America")
        sa = [("Argentina", "buenos aires", "Plaza de Mayo"),
              ("Brazil", "brasilia", "Became the capital 60 years ago"),
              ("Chile", "santiago", "Impractical Jokers running gag"),
              ("Colombia", "bogota", "high altitude"),
              ("Ecuador", "quito", "ancient Incan city"),
              ("Guyana", "georgetown", "coast"),
              ("Paraguay", "asuncion", "grand LÃ³pez Palace"),
              ("Peru", "lima", "arid Pacific coast"),
              ("Suriname", "paramaribo", "Dutch colonial buildings"),
              ("Uruguay", "montevideo", "Plaza de la Independencia"),
              ("Venezuela", "caracas", "twin towers"),]
        sa2 = [("Bolivia", "sucre", "la paz", "What's sugar in another language?")]
        random.shuffle(sa)
        for i in sa:
            question(i[0], i[1], i[2])
        for j in sa2:
            question2caps(j[0], j[1], j[2], j[3])
        score = (score / ((3*len(sa))+3)) * 100
        print("Your score is", round(score,2), "%")
    elif continent ==4:
        print("You have chosen Asia")
        asia = [("Afghanistan", "kabul", "Sounds like a Mortal Kombat character"),
                ("Armenia", "yerevan", "Republic Square"),
                ("Azerbaijan", "baku", "Flame Towers"),
                ("Bahrain", "manama", "ancient Dilmun civilization"),
                ("Bangladesh", "dhaka", "Extraction"),
                ("Bhutan", "thimphu", "Tashichho Dzong"),
                ("Brunei", "bandar seri begawan", "Sultan Omar Ali Saifuddien Mosque"),
                ("Cambodia", "phnom penh", "junction of the Mekong and TonlÃ© Sap rivers"),
                ("China", "beijing", "Nope, not Shanghai"),
                ("Cyprus", "nicosia", "also known as Lefkosia"),
                ("Timor-Leste", "dili", "Cristo Rei de Dili statue"),
                ("Georgia", "tbilisi", "Narikala"),
                ("India", "new delhi", "humayun's tomb"),
                ("Indonesia", "jakarta", "On Java"),
                ("Iran", "tehran", "National Jewelry Museum"),
                ("Iraq", "baghdad", "Tigris River"),
                ("Israel", "jerusalem", "Wailing Wall"),
                ("Japan", "tokyo", "2020 Olympics"),
                ("Jordan", "amman", "Roman Temple of Hercules"),
                ("Kazakhstan", "nur-sultan", "Used to be called Astana"),
                ("Kuwait", "kuwait city", "Grand Mosque"),
                ("Kyrgyzstan", "bishkek", "Ala Archa National Park"),
                ("Laos", "vientiane", "Pha That Luang"),
                ("Lebanon", "beirut", "the Paris of the Middle East"),
                ("Malaysia", "kuala lumpur", "Petronas Twin Towers"),
                ("Maldives", "male", "Islamic Centre"),
                ("Mongolia", "ulaanbaatar", "Tuul River valley"),
                ("Myanmar", "naypyidaw", ""),
                ("Nepal", "kathmandu", "Doctor Strange"),
                ("North Korea", "pyongyang", "The Interview"),
                ("Oman", "muscat", "The golden stupa of Uppatasanti Pagoda"),
                ("Pakistan", "islamabad", "high standards of living"),
                ("Philippines", "manila", "Intramuros"),
                ("Qatar", "doha", "National Library"),
                ("Saudi Arabia", "riyadh", "largest city on the Arabian Peninsula"),
                ("Singapore", "singapore", "Same"),
                ("South Korea", "seoul", "High-tech subways"),
                ("Syria", "damascus", "City of Jasmine"),
                ("Taiwan", "taipei", "bamboo-shaped skyscraper"),
                ("Tajikistan", "dushanbe", "Varzob River"),
                ("Thailand", "bangkok", "Most visited city in the world"),
                ("Turkey", "ankara", "You're wrong, it's not Istanbul"),
                ("Turkmenistan", "ashgabat", " Turkmen Carpet Museum"),
                ("United Arab Emirates", "abu dhabi", "shopping megacenters and oil exports"),
                ("Uzbekistan", "tashkent", "Amir Timur Museum"),
                ("Vietnam", "hanoi", "Bach Ma"),
                ("Yemen", "sana'a", "It has an apostrophe")]
        asia2 = [("Sri Lanka", "sri jayawardenepura kotte", "colombo","One of the capitals has a long name")]
        random.shuffle(asia)
        for i in asia:
            question(i[0], i[1], i[2])
        for j in asia2:
            question2caps(j[0], j[1], j[2], j[3])
        score = (score / ((3 * len(asia)) + 3)) * 100
        print("Your score is", round(score,2), "%")
    elif continent ==5:
        print("You have chosen Africa")
        af = [("Algeria", "algiers", "Sounds like the country name"),
              ("Angola", "luanda", "West coast"),
              ("Botswana", "gaborone", "Large game reserve"),
              ("Burkina Faso", "ouagadougou", "funny name"),
              ("Burundi", "gitega", "formerly Kitega"),
              ("Cameroon", "yaounde", "Mvog-Betsi Zoo"),
              ("Cape Verde", "praia", "southern coast of Santiago Island"),
              ("Central African Republic", "bangui", "the most remote radio station in Africa"),
              ("Chad", "n'djamena", "Chari River"),
              ("Comoros", "moroni", "Old Friday Mosque"),
              ("Democratic Republic of Congo", "kinshasa", "Congo River"),
              ("Republic of Congo", "brazzaville", "near Kinshasa"),
              ("Djibouti", "djibouti", "Same"),
              ("Egypt", "cairo", "Pyramid of Giza is nearby"),
              ("Equatorial Guinea", "malabo", "Bioko island"),
              ("Eritrea", "asmara", "high altitude"),
              ("Ethiopia", "addis ababa", "airplane-shaped Fiat Tagliero service station"),
              ("Gabon", "libreville", "Synonamous to free town"),
              ("Gambia", "banjul", "Albert Market"),
              ("Ghana", "accra", "Kwame Nkrumah Memorial Park"),
              ("Guinea", "conakry", "Loos Islands nearby"),
              ("Guinea-Bissau", "bissau", "half of the country name"),
              ("Ivory Coast", "yamoussoukro", "enormous basilica"),
              ("Kenya", "nairobi", "elephant orphanage"),
              ("Lesotho", "maseru", "cone-shaped Basotho Hat"),
              ("Liberia", "monrovia", "American president"),
              ("Libya", "tripoli", "3 of something"),
              ("Madagascar", "antananarivo", "wooden houses and royal tombs"),
              ("Malawi", "lilongwe", "Wildlife Centre"),
              ("Mali", "bamako", "Niger River"),
              ("Mauritania", "nouakchott", "sounds like a sneeze"),
              ("Mauritius", "port louis", "horse-racing track"),
              ("Morocco", "rabat", "Hassan Tower"),
              ("Mozambique", "maputo", "Baixa"),
              ("Namibia", "windhoek", "Heroesâ€™ Acre war memorial"),
              ("Niger", "niamey", "Niger River"),
              ("Nigeria", "abuja", "monolith"),
              ("Rwanda", "kigali", "Caplaki Crafts Village"),
              ("SÃ£o TomÃ© & Principe", "sao tome", "Part of country name"),
              ("Senegal", "dakar", "Cap-Vert peninsula"),
              ("Seychelles", "victoria", "Girl's name"),
              ("Sierra Leone", "freetown", "symbol of emancipation"),
              ("Somalia", "mogadishu", " important port"),
              ("South Sudan", "juba", "White Nile"),
              ("Sudan", "khartoum", "population of 5,274,321"),
              ("Tanzania", "dodoma", "pending complete transfer of official functions from Dar es Salaam"),
              ("Togo", "lome", "Palm Trees"),
              ("Tunisia", "tunis", "Similar to counrty name"),
              ("Uganda", "kampala", "red-tile villas"),
              ("Zambia", "lusaka", "Munda Wanga Environmental Park nearby"),
              ("Zimbabwe", "harare", "Sounds like someone laughing")]
        af2 = [("Eswatini", "mbabane", "lobamba", "Hhohho Region")]
        af3 = [("South Africa", "cape town", "pretoria", "bloemfontein", "None of the 3 capitals are Johannesburg")]
        random.shuffle(af)
        for i in af:
            question(i[0], i[1], i[2])
        for j in af2:
            question2caps(j[0], j[1], j[2], j[3])
        for k in af3:
            question3caps(k[0], k[1], k[2], k[3], k[4])
        score = (score / ((3 * len(af)) + 6)) * 100
        print("Your score is", round(score,2), "%")
    elif continent ==6:
        print("Australia/Oceania")
        aus=[("Australia", "canberra", "No, it's not Sydney or Melbourne"),
             ("Fiji", "suva", "British colonial buildings"),
             ("Kiribati", "south tarawa", "It has half of the country's population"),
             ("Marshall Islands", "majuro", "also a large coral atoll of 64 islands"),
             ("Micronesia", "palikir", "under 5,000 residents"),
             ("Nauru", "yaren", "original name was Makwa"),
             ("New Zealand", "wellington", "Cook Strait"),
             ("Palau", "ngerulmud", "hard to pronounce"),
             ("Papua New Guinea", "port moresby", "Paga Hill"),
             ("Samoa", "apia", "Palolo Deep Marine Reserve"),
             ("Solomon Islands", "honiara", "Mataniko Falls"),
             ("Tonga", "nuku'alofa", "island of Tongatapu"),
             ("Tuvalu", "funafuti", "narrow sweep of land encircling a lagoon"),
             ("Vanuatu", "port vila", "Efate island")]
        random.shuffle(aus)
        for i in aus:
            question(i[0], i[1], i[2])
        score = (score / (3*len(aus))) * 100
        print("Your score is", round(score,2), "%")

    #Say something witty based on the user's score
    if score < 20:
        print("Your lack of knowledge concerns me.")
    elif score >= 20 and score < 40:
        print("You've got quite a bit of room to improve there champ.")
    elif score >= 40 and score < 60:
        print("Eh, at least you're trying.")
    elif score >= 60 and score < 80:
        print("Good job, you didn't fail.")
    elif score >= 80 and score < 99.99:
        print("Very well done, you know your capitals alright!")
    elif score == 100:
        print("You are a truly flawless human being, bravo!")
    global again
    again = input("Would you like to take another quiz? ").lower()
main()
#Repeat quiz if user wants to play again
global again
while again[0]=="y":
    main()
input("Thanks for playing! Press the enter key to quit.")