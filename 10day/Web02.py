# Web02.py

import webbrowser
google_url = "www.google.com/#q="
search_words = ['python web scraping','python webbrowser']

for search_word in search_words:
    webbrowser.open_new(google_url+search_word)