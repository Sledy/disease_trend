from Bio import Entrez
import pygal


class SearchReport:

    RETMAX = 0
    RET_FORMAT = "xml"

    def __init__(self, query: str, mindate: int, maxdate: int):
        """
        Class includes methods that perform basic operation on PubMed database using Entrez library

        :param query: name that would be searched for in database
        :param mindate: minimal date which would be taken in search
        :param maxdate: maximal date which would be taken in search
        :type query: str
        :type mindate: str
        :type maxdate: str
        """
        self.query = query
        self.mindate = mindate
        self.maxdate = maxdate

    def count_by_year(self, start_date: str, end_date: str):
        """
        Methods search for data based on the given time interval and returns the count of articles found for given year

        :param start_date: starting date which would be taken in search
        :param end_date: ending date which would be taken in search
        :type start_date: str
        :type end_date: str

        :return: return number of articles count
        :rtype: int
        """
        Entrez.email = 'moja.praca.dyplomowa123@gmail.com'
        handle = Entrez.esearch(db='pubmed', retmax=SearchReport.RETMAX, term=self.query,
                                retmode=SearchReport.RET_FORMAT, mindate=start_date,
                                maxdate=end_date)

        results = Entrez.read(handle)
        return int(results["Count"])

    def give_trend(self):
        """
        Generate uri with the graph including article trend for the given time interval. Method send request per year,
        therefore its operation can be time consuming

        :return: uri for the graph generation
        :rtype: str
        """
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

