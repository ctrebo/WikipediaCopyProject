import wikipediaapi
import os
import random
from time import sleep


#get Language
def getLanguageInput():
    while True:
        language = input("Enter a Language('de', 'en', 'it', 'q' to quit): ")
        if language == "de" or language == "en" or language == "it":
            return language
        elif language == 'q':
            exit()
        else:
            print("Language not avalaible")
        
def getRandomNumber():
    return random.randint(1, 1000)


#get file path from user
def getFilePath():
    while True:
        path = input("Enter path to dictionary where the file with text should be placed: ")  
        if '\\\\' in path or '//' in path:                                  #dont let user use '//' and '\\'
            print("Do not use '\\\\' or '//' in path")
        else:
            if os.path.exists(path):
                return path
           
#function which takes the path to the directory, the thema the user wants to search for and a random number
# and then returns the whole path with filename
def getfullPath(path, thema, random_number, extension):
    while True:
        filename = thema + str(random_number) + extension
        if not os.path.isfile(os.path.join(path, filename)):
            return os.path.join(path, filename)
        else:
            random_number = random.randint(1, 1000)

#function which is meant to get an Option from the user. The option decides how the program
#will run after the first articel got copied into a file
def getOption():
    while True:
        print("---------------------------------\nWhat do you want to do now?\n Enter 1 to Copy another article into the same file\n Enter 2 to copy something into another file\n Enter 'q' to quit\n")
        option = input(": ")
        if option == "1" or option == "2" or option == 'q':
            print('\n')
            return option
        else:
            print("\nInvalid input!") 

#main function, put the pieces together
def main():
    while True: 
        file_extension = ".txt"
        wiki_wiki = wikipediaapi.Wikipedia(getLanguageInput())                  #get Language of Wikipedia Artikel
        path = getFilePath()                                                    #get File path from user
        random_number = getRandomNumber()                                       #get random Number

        thema = input("Enter the topic you want to use: ")                      #get topic from user
        page_py = wiki_wiki.page(thema)
        while page_py.exists() == False:
            thema = input("Page doesnt exists: ")                               #get topic from user
            page_py = wiki_wiki.page(thema)

        full_path_to_file = getfullPath(path, thema, random_number, file_extension)
        with open(full_path_to_file, 'w', encoding='utf8') as file:
                file.write(page_py.summary)
                print("Done\n")
                sleep(1)
        
        bool_for_option = True

        while bool_for_option:  
            sleep(1)                                                
            option = getOption()
            if option == "1":
                wiki_wiki = wikipediaapi.Wikipedia(getLanguageInput())

                thema = input("Enter the topic you want to use: ")                 #get topic from user
                page_py = wiki_wiki.page(thema)
                while page_py.exists() == False:
                    thema = input("Page doesnt exists: ")                          #get topic from user
                    page_py = wiki_wiki.page(thema)
                with open(full_path_to_file, 'a', encoding='utf8') as file:
                    file.write("\n\n\n\n")
                    file.write(page_py.summary)
                    print("Copied article into file\n")


            if option == "2":                                                      #idee: loop unterbrechen mit bool_for_option = False
                bool_for_option = False

            if option == 'q':
                exit()


main()
