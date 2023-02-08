
import spacy


#RUNNING CODE WITH EN_CORE_WEB_MD
print("***RUNNING CODE WITH EN_CORE_WEB_MD***")
nlp  = spacy.load('en_core_web_md')


tokens = nlp('cat apple monkey banana kiwi salt fish')
for token1 in tokens:

    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# OUTPUT
'''
cat cat 1.0
cat apple 0.2036806046962738    
cat monkey 0.5929930210113525   
cat banana 0.2235882580280304   
cat kiwi 0.15740658342838287    
cat salt 0.15873362123966217    
cat fish 0.319871723651886      
apple cat 0.2036806046962738    
apple apple 1.0
apple monkey 0.2342509925365448 
apple banana 0.6646699905395508 
apple kiwi 0.6305076479911804   
apple salt 0.35949474573135376  
apple fish 0.37951505184173584  
monkey cat 0.5929930210113525   
monkey apple 0.2342509925365448 
monkey monkey 1.0
monkey banana 0.4041501581668854
monkey kiwi 0.30731332302093506 
monkey salt 0.0653570294380188  
monkey fish 0.31199339032173157 
banana cat 0.2235882580280304   
banana apple 0.6646699905395508 
banana monkey 0.4041501581668854
banana banana 1.0
banana kiwi 0.7625851631164551  
banana salt 0.364793062210083   
banana fish 0.39355403184890747 
kiwi cat 0.15740658342838287    
kiwi apple 0.6305076479911804   
kiwi monkey 0.30731332302093506 
kiwi banana 0.7625851631164551  
kiwi kiwi 1.0
kiwi salt 0.35219359397888184   
kiwi fish 0.3806382119655609    
salt cat 0.15873362123966217    
salt apple 0.35949474573135376  
salt monkey 0.0653570294380188  
salt banana 0.364793062210083   
salt kiwi 0.35219359397888184   
salt salt 1.0
salt fish 0.5228388905525208    
fish cat 0.319871723651886      
fish apple 0.37951505184173584  
fish monkey 0.31199339032173157 
fish banana 0.39355403184890747 
fish kiwi 0.3806382119655609    
fish salt 0.5228388905525208    
fish fish 1.0
'''

#Interesting outputs using  en_core_web_md
# Cat and banana is only 0.22 but banana and monkey is  0.4 - showing a higher relationship between banana and monkeys
#Fish & Salt also have a high relation of 0.5 - shoes fish and salt may be eaten together
#kiwi and banana 0.76, apple & kiwi 0.63 , apple & banana 0.66 - shows diffrent fruit have higher or lower relationships and aren't all equal
#Cat and fish - 0.31 - fish & monkey 0.31-  Shoes no difference between relationships - although cats are thought to eat fish.

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my car in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity) 

'''where did my dog go -  0.630065230699739    
Hello, there is my car -  0.8033180111627156
I've lost my car in my car -  0.6787541571030323
I'd like my boat back -  0.5624940517078084
I will name my dog Diana -  0.6491444739190607'''





#RUNNING ALL CODE WITH EN_CORE_WEB_SM
print("***RUNNING CODE WITH EN_CORE_WEB_SM***")

nlp  = spacy.load('en_core_web_sm')


tokens = nlp('cat apple monkey banana kiwi salt fish')
for token1 in tokens:

    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#Output when using en_core_web_sm


"""
cat apple 0.7098944187164307
cat monkey 0.592245876789093
cat banana 0.6529050469398499
cat kiwi 0.6591975688934326
cat salt 0.6309078335762024
cat fish 0.12497720867395401
apple cat 0.7098944187164307
apple apple 1.0
apple monkey 0.7637171149253845
apple banana 0.7395413517951965
apple kiwi 0.7149356007575989
apple salt 0.7370610237121582
apple fish 0.24386568367481232
monkey cat 0.592245876789093
monkey apple 0.7637171149253845
monkey monkey 1.0
monkey banana 0.7763100862503052
monkey kiwi 0.7900035977363586
monkey salt 0.709708034992218
monkey fish 0.3213634490966797
banana cat 0.6529050469398499
banana apple 0.7395413517951965
banana monkey 0.7763100862503052
banana banana 1.0
banana kiwi 0.7970467209815979
banana salt 0.7368021011352539
banana fish 0.23744343221187592
kiwi cat 0.6591975688934326
kiwi apple 0.7149356007575989
kiwi monkey 0.7900035977363586
kiwi banana 0.7970467209815979
kiwi kiwi 1.0
kiwi salt 0.7332149147987366
kiwi fish 0.2809262275695801
salt cat 0.6309078335762024
salt apple 0.7370610237121582
salt monkey 0.709708034992218
salt banana 0.7368021011352539
salt kiwi 0.7332149147987366
salt salt 1.0
salt fish 0.29161497950553894
fish cat 0.12497720867395401
fish apple 0.24386568367481232
fish monkey 0.3213634490966797
fish banana 0.23744343221187592
fish kiwi 0.2809262275695801
fish salt 0.29161497950553894
fish fish 1.0
"""

# Comparing MD vs SM
# MD - Cat and banana is 0.22, banana & monkey is  0.4
# SM - Cat & banana is 0.65, - banana and monkey is 0.77 - shows higher relationship values 

#MD Fish & Salt   0.5 - 
#SM Fish & Salt - 0.291 - much lower than MD's relationship 

#MD  - kiwi & banana 0.76, apple & kiwi 0.63 , apple & banana 0.66 - 
#SM - kiwi & banana  0.79, apple & kiwi 0.71, apple & banana 0.73 - shows less variance relationship strength between fruits
# 
# Cat & fish - 0.31 - fish & monkey 0.31-  
#Cat & Fish 0.12, fish & monkey 0.31 - Shows even lower relationshop with cat & fish - although cats are thought to eat fish.




sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my car in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity) 

'''
where did my dog go -  0.4043351553824302
Hello, there is my car -  0.5648939507997681
I've lost my car in my car -  0.548028403302901
I'd like my boat back -  0.3007499696891998
I will name my dog Diana -  0.3904074310483232'''