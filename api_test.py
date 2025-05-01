import requests

url = "https://www.google.com/search?q=iphone+16+pro+max&sca_esv=1740ddc3d2160827&sxsrf=AHTn8zoP2gyXUNamWenN4UX7H9J07htTKw%3A1746121467550&ei=-7ITaICzIcmt4-EP5NHZqQ4&ved=0ahUKEwjAnLuu6YKNAxXJ1jgGHeRoNuUQ4dUDCA8&oq=iphone+16+pro+max&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWlwaG9uZSAxNiBwcm8gbWF4SABQAFgAcAB4AZABAJgBAKABAKoBALgBDMgBAJgCAKACAJgDAJIHAKAHALIHALgHAA&sclient=gws-wiz-serp"

resp = requests.get(url)
print(resp)
assert resp.status_code == 200
content = resp.content
print(content)
print(type(content))
readable_response = content.decode('utf-8')
print(readable_response)
