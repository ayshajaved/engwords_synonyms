#i will make a programm that will give you the synonym of the english hard word
# List of advanced English words and their synonyms
words_synonyms = [                                                 #a list with dictionaries
    {"English": "aberration", "Synonym": "anomaly"},
    {"English": "abhor", "Synonym": "detest"},
    {"English": "acquiesce", "Synonym": "comply"},
    {"English": "alacrity", "Synonym": "eagerness"},
    {"English": "amiable", "Synonym": "affable"},
    {"English": "appease", "Synonym": "placate"},
    {"English": "arcane", "Synonym": "esoteric"},
    {"English": "avarice", "Synonym": "greed"},
    {"English": "brazen", "Synonym": "audacious"},
    {"English": "brusque", "Synonym": "curt"},
    {"English": "cajole", "Synonym": "coax"},
    {"English": "callous", "Synonym": "heartless"},
    {"English": "candor", "Synonym": "frankness"},
    {"English": "chide", "Synonym": "scold"},
    {"English": "circumspect", "Synonym": "cautious"},
    {"English": "coerce", "Synonym": "force"},
    {"English": "complacency", "Synonym": "self-satisfaction"},
    {"English": "confidant", "Synonym": "trusted friend"},
    {"English": "connive", "Synonym": "conspire"},
    {"English": "cumulative", "Synonym": "accumulative"},
    {"English": "debase", "Synonym": "degrade"},
    {"English": "decry", "Synonym": "denounce"},
    {"English": "deferential", "Synonym": "respectful"},
    {"English": "demure", "Synonym": "modest"},
    {"English": "deride", "Synonym": "mock"},
    {"English": "despot", "Synonym": "tyrant"},
    {"English": "diligent", "Synonym": "industrious"},
    {"English": "elated", "Synonym": "overjoyed"},
    {"English": "eloquent", "Synonym": "articulate"},
    {"English": "embezzle", "Synonym": "misappropriate"},
    {"English": "empathy", "Synonym": "compassion"},
    {"English": "enmity", "Synonym": "hostility"},
    {"English": "erudite", "Synonym": "learned"},
    {"English": "extol", "Synonym": "praise"},
    {"English": "fabricate", "Synonym": "invent"},
    {"English": "feral", "Synonym": "wild"},
    {"English": "flabbergasted", "Synonym": "astonished"},
    {"English": "forsake", "Synonym": "abandon"},
    {"English": "fractious", "Synonym": "irritable"},
    {"English": "furtive", "Synonym": "secretive"},
    {"English": "gratuitous", "Synonym": "unwarranted"},
    {"English": "haughty", "Synonym": "arrogant"},
    {"English": "hypocrisy", "Synonym": "duplicity"},
    {"English": "impeccable", "Synonym": "flawless"},
    {"English": "impertinent", "Synonym": "rude"},
    {"English": "implacable", "Synonym": "unappeasable"},
    {"English": "impudent", "Synonym": "insolent"},
    {"English": "incisive", "Synonym": "keen"},
    {"English": "indolent", "Synonym": "lazy"},
    {"English": "inept", "Synonym": "incompetent"},
    {"English": "infamy", "Synonym": "notoriety"},
    {"English": "insatiable", "Synonym": "unquenchable"},
    {"English": "insular", "Synonym": "narrow-minded"},
    {"English": "intrepid", "Synonym": "fearless"},
    {"English": "inveterate", "Synonym": "habitual"},
    {"English": "jubilant", "Synonym": "overjoyed"},
    {"English": "knell", "Synonym": "toll"},
    {"English": "laconic", "Synonym": "terse"},
    {"English": "lament", "Synonym": "mourn"},
    {"English": "languid", "Synonym": "listless"},
    {"English": "latent", "Synonym": "hidden"},
    {"English": "legerdemain", "Synonym": "sleight of hand"},
    {"English": "lethargic", "Synonym": "sluggish"},
    {"English": "magnanimous", "Synonym": "generous"},
    {"English": "malevolent", "Synonym": "malicious"},
    {"English": "maverick", "Synonym": "nonconformist"},
    {"English": "meticulous", "Synonym": "careful"},
    {"English": "modicum", "Synonym": "small amount"},
    {"English": "morose", "Synonym": "sullen"},
    {"English": "myriad", "Synonym": "multitude"},
    {"English": "nadir", "Synonym": "lowest point"},
    {"English": "negligent", "Synonym": "careless"},
    {"English": "neophyte", "Synonym": "novice"},
    {"English": "obdurate", "Synonym": "stubborn"},
    {"English": "obfuscate", "Synonym": "confuse"},
    {"English": "oblivious", "Synonym": "unaware"},
    {"English": "obscure", "Synonym": "unclear"},
    {"English": "obsolete", "Synonym": "outdated"},
    {"English": "obstinate", "Synonym": "stubborn"},
    {"English": "omniscient", "Synonym": "all-knowing"},
    {"English": "onerous", "Synonym": "burdensome"},
    {"English": "opulent", "Synonym": "luxurious"},
    {"English": "ostensible", "Synonym": "apparent"},
    {"English": "ostracize", "Synonym": "exclude"},
    {"English": "panacea", "Synonym": "cure-all"},
    {"English": "paragon", "Synonym": "model"},
    {"English": "pariah", "Synonym": "outcast"},
    {"English": "partisan", "Synonym": "supporter"},
    {"English": "patent", "Synonym": "obvious"},
    {"English": "pejorative", "Synonym": "derogatory"},
    {"English": "penchant", "Synonym": "inclination"},
    {"English": "perfidious", "Synonym": "treacherous"},
    {"English": "perfunctory", "Synonym": "cursory"},
    {"English": "perspicacious", "Synonym": "shrewd"},
    {"English": "pertinacious", "Synonym": "persistent"},
    {"English": "phlegmatic", "Synonym": "calm"},
    {"English": "platitude", "Synonym": "cliché"},
    {"English": "plethora", "Synonym": "abundance"},
    {"English": "precocious", "Synonym": "advanced"},
    {"English": "predilection", "Synonym": "preference"},
    {"English": "proclivity", "Synonym": "tendency"}
]

# Print the words
print("-----------------------------------------------")
print("WELCOME TO THE ENGLISH WORDS LEARNING PROGRAMM")
print("-----------------------------------------------")
for word in words_synonyms:                                                  #printing all the english words
    print(word["English"])
while True:
    ch = input("Enter the word you want the synonym of!(\"exit\" to exit): ")
    if ch == "exit":                                                         #exiting
        print("Exiting from the program!")
        break
    found = False
    for words in words_synonyms:
        if ch == words["English"]:
            print(words["Synonym"])                                       
            found = True
            break
    if not found:                                                           #checking if the word is not in the list
        print("The word is not in the list!")
            

#this is the limited english dictionary with limited synonyms just a python learning short project
        
        

