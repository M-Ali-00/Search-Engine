from ingest import ingest_page
from search import search

# page = {
#     "url": "https://math.com/calculus",
#     "title": "Introduction to Calculus",
#     "text": """
#     A derivative measures how a function changes.
#     Limits help define derivatives.
#     Integrals measure accumulation.
#     """
# }

# ingest_page(page)

# print("Page ingested successfully")

print(search("what is a derivative?"))