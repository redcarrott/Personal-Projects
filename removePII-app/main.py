#!/usr/bin/env python3

print(str("\n\n -- Removing PIIs from PDFs -- \n" + 
         "This program is meant to remove PIIs, " + 
         "specifically names, addresses, and emails " + 
         "from PDFs to ensure digital privacy.\n" + 
         "Please make sure that all PDF pages are compiled into one PDF, " +
         "and named under \'example1.pdf\'"".\n\n"))


#############################################################################
###################### Running the script ###################################
#############################################################################


# imports
import fitz
import re

import ast
with open('personal_info.txt') as f:
    x = f.read()

info = ast.literal_eval(x)
#print(info)
 
class Redactor:
   
    # static methods work independent of class object
    @staticmethod
    def get_sensitive_data(lines):
       
        """ Function to get all the lines """
         
        # email regex
        EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
        for line in lines:
           
            # matching the regex to each line
            if re.search(EMAIL_REG, line, re.IGNORECASE):
                search = re.search(EMAIL_REG, line, re.IGNORECASE)
                #print(search)
                 
                # yields creates a generator
                # generator is used to return
                # values in between function iterations
                yield search.group(1)
                #print(search.group(1))
        
        # names and addresses from personal_info.txt
        for i in info:
            for line in lines:
                
                for x in info[i]:
                    if x in line:
                        search_2 = x
                        #print(search_2)

                        yield search_2
                        #print(search_2.group(2))
                    
 
    # constructor
    def __init__(self, path):
        self.path = path
 
    def redaction(self):
       
        """ main redactor code """
         
        # opening the pdf
        doc = fitz.open(self.path)
         
        # iterating through pages
        for page in doc:
           
            # _wrapContents is needed for fixing
            # alignment issues with rect boxes in some
            # cases where there is alignment issue
            ## page._wrapContents()
             
            # getting the rect boxes which consists the matching email regex
            #print(page.get_text("text").split('\n'))
            # this creates a list of the PDF text contents
            sensitive = self.get_sensitive_data(page.get_text("text")
                                                .split('\n'))
            
            for data in sensitive:
                areas = page.search_for(data)
                 
                # drawing outline over sensitive datas
                [page.add_redact_annot(area, fill = (0, 0, 0)) for area in areas]
                 
            # applying the redaction
            page.apply_redactions()
             
        # saving it to a new pdf
        doc.save('redacted.pdf')
        print("Successfully redacted")
 
# driver code for testing
if __name__ == "__main__":
   
    # replace it with name of the pdf file
    path = 'example1.pdf'
    redactor = Redactor(path)
    redactor.redaction()

