import Vk_parser as parser
import time

def main():
    first_time = time.time()
    
    urls = ['samsung.galaxy_a', 'kupit_iphone_v_moskve', 'rumicomrussia', 'huaweip20', 'ru_oppo']

    token = "fe91c3a9fe91c3a9fe91c3a96efee5034cffe91fe91c3a9a13265b3a8814f5207fa1f50"

    vk_parse = parser.Vk_parser(token)
    vk_parse.Get_sentimental(urls, 50)
    vk_parse.to_csv('dataset20.11.csv')

    print('Parsing data finished!', round(time.time() - first_time, 2), 'sec')

if __name__ == "__main__":
    main()