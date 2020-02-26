import sys
from pprint import pprint
from zipfile import *
import string
import itertools
import os


def one_dimension(l):
    gl_l = []

    def recursa(l):
        for i in l:
            if isinstance(i, list):
                recursa(i)
            else:
                gl_l.append(i)
    recursa(l)
    return gl_l


if not os.path.exists("directory"):
    with ZipFile(r"D:\Документы\Универ\Python\hillel\lesson6.zip", "r") as f:
        t = list(itertools.product(string.ascii_lowercase, repeat=3)) # список сочетаний с повторениями из 3х букв
        print(len(t))
        for i in t:
            password = "".join(i)
            # print(password)
            password = password.encode('utf8')
            # print(password)
            try:
                f.extractall("directory", pwd=password)
                print(password)
                print("Ok")
                break
            except Exception as E:  # except RuntimeError as E:
                print(f"Not found yet: {E}")


if not os.path.exists("new_directory"):
    os.mkdir(r"D:\Документы\Универ\Python\hillel\9\new_directory")


white_walker = os.walk(r"D:\Документы\Универ\Python\hillel\9\directory")
# print(white_walker)
city_list = {}
list_of_all = []
for i in white_walker:
    t = one_dimension(i)
    for j in t:
        if j.endswith(".txt"):
            f = open(r"{}\{}".format(i[0], j), errors="ignore")
            for line in f:
                line_list = line.split(sep="\t")

                cur_city = line_list[3]
                domain = line_list[5]
                user_id = line_list[4]

                if cur_city not in city_list:
                    city_list[cur_city] = {domain: [user_id]}
                else:
                    city_content = city_list[cur_city]
                    if domain not in city_content:
                        city_list[cur_city][domain] = [user_id]
                    else:
                        city_list[cur_city][domain].append(user_id)
                if not isinstance(city_list[cur_city][domain], list):
                    raise Exception("!")
                # print(line_list)


# pprint(list_of_all)
# pprint(city_list)

if not os.path.exists(r'D:\Документы\Универ\Python\hillel\9\Cities'):
    os.mkdir(r'D:\Документы\Универ\Python\hillel\9\Cities')

c_l = city_list.copy()
for i in c_l:
    # print(i)
    # print(type(i))
    with open(rf'D:\Документы\Универ\Python\hillel\9\Cities\{i}.tsv', 'w') as citi_i:

        for j in c_l[i]:
            # print(j)
            # print(type(j))
            # print(c_l[i][j])
            # print("! ", set(c_l[i][j]))
            # print(type((c_l[i])[j]))

            city_list[i][j] = len(set(c_l[i][j]))
            # print(city_list[i][j])
            # citi_i.write(f"{city_list[i]}\n")
            # city_list[i][j] = len(c_l[i][j])

print(city_list)
for i in c_l:

    with open(f'D:\\Документы\\Универ\\Python\\hillel\\9\\Cities\\{i}.tsv', 'w') as citi_i:

        for j in city_list[i]:
            # city_list[i][j] = len(set(c_l[i][j]))
            # print(city_list[i][j])
            citi_i.write(f"{j}\t{city_list[i][j]}\n")
            # city_list[i][j] = len(c_l[i][j])





"""
 “device\tage\tsex\tcity\tuser_id\tsearch_keyword\tdomain\turl\ttype”
"""
