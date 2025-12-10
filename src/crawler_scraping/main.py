from crawler_pl import Crawler_Portal_Transparencia

if __name__ == "__main__":
    crawler = Crawler_Portal_Transparencia(period_from='01-01-2024',
                                           period_to='01-01-2025',
                                           search_for='favorecido')
    crawler.execute_crawler()