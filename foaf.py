import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import word_tokenize,pos_tag, ne_chunk
from nltk import RegexpParser

# Affiliation is the list that includes the verbs means "work for".
Affiliation = ["work", "works", "worked", "working", "affiliates", "affiliate", "affiliated", "affiliating", "serve", "serves", "served", "serving", "employed", "hired", "occupied"]

# Third Person, to replace "he" or "she" with a specific name.
Third_person = ["He", "She", "They", "he", "she", "they"]

# Knows_action is the list that indicates A knows B, it contains all kinds of tense.
# The verbs list contains "whisper", "dance", "talk", "speak", "play", "call", "pursue", "acclaim".
Knows_action = ["whispering", "whisper", "whispers", "whispered", "dancing", "dance", "dances", "danced", "talking", "talk", "talks", "talked", "playing", "play", "plays", "played", "speaking", "speak", "speaks", "spoke", "spoken", "calling", "call", "calls", "called", "pursuing", "pursue", "pursues", "pursued", "acclaiming", "acclaim", "acclaims", "acclaimed"]

# Negationlist is the list that indicates deny, for example, do not/ don't.
Negationlist = ["not", "n't"]

# Negation flag in the first sentence.
negation_flag1 = 0

# Negation flag in the second sentence.
negation_flag2 = 0

# Name list to store the Person's name.
namelist = []
validation_name = []

# Organization list to store the name of Organization.
organizationlist = []
validation_organization = []

# Location list to store the name of Location.
locationlist = []

# The sentence to be analyzed.
sentence = "Jimmy works at Google in California. He was seen whispering to Marla."

# Create a text file and write the output to this file, named Output.txt, the path of this file may be changed in different computer.
f = open("C:/Users/Bolong/Desktop/AIFIN/Output.txt",'w+')

# Write the prefix and namespace in text file.
f.write("@prefix : <https://s2.smu.edu/~47838730/#>.\n@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.\n@prefix schema: <http://www.schema.org> \n\n")

# Get the list of tuples of tags.
tags = pos_tag(word_tokenize(sentence))

# Split the original sentence into two sentences using ".", this step is used to judge negative sentence.
tags_1_negation = pos_tag(word_tokenize(sentence.split(".")[0]))
tags_2_negation = pos_tag(word_tokenize(sentence.split(".")[1]))

# Judge whether sentence 1 is Negative Sentences, if yes, the negation_flag1 will be 1.
for i in tags_1_negation:
    if i[0] in Negationlist:
        negation_flag1 = 1

# Judge whether sentence 2 is Negative Sentences, if yes, the negation_flag2 will be 1.
for i in tags_2_negation:
    if i[0] in Negationlist:
        negation_flag2 = 1

# Chunk the tags from original sentence and get the tree structure.
neChunks = ne_chunk(tags)
#print("\n", type(neChunks))
#print(neChunks)

# Affiliation_flag used to judge whether a person employed by an organization, 0 means "No".
affliation_flag = 0

# Get Person's name using chunk.
for i in neChunks.subtrees(filter=lambda x: x.label() == 'PERSON'):
    #print("Subtree = ", i)
    for node in i:
        name, type = node
        # If find a person's name, add it into namelist
        namelist.append(name)
        # Get the N3 triples "rdf:type schema:Person" and "schema:givenName"
        f.write(":" + name + " rdf:type schema:Person .\n")
        f.write(":" + name + " schema:givenName " + '\"' + name + '\"' + " .\n")
        print(":" + name + " rdf:type schema:Person .")
        print(":" + name + " schema:givenName " + '\"' + name + '\"' + " .")

# Get Organization's name using chunk.
for i in neChunks.subtrees(filter=lambda x: x.label() == 'ORGANIZATION'):
    #print("Subtree = ", i)
    for node in i:
        organization, type = node
        # If find a organization, add it into organizationlist.
        organizationlist.append(organization)
        # Get the N3 triples "rdf:type schema:Organization" and "schema:name"
        f.write(":" + organization + " rdf:type schema:Organization .\n")
        f.write(":" + organization + " schema:name " + '\"' + organization + '\"' + " .\n")
        print(":" + organization + " rdf:type schema:Organization .")
        print(":" + organization + " schema:name " + '\"' + organization + '\"' + " .")

# Get Location's name using chunk.
for i in neChunks.subtrees(filter=lambda x: x.label() == 'GPE'):
    #print("Subtree = ", i)
    for node in i:
        location, type = node
        # If find a location, add it into locationlist.
        locationlist.append(location)
        # Get the N3 triples "rdf:type schema:Place" and "schema:name"
        f.write(":" + location + " rdf:type schema:Place .\n")
        f.write(":" + location + " schema:name " + '\"' + location + '\"' + " .\n")
        print(":" + location + " rdf:type schema:Place .")
        print(":" + location + " schema:name " + '\"' + location + '\"' + " .")

# When get the organization and location, we can find organization locates at someplace, Get the N3 triples "schema:location".
for t in organizationlist:
    for r in locationlist:
        f.write(":" + t + " schema:location " + ":" + r + " .\n")
        print(":" + t + " schema:location " + ":" + r + " .")

# Judge employment relationship.
for i in tags:
    if i[0] in namelist:
        validation_name.append(i[0])
    if i[0] in Affiliation:
        # Find the verbs means employment relationship, then affliation_flag will be set to 1.
        affliation_flag = 1
    if i[0] in organizationlist:
        validation_organization.append(i[0])
        # When the organization was found, then affliation_flag will be set to 1., now we have person name, organization and employement, then can create a new triple.
        affliation_flag = 2
    if affliation_flag == 2 and len(validation_organization) and len(validation_name):
        organ = validation_organization.pop()
        for each in validation_name:
            if negation_flag1 == 0:
                # If the sentence is not negative sentence, like "He didn't work at Google.", then create the triple.
                f.write(":" + each + " schema:memberOf " + ":" + organ + " .\n")
                print(":" + each +  " schema:memberOf " + ":" + organ + " .")

# Using grammar to analyze the sentence.
regex = RegexpParser(r'''
NP: {<DT>?<NN.*>+}
VP: {<VB.*>*<TO|IN>?}
}<TO|IN>{
''')


#print(namelist)

#print(organizationlist)

validation_name = []

# Replace the sentence "He was seen whispering" with "Jimmy was seen whispering."
for i in tags:
    if i[0] in namelist:
        validation_name.append(i[0])
    if i[0] in Third_person and len(validation_name):
        k = validation_name.pop()
        sentence = sentence.replace(i[0], k)
        #print(sentence)


#print(sentence)

multiple_sentence = sentence.split(".")

tags = pos_tag(word_tokenize(multiple_sentence[1]))
#print(tags)


validation_know = []

validation_name = []

#############################

for i in tags:
    if i[0] in namelist:
        # Find which NP is the person's name, if found, store it in validation_name list.
        validation_name.append(i[0])
        #print(validation_name)
    if i[0] in Knows_action:
        # Find the verb which has the meaning "knows", if found, add it into validation_know list.
        validation_know.append(i[0])
        #print(validation_know)
    if len(validation_name)==2 and len(validation_know):
        know_person2 = validation_name.pop()
        know_person1 = validation_name.pop()
        if negation_flag2 == 0:
            # If the sentence is not negative sentence, then create the new triple "schema:knows".
            f.write(":" + know_person1 + " schema:knows " + ":" + know_person2 + " .\n")
            f.write(":" + know_person2 + " schema:knows " + ":" + know_person1 + " .\n")
            print(":" + know_person1 + " schema:knows " + ":" + know_person2 + " .")
            print(":" + know_person2 + " schema:knows " + ":" + know_person1 + " .")


#############################
tg = regex.parse(tags)

#print(tg)