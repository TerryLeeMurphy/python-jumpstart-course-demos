import headers
import collections
import requests
import bs4

# Create a named tuple to store the weather report
# this scoped here to be global for all functions in the program

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')

def main():
    ds = 72  # set display size
    headers.dashes_line(ds)
    title = 'W e a t h e r  A p p'
    headers.print_header(title, ds)
    headers.dashes_line(ds)
    state = get_input('state')
    city = get_input('city')
    location = collections.namedtuple('Location', 'state, city')
    l = location(state, city)
    #print(l)
    print()
    headers.dashes_line(ds)
    html = get_html(state, city)
    report = get_weather(html)
    print('Current Conditions in {} are {} and {}{}'.format(
        report.loc,
        report.cond,
        report.temp,
        report.scale
    ))
    headers.dashes_line(ds)
    print('Goodbye')

def get_input(what):
    if what == 'state':
        default = 'TN'
    elif what == 'city':
        default = 'Gladeville'
    else:
        default = 'Unknown'
    message = 'To report on current weather conditions please enter the {} i.e. {} : '.format(
        what, default)
    userinput = input(message)
    if userinput == '':
        userinput = default
    return userinput


def get_html(state, city):
    url = 'https://www.wunderground.com/weather/us/{}/{}'.format(
        state.lower().strip(), city.lower().strip())
    response = requests.get(url)
    # print(response.text[0:512])
    return response.text


def get_weather(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    # strip some unneeded crap out the header h1
    loc = soup.find('h1').get_text() \
        .replace(' Weather Conditions', '') \
        .replace('star_ratehome', '')
    # print(loc)
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()
    loc = cleanup(loc)
    condition = cleanup(condition).lower()
    temp = cleanup(temp)
    scale = cleanup(scale)
    report = WeatherReport(cond=condition,temp=temp,scale=scale,loc=loc)
    return report

def cleanup(text: str):
    if not text:
        return text

    text = text.strip()
    return text

if __name__ == '__main__':
    main()
