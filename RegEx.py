import re

text = 'Карта map и объект bitmap - это разные вещи'

match = re.findall(r'\bmap\b', text)  # r'\b..\b' if we want to find a separate text
# print(match)

"""Symbol classes [] """
text2 = 'Еда, беду, победа'
match2 = re.findall(r"[еЕ]д[ау]", text2)
# print(match2)

"""Inversion symbols ^ """
text3 = 'Еда, беду, -5 55 победа'
match3 = re.findall(r"[^0-9]", text3)
# print(match3)

"""Quantifiers {}"""
text4 = 'Gogle, Google, Gooogle, Gooooogle'
match4 = re.findall(r"o{2,5}", text4)  # 'Mayor' quantifier
# print(match4)

text5 = 'Gogle, Google, Gooogle, Gooooogle'
match5 = re.findall(r"o{2,5}?", text5)  # 'Minor' quantifier
# print(match5)

phone = '89515201874, 8951931'
matchPhone = re.findall(r"8\d{10}", phone)
# print(matchPhone)

text6 = 'стеклянный, стекляный'
match6 = re.findall(r"стеклянн?ый", text6)
# print(match6)

text7 = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year=  2001'
match7 = re.findall(r"\w+\s*=\s*[^;]+", text7)
# print(match7)
# or
text7a = text7.split(';')
# print(text7a)

text8 = "<p> Картинка <img src='bg.jpg'> в тексте</p>"
match8 = re.findall(r"<img.*?>",
                    text8)  # by default * is a major, that means that the string will proceed till the second >
# to avoid that we must use minor quantifier ?
# print(match8)

text9 = "<p> Картинка <img alt='картинка' src='bg.jpg'> в тексте</p>"
match9 = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text9)
# print(match9)

"""Retaining brackets"""
text10 = "lat = 5, lon = 7, a = 5"
match10 = re.findall(r"(lat|lon)\s*=\s*(\d+)", text10)  # To print kwargs
# print(match10)

"""non-retaining brackets"""
text11 = "lat = 5, lon = 7, a = 5"
match11 = re.findall(r"(lat|lon)\s*=\s*(?:\d+)", text11)  # To print only keys
# print(match11)

text12 = "<p> Картинка <img src='bg.jpg'> в тексте</p>"
match12 = re.findall(r"<img\s*[^>]*src=['](.+?)[']", text12)  # retaining brackets
match12a = re.findall(r"<img\s*[^>]*src=(['])(.+?)\1", text12)  # repeat of retaining brackets
match12b = re.findall(r"<img\s*[^>]*src=(?P<one>['])(.+?)(?P=one)",
                      text12)  # assigning of a name for retaining brackets
# print(match12)
# print(match12a)
# print(match12b)

"""Parsing of a HTML file"""
with open("RegExTest.html", "r") as f:  # r opens file explicitly, without any links
    lat = []
    lon = []
    for text13 in f:
        match13 = re.findall(r'<point\s+[^>]*?lon=([\'\"])([0-9.,]+)\1\s+[^>]*lat=([\'\"])([0-9.,]+)\1', text13)
        if len(match13) > 0:
            lon.append(match13[0][1])
            lat.append(match13[0][3])
#     print(lon, lat, sep='\n')

"""Checks and flags"""

text14 = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

match14 = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text14, re.MULTILINE)  # normal check (?=exp)
match14a = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", text14, re.MULTILINE)  # retrospective check (?<=exp)
match14b = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text14,
                      re.MULTILINE)  # negative retrospective check (?<!exp)  (if dont understand try to add a space in ("control-type ") in text14
# print(match14)
# print(match14a)
# print(match14b)


'''Grouping expressions'''

text15 = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<p align=center>Hello World!</p>
</body>
</html>"""
match15 = re.findall(r"([-\w]+)[ \t]*=[[ \t]*(?P<name>[\"'])?(?(name)([^\"']+(?<![ \t]))|([^ \t>]+))", text15,
                     re.MULTILINE)
# here the following grouping expression is used (?P<name>__)?(?(name)yes_pattern|no_pattern)
# print(match15)

"""Set of flags (examples)"""
match15b = re.findall(r"""([-\w]+)             #выделяем атрибут
                   [ \t]*=[ \t]*            #далее, должно идти равно и кавычки
                   (?P<q>[\"'])?            #проверяем наличие кавычки
                   (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение атрибута
                   """,
                      text15, re.MULTILINE | re.VERBOSE)
# print(match15b)

text16 = "Python, python, PYTHON"
match16 = re.findall(r"(?i)python", text16)
# print(match16)

"""Methods"""
text17 = "<font color=#CC0000>"
match17 = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text17)
# print(match17)
# print(match17.group(0))
# print(match17.group(1))
# print(match17.group(2))
# print(match17.groups())
# print(match17.lastindex)
# print(match17.start(1))
# print(match17.end(1))
# print(match17.span(0))
# print(match17.pos)
# print(match17.endpos)
# print(match17.re)
# print(match17.string)
# print(match17.groupdict())
# print(match17.expand(r'\g<key>:\g<value>'))

"""Methods re"""
text18 = "<font color=#CC0000 bg=#ffffff>"
match18 = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text18) # serach is looking for only a first attribute
# print(match18)

# for match18a in re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text18): # finder is looking for iterated objects, used only in loops
#     # print(match18a.groups())

text19 = "+7(123)456-78-90"
match19 = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text19) # match is used for finding a match starting from the beginning of the string. Try to make a space before +7.
# print(match19)

text20 = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
<point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />
"""

match20 = re.split(r"[\n;,]+", text20) # split divides an array by strings
# print(match20)

text21 = """Москва
Казань
Тверь
Самара
Уфа"""

match21 = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text21) # sub substitutes a selected string by a set value
# print(match21)

count = 0
def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n" # substitution by a function

match21a = re.sub(r"\s*(\w+)\s*", replFind, text21)
# print(match21a)

match21b, total21b = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", text21) # subs returns substituted values and a number of substitutions
# print(match21b, total21b)

comp = re.compile(r"\s*(\w+)\s*")
match21c, total21c = comp.subn(r"<option>\1</option>\n", text21) # compile makes a pattern
print(match21c, total21c)