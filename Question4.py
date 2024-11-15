from bs4 import BeautifulSoup
import re

# Specify the file name (relative path)
file_name = "index.html"

# Open the file in read mode
with open(file_name, "r", encoding="utf-8") as file:
    # Read the file content
    html_content = file.read()

# Parse the HTML with BeautifulSoup
bs = BeautifulSoup(html_content, "html.parser")

# a. [3 points]. The text of the HTML page title. Use the HTML tags to do this search.
print(bs.title.text)
print()
# b. [3 points]. The text of the second list item element <li> below "To show off"? Use the HTML tags to do this search. The output should be "To my friends".
print(bs.body.ul.li.next_sibling.get_text())
# c. [3 points]. All <td> tags in the first row <tr> of the table. Use the HTML tags to do this search.
print(bs.body.table.tr.find_all("td"))
# d. [3 points]. All <h2> headings text that includes the word “tutorial”. Use the HTML tags and regex to do this search.
print(bs.find_all('h2', string=(re.compile('tutorial'))))
# e. [3 points]. All text that includes the “HTML” word. Use the HTML text to do this search.
print(bs.find_all(string=(re.compile('HTML'))))
# f. [3 points]. All text in the second row <tr> of the table. Use the HTML tags to do this search.
print(bs.body.table.tr.next_sibling.next_sibling)
# g. [3 points]. All <img> tags from the table. Use the HTML tags to do this search.
print(bs.find_all("img"))