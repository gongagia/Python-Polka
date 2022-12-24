"""
Script for singular phrase google hacking. Text files are not included for upload. Look at web archive for
google index filetypes in the readme and operators utilized. google version 3.0.0 python package was implemented for
this script.
"""
import googlesearch
import re

"""
variable declaration for search arrays and user input for search query. Rationale behind multiple arrays is to
improve efficiency of search queries and negating the newlines prevalent in array entry 
"""
user_input = input("What do you want to search: ")
file_types_query,file_types, filequery, filetypes, google_search_queries, google_queries, google_queries_concat = \
    [], [], [], [], [], [], []

"""
opens up two text files: queries and extensions. Throughout the file opening interation, the utilization of arrays 
google_search_queries, file_types, and file_types_queries. Iteration of the files pushes the contents into the array
google_search_queries. If filetype: is discovered in the queries txt files, for loop iteration is employed; appending
extensions.txt contents to the filetype: query in the queries.txt. Only filetype: is concated with extensions due to the
conditional. File_type_query introduces search options for a specified filetype indexable by google and user input 
"""
with open("queries.txt", 'r') as q:
    with open("extensions.txt", 'r') as e:
        for queries in q:
            google_search_queries.append(queries + user_input)
            if "filetype:" in queries:
                for extensions in e:
                    file_types.append(queries + extensions)
                    file_types_query.append(queries + extensions + " " + '"' + user_input + '"')

"""
with the declaration of search query combinations, the filetype: query value in google_search_queries was popped.
implementation of for loops is to replace the \n prevalent in each value stored file_types_query, file_types. These 
modified values are appended to four arrays: filequery, filetypes, and googlequeries, google_queries_concat. 
Google_queries_concat
"""
google_search_queries.pop(0)
for sub in file_types_query:
    filequery.append(re.sub('\n', '', sub))

for sub in file_types:
    filetypes.append(re.sub('\n', '', sub))

for x in google_search_queries:
    google_queries.append(re.sub('\n', '', x))

for x in google_queries:
    for y in filetypes:
        google_queries_concat.append(x + " " + y)

"""
implements the google python package to print off search results based on search query. Pause functionality is 
a wait timer per http request to mitigate HTTP 424 errors. utilizes the google_queries to perform a baseline search 
from the values of those arrays. Conditional in the iteration for x in google_queries_concat: is present because of 
link: and cache: operators adverse collaborations of other operators
"""
for x in google_queries:
    print(x)
    for y in googlesearch.search(x, pause=69.0):
        print(y)

for x in google_queries_concat:
    if "link" and "filetype" or "cache" and "filetype" in x:
        google_queries_concat.pop()
    print(x)
    for y in googlesearch.search(x, pause=69.0):
        print(y)

