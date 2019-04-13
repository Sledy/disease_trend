from Bio import Entrez


def search(query):
    Entrez.email = 'moja.praca.dyplomowa123@gmail.com'
    handle = Entrez.esearch(db='pubmed', term=query, retmode='json')
    results = Entrez.read(handle)
    return results


def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results



if __name__ == '__main__':
    results = search('fever')

    print()

