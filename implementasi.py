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

#%% Normalisasi dan tokenisasi

import re

def preprocess_text(text):
    # 1. Lowercase
    text = text.lower()
    # 2. Hapus karakter non-huruf (opsional, di sini contoh hapus tanda baca dasar)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # 3. Tokenisasi berdasarkan spasi
    tokens = text.split()
    return tokens

# Membuat struktur baru yang berisi token-token setiap dokumen
tokenized_docs = {}
for doc_id, content in documents.items():
    tokenized_docs[doc_id] = preprocess_text(content)

# Cek isi token
print("D1:",tokenized_docs["D1"])
print("D2:",tokenized_docs["D2"])
print("D3:",tokenized_docs["D3"])
print("D4:",tokenized_docs["D4"])
print("D5:",tokenized_docs["D5"])
print("D6:",tokenized_docs["D6"])
print("D7:",tokenized_docs["D7"])
print("D8:",tokenized_docs["D8"])
print("D9:",tokenized_docs["D9"])
print("D10:",tokenized_docs["D10"])

# %% Membuat fungsi boolean retrieval

def boolean_retrieval(tokens_dict, query):
    """
    Mengembalikan list dokumen yang relevan dengan query Boolean sederhana.
    Query diasumsikan dalam bentuk: 'term1 AND term2', 'term1 OR term2', atau 'term1 NOT term2'.
    """
    # 1. Lowercase query dan pisahkan berdasarkan spasi
    q = query.lower().split()

    # Antisipasi format query 3 kata: [term1, operator, term2]
    if len(q) != 3:
        raise ValueError("Format query tidak sesuai (harus 3 bagian: term1 OP term2).")

    term1, operator, term2 = q[0], q[1], q[2]

    # 2. Kumpulkan dokumen mana saja yang mengandung term1 dan term2
    docs_with_term1 = set()
    docs_with_term2 = set()

    for doc_id, tokens in tokens_dict.items():
        if term1 in tokens:
            docs_with_term1.add(doc_id)
        if term2 in tokens:
            docs_with_term2.add(doc_id)

    # 3. Operasi Boolean
    if operator == "and":
        # Dokumen yang mengandung term1 DAN term2
        result = docs_with_term1.intersection(docs_with_term2)
    elif operator == "or":
        # Dokumen yang mengandung term1 ATAU term2
        result = docs_with_term1.union(docs_with_term2)
    elif operator == "not":
        # Dokumen yang mengandung term1 TAPI TIDAK mengandung term2
        result = docs_with_term1.difference(docs_with_term2)
    else:
        raise ValueError("Operator yang didukung hanya AND, OR, NOT.")

    return sorted(list(result))

#%% Uji coba dengan query

queries = [
    "Search AND Engine",
    "Information OR Retrieval",
    "Machine NOT Learning"
]

for q in queries:
    hasil = boolean_retrieval(tokenized_docs, q)
    print(f"Query: {q}")
    print(f"Dokumen relevan: {hasil}")
    print("-----")
