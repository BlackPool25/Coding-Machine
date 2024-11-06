from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_tags = soup.find_all('div', class_='card')
    for tag in course_tags:
        print(tag.h5.text)
        print(tag.a.text)
        print()