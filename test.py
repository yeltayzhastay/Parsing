import Vk_parser as parser
import time

if __name__ == "__main__":
    url = 'ru_oppo'
    token = "fe91c3a9fe91c3a9fe91c3a96efee5034cffe91fe91c3a9a13265b3a8814f5207fa1f50"
    parse = parser.Vk_parser(token)
    print(parse.get_group_posts_all(url))