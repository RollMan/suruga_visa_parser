from bs4 import BeautifulSoup
import pathlib

def parser(path):
    with open(path, 'r', encoding='shift_jis') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', class_="table-type2 clear margin-b-10px")

    tr_list = table.find_all('tr')[2:]

    dest_amount = [tr.find_all('td') for tr in tr_list]
    dest_amount = [(td[0].get_text(strip=True), int(td[1].get_text(strip=True).replace(',', ''))) for td in dest_amount]

    return dest_amount

def main():
    monthes = [202012, 202101, 202102, 202103, 202104, 202105, 202106, 202107, 202108, 202109, 202110, 202111]
    pay = {}
    for month in monthes:
        dest_amount = parser(pathlib.Path(str(month) + ".html"))
        for dest, amount in dest_amount:
            if dest not in pay:
                pay[dest] = amount
            else:
                pay[dest] += amount

    for k, v in pay.items():
        print(k, '\t', v)

if __name__ == '__main__':
    main()
