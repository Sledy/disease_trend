from Bio import Entrez
import pygal




class SearchReport:

    RETMAX = 0
    RET_FORMAT = "xml"

    def __init__(self, query: str, mindate: int, maxdate: int):
        self.query = query
        self.mindate = mindate
        self.maxdate = maxdate

    def count_by_year(self, start_date, end_date):
        Entrez.email = 'moja.praca.dyplomowa123@gmail.com'
        handle = Entrez.esearch(db='pubmed', retmax=SearchReport.RETMAX, term=self.query,
                                retmode=SearchReport.RET_FORMAT, mindate=start_date,
                                maxdate=end_date)

        results = Entrez.read(handle)
        return int(results["Count"])

    def give_trend(self):
        count_list = list()
        year_list = list()

        for i in range(self.mindate, self.maxdate+1):
            year_list.append(str(i))
            count_list.append(self.count_by_year(start_date=str(i), end_date=str(i)))

        graph = pygal.Line()
        graph.title = 'Articles released'
        graph.x_labels = year_list
        graph.add("Articles released in year", count_list)
        graph_data = graph.render_data_uri()

        return graph_data






if __name__ == '__main__':
    articles = SearchReport(query="fever", mindate=1900, maxdate=1901)
    my_dict = articles.give_trend()

