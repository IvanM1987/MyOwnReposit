
# # a = 100
# # b = [1, 2, 3, 4]
# #
# # def test(some_list):
# #     some_list.append(100)
# #
# # def test2(x):
# #     x += 1
# #     print(x)
# #
# # test2(a)
# #
# # test(b)
# # print(b)
#
# # a = [1, 2, 3, 4, 5]
# # b = a.copy()
# #
# # b.append(100)
# # print(a, b)
#
# # import copy
# #
# # a = [1, 2, 3, 4, 5, [1, 2, 3]]
# # b = copy.deepcopy(a)
# #
# # b[5].append(100)
# # print(a, b)
#
# # matrix = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# #     [7, 8, 9]
# # ]
# #
# # for line in matrix:
# #     for num in line:
# #         print(num)
#
# # numpy - Р±РёР±Р»РёРѕС‚РµРєР°
#
# # print(1 and 0)
# # print(1 and 2)
# # print(0 and 0)
# # print(1 and 0)
#
# # print(1 or 0)
# # print(4 or 1)
# # print(0 or 0)
#
# # name = input('Name:')
# #
# # print(name or 'Guest')
#
#
# # age = int(input('age:'))
# #
# # # РўРµСЂРЅР°СЂРЅС‹Р№ РѕРїРµСЂР°С‚РѕСЂ
# # print('Welcome' if age >= 18 else 'Good Bye')
#
# # a = 10
# # b = 10
# # print(a is b)
# # a = 11
# # b = 11
# # print(a is b)
#
# # a = [1, 2]
# # b = [1, 2]
# #
# # print(a is b)
#
# import random
#
# count = 10
# # result = []
# #
# # for _ in range(count):
# #     result.append(random.randint(-100,100))
# #
# # print(result)
# #
# # result = [random.randint(-100,100) for _ in range(count)]
# # result = [i ** 2 for i in range(count)]
# # result = [i ** 2 for i in range(-10, 5) if i > 0]
# # print(result)
# #
# # result = {i: random.randint(-100,100) for i in range(count)}
# # print(result)
#
# # a = [1, 2]
# #
# # try:
# #     a[0]
# #     1/0
# # except IndexError:
# #     print('РќРµРІРµСЂРЅС‹Р№ РёРЅРґРµРєСЃ!')
# # except ZeroDivisionError:
# #     print('РќРµР»СЊР·СЏ РґРµР»РёС‚СЊ РЅР° РЅРѕР»СЊ!')
# # except Exception as e:
# #     print(e.__class__)
# # else:
# #     print('РСЃРїРѕР»РЅРёС‚СЃСЏ РµСЃР»Рё РѕС€РёР±РѕРє РЅРµ Р±С‹Р»Рѕ!')
# # finally:
# #     print('РСЃРїРѕР»РЅРёС‚СЃСЏ РІ Р»СЋР±РѕРј СЃР»СѓС‡Р°Рµ!')
# #
# # print(100)
#
# # regex101.com
# #
# # import re
# #
# # pattern = '^([a-zA-Z0-9-]+)@[a-z]+\.(ru|org|com|СЂС„)$'
# # email = 'Bear-1@animals.com'
# #
# # search_result = re.search(pattern, email)
# # if search_result:
# #     print(search_result.group(0))
# #     print(search_result.group(1))
# #     print(search_result.group(2))
# #     print('РђРґСЂРµСЃ РІРµСЂРЅС‹Р№!')
# # else:
# #     print('РђРґСЂРµСЃ РЅРµ РІРµСЂРЅС‹Р№!')
# #
# # print(re.search(pattern, email))
# # print(re.match(pattern, email))
#
# # pattern = '89[0-9]{9}'
# # text = 'bla bla bla 89173333333 bla bla bla 89173345333'
# # print(re.findall(pattern, text))
#
# # HARD - РґРµР»Р°РµРј Р±РµР· СЂРµРіСѓР»СЏСЂРЅС‹С… РІС‹СЂР°Р¶РµРЅРёР№!!!