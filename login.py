import requests

# can be configurable based on use case
USERNAME = "nilepatest001"
PASSWORD = "Password@1"
url = "https://clarity.dexcom.com/users/auth/dexcom_sts"
# Defining headers
headers = {"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
# using session obj
with requests.session() as session:
    loginPage = session.get(url, headers=headers)
    print(loginPage.history)
    print(loginPage.status_code) # Returns 200
    loginPage.cookies.get_dict()

    # capture cookies from redirect
    loginPage.history[0].cookies.get_dict(), loginPage.history[1].cookies.get_dict()

    # Cookies are in multiple redirects, add them to the request cookie
    cookies = loginPage.cookies.get_dict()
    for hist in loginPage.history:
        print(hist.cookies.get_dict())
        cookies.update(hist.cookies.get_dict())

    token = loginPage.cookies.get_dict()
    print(token)
    # building payload to send to post request
    payload = {"username": USERNAME, "password": PASSWORD}
    payload.update(token)
    r2 = session.post(loginPage.url, data=payload, headers=headers, cookies=cookies)
    print("Status code:", r2.status_code)
    print("Content: \n", r2.content)
