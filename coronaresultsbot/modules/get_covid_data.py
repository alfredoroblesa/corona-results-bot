from coronaresultsbot.modules.utilities import get_html_soup
from coronaresultsbot.modules.utilities import clean_string


def get_covid_data(country):
    url = "https://www.worldometers.info/coronavirus/country/" + country + "/"
    soup = get_html_soup(url)

    if soup.find('title').text == "404 Not Found":
        msg = "Sorry, I did not get that. Try again."
        return msg

    header_div      = soup.find_all('div')[5]
    last_update     = header_div.find_all('div')[4].find_all('div')[3].string.strip()
    total_cases     = clean_string(header_div.find_all('span')[0].string)
    deaths          = clean_string(header_div.find_all('span')[1].string)
    recovered       = clean_string(header_div.find_all('span')[2].string)

    flag_icons = {  "spain": "🇪🇸",
                    "italy": "🇮🇹",
                    "france": "🇫🇷",
                    "germany": "🇩🇪",
                    "china": "🇨🇳",
                    "us": "🇺🇸",
                    "uk": "🇬🇧"}

    countries_dic = {"spain": "Spain",
                    "italy": "Italy",
                    "france": "France",
                    "germany": "Germany",
                    "china": "China",
                    "us": "United States",
                    "uk": "United Kingdom"}

    if country == 'spain':
        info_url = "https://www.elconfidencial.com/tecnologia/ciencia/2020-03-15/coronavirus-ultimos-datos-espana-mundo_2497567"
        msg = "{} {}\n*Coronavirus Cases: {}\nDeaths: {}\nRecovered: {}*\n\n{}\n\nMore info at: [{}]({})".format(flag_icons[country],countries_dic[country].upper(),total_cases,deaths,recovered,last_update,info_url,info_url)
    elif country in countries_dic:
        msg = "{} {}\n*Coronavirus Cases: {}\nDeaths: {}\nRecovered: {}*\n\n{}".format(flag_icons[country],countries_dic[country].upper(),total_cases,deaths,recovered,last_update)
    else:
        msg = "{}\n*Coronavirus Cases: {}\nDeaths: {}\nRecovered: {}*\n\n{}".format(country.upper(),total_cases,deaths,recovered,last_update)

    return msg