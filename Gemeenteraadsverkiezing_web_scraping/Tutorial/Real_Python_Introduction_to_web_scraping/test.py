from mathematicians import simple_get
raw_html = simple_get('https://www.vlaanderenkiest.be/verkiezingen2012/#/gemeente/11005/p_-5/uitslagen')
print(len(raw_html))
file = open('test.html', 'w')
file.write(raw_html)
file.close()
