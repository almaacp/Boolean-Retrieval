#%% Simpan dokumen

documents = {
    "D1": "Machine learning improves search engines.",
    "D2": "Information retrieval techniques are evolving.",
    "D3": "Boolean retrieval use logical operators.",
    "D4": "Query processing is essential in search engines.",
    "D5": "Data science leverages machine learning.",
    "D6": "Machine learning improves search engine results.",
    "D7": "Information retrieval approaches are popular.",
    "D8": "Search algorithms improve information discovery.",
    "D9": "Data science integrates complex search engine results.",
    "D10": "Ranking methods optimize search engine results."
}

#%% Membuat fungsi boolean retrieval

def boolean_retrieval(query, documents):
    results = []
    query = query.lower()
    for doc_id, text in documents.items():
        text = text.lower()
        if 'and' in query:
            terms = query.split(' and ')
            if all(term in text for term in terms):
                results.append(doc_id)
        elif 'or' in query:
            terms = query.split(' or ')
            if any(term in text for term in terms):
                results.append(doc_id)
        elif 'not' in query:
            terms = query.split(' not ')
            if terms[0] in text and terms[1] not in text:
                results.append(doc_id)
    return results

#%% Uji coba dengan query

queries = [
    "Search AND Engine",
    "Information OR Retrieval",
    "Machine NOT Learning"
]

for q in queries:
    hasil = boolean_retrieval(q, documents)
    print(f"Query: {q}")
    print(f"Dokumen relevan: {hasil}")
    print("-----")
