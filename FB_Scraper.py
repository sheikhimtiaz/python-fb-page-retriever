from Scraper import Scraper, Browser
import getpass

username = input("Username: ")
password = getpass.getpass('Password: ')
profile = input("Profile: ")

def fileName():
    i = len(profile)-1
    rt = []
    while i >= 0:
        if profile[i] == r'/':
            break
        rt.append(profile[i])
        i -= 1
    return ''.join(list(reversed(rt))) + '.txt'


output = open(fileName(), 'w', buffering=1,  encoding='utf-8')
br = Browser()
br.Login(username, password)

scraper = Scraper()
scraper.setHtml(br.getSource(profile))
navs = scraper.getNavLinks()

i = 0
while i < len(navs):
    if "Show more" in navs[i][0]:
        i += 1
        break
    i += 1

while i < len(navs):
    url = navs[i][1]
    while True:
        html = br.getSource(url)
        scraper.setHtml(html)
        posts = scraper.scrape()
        for post in posts:
            print(post, file=output)
        ns = scraper.getNavLinks()
        for n in ns:
            if 'Show more' in n[0]:
                url = n[1]
                break
        else:
            break
    i += 1
br.close()
output.close()
print('Done..........')
