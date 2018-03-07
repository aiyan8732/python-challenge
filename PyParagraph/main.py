import os
import re

# List of paragraph
paragraphList = ["1", "2"]

# Loop through paragraph
for paragraph in paragraphList:

    # Grab paragraph path
    inputpath = os.path.join('raw_data','paragraph_' + paragraph + ".txt")
    outputpath = os.path.join('output','output_' + paragraph + ".txt")

    with open(inputpath,'r') as txtFile:
        sentenceList = re.split('(?<=[.!?]) +|\n+',txtFile.read())
        
        # Set initiale list
        sentenceLength = len(sentenceList)
        wordCount = 0
        letterCount = 0

        # loop through sentences in sentenceList
        for sentence in sentenceList:
            wordList = sentence.split(' ')
            wordCount = wordCount + len(wordList)
            for word in wordList:
                letterCount = letterCount + len(word)   

        print("Paragraph Analysis")
        print("-----------------------------")
        print("Approximate Word Count: " + str(wordCount))
        print("Approximate Sentence Count: " + str(sentenceLength))
        print("Average Letter Count: " + str(letterCount/wordCount))
        print("Average Sentence Length: " + str(wordCount/sentenceLength))
        print(" ")

    # Write analysis into new txt file
    with open(outputpath, 'w') as txtFile:
        txtFile.write("Paragraph Analysis")
        txtFile.write("\n-----------------------------")     
        txtFile.write("\nApproximate Word Count: " + str(wordCount))
        txtFile.write("\nApproximate Sentence Count: " + str(sentenceLength))
        txtFile.write("\nAverage Letter Count: " + str(letterCount/wordCount))
        txtFile.write("\nAverage Sentence Length: " + str(wordCount/sentenceLength))
        
          


        
        


        
                
            
            
