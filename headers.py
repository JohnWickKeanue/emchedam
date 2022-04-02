
import requests

cookies = {
    'country': 'IN',
    'display-language': 'en',
    'xaccesstoken': 'eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInBsYXRmb3JtX2NvZGUiOiJXZWJAJCF0Mzg3MTIiLCJpc3N1ZWRBdCI6IjIwMjItMDQtMDJUMDA6MzA6MDIrMDAwMCIsInR0bCI6ODY0MDB9.4RH1dilEOHsahhdu2HN6d2tnY8PN41OJUcJYJxjgu3I',
    '_iidt': 'dS+vqnGyj/Ii2D/dGXqtlOUvY9nspR/2tPpNFejNYNqzaygaqWwpHyMM9tcGgpYYxZeQdqmut0JVSQ==',
    '_vid_t': 'ogQZMIxW1ghOkGVu05qe+j9hftRG0nAAmAyLS5EcEgDGWIipaBIxNilqg4N1J1MLOtwtvK3DjF5PGA==',
    'G_ENABLED_IDPS': 'google',
    'state': 'TG',
    'content-language': 'en,te',
    'g_state': '{"i_t":1648962961136,"i_l":0}',
    'user-type': 'premium',
    'refreshToken': '677e4461e431ac87698fe96f023162c8b81a509a67be31de8d64ad92ae96480e',
    'WZRK_S_RKW-4R7-785Z': '%7B%22p%22%3A1%7D',
    'ssoToken': '883efedd7287347c72e6862dc43443f2',
}

headers = {
    'authority': 'www.zee5.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99"',
    'accept': '*/*',
    'sec-ch-ua-mobile': '?1',
    'save-data': 'on',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; M2012K11AI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.94 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.zee5.com/signin',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'country=IN; display-language=en; xaccesstoken=eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInBsYXRmb3JtX2NvZGUiOiJXZWJAJCF0Mzg3MTIiLCJpc3N1ZWRBdCI6IjIwMjItMDQtMDJUMDA6MzA6MDIrMDAwMCIsInR0bCI6ODY0MDB9.4RH1dilEOHsahhdu2HN6d2tnY8PN41OJUcJYJxjgu3I; _iidt=dS+vqnGyj/Ii2D/dGXqtlOUvY9nspR/2tPpNFejNYNqzaygaqWwpHyMM9tcGgpYYxZeQdqmut0JVSQ==; _vid_t=ogQZMIxW1ghOkGVu05qe+j9hftRG0nAAmAyLS5EcEgDGWIipaBIxNilqg4N1J1MLOtwtvK3DjF5PGA==; G_ENABLED_IDPS=google; state=TG; content-language=en,te; g_state={"i_t":1648962961136,"i_l":0}; user-type=premium; refreshToken=677e4461e431ac87698fe96f023162c8b81a509a67be31de8d64ad92ae96480e; WZRK_S_RKW-4R7-785Z=%7B%22p%22%3A1%7D; ssoToken=883efedd7287347c72e6862dc43443f2',
}

response = requests.get('https://www.zee5.com/', headers=headers, cookies=cookies)
