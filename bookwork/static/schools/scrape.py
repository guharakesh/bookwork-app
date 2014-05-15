from bs4 import BeautifulSoup

soup = BeautifulSoup(open('/home/bookwork/app/bookwork/static/schools/colleges.html'))
f = open('/home/bookwork/app/bookwork/static/schools/out.txt','w')

count = 1

for link in soup.body.contents[1].contents[9].contents[9].find_all('a'):
    if len(link.parent.contents) != 4:
        name = link.contents[0].encode('utf-8')
        data = '{0}|{1}\n'.format(count,name)
        f.write(data)
        count = count + 1

f.close()
