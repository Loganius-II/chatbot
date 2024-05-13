import wikipediaapi
from PyEssnt_LoganTheCreator.pyEssnt import Replace_Str
def search_wikipedia(query: str):
    wiki_wiki = wikipediaapi.Wikipedia('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0', 'en')
    query = Replace_Str(query).for_str("who","what","when","where","why","was","to")
    page = wiki_wiki.page(query)
    
    if page.exists():
        return page.summary
    else:
        return None

def extract_topic(query):
    # List of common question words
    question_words = ["who", "what", "where", "when", "why", "how", "was", "to"]
    # Split the query into words
    words = query.lower().split()
    # Remove question words from the query
    cleaned_words = [word for word in words if word not in question_words]
    # Join the cleaned words back into a string
    cleaned_query = " ".join(cleaned_words)
    return cleaned_query

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            cleaned_query = extract_topic(user_input)
            result = search_wikipedia(cleaned_query)
            print("Bot:", result)

if __name__ == "__main__":
    main()
