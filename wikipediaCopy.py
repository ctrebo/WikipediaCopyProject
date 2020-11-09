import wikipediaapi
import os


#get Language
def getLanguageInput():
    while True:
        language = input("Enter a Language('de', 'en', 'it', 'q' to quit): ")
        if language == "de" or language == "en" or language == "it":
            print(language)
        elif language == 'q':
            exit()
        else:
            print("Language not avalaible")
        

#get file path from user
def getFilePath():
    while True:
        path = input("Enter path to dictionary where the file with text should be placed: ")  
        if '\\\\' in path or '//' in path:                                  #dont let user use '//' and '\\'
            print("Do not use '\\\\' or '//' in path")
        else:
            if '/' in path and "\\" not in path:                            #if '/' in path replace it with '\\'
                path = path.replace('/', '\\\\')      
                if os.path.exists(path):                                    # If the path exists return it
                    return path
                else:
                    print("The path doesnt exists")

            elif '\\' in path and "/" not in path:                          #if '\' in path replace it with '\\'
                path = path.replace('\\', '\\\\')                           
                if os.path.exists(path):                                    # If the path exists return it
                    return path
                else:
                    print("The path doesnt exists")

            elif '\\' in path and '/' in path:
                path = path.replace('\\', '\\\\')                           #if '\' and '/' in path replace it with '\\'
                path = path.replace('/', '\\\\')
                if os.path.exists(path):                                    # If the path exists return it
                    return path
                else:
                    print("The path doesnt exists")

def main():
    wiki_wiki = wikipediaapi.Wikipedia(getLanguageInput())                  #get Language of Wikipedia Artikel
    thema = input("Enter the topic you want to use: ")
    page_py = wiki_wiki.page(thema)

    print("Page - Exists: {}".format(page_py.exists()))
    print("Page - Summary: {} ".format(page_py.summary[0:300]))



