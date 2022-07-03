from lxml import etree

tree = etree.parse('gettext.html', etree.HTMLParser())
r = tree.xpath('//div[@class="text1"]//text()')
# print(r)
for each in r:
    print(each)