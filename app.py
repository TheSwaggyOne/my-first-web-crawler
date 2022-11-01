from warcio.archiveiterator import ArchiveIterator
import re
import requests

from bs4 import BeautifulSoup

regex = re.compile(
    "COVID|Pandemic|Outbreak|Quarantine|Self-isolation|Isolation|Social distance|due to covid|economic impact of "
    "COVID-19", re.IGNORECASE
)

entries = 0
matching_entries = 0
hits = 0

file_name = "https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-05/segments/1642320299852.23/warc/CC-MAIN" \
            "-20220116093137-20220116123137-00000.warc.gz "


stream = None
if file_name.startswith("http://") or file_name.startswith(
        "https://"
):
    stream = requests.get(file_name, stream=True).raw
else:
    stream = open(file_name, "rb")

for record in ArchiveIterator(stream):
    if record.rec_type == "warcinfo":
        continue

    if not record.http_headers:
        continue

    # print(record.rec_headers.get_header('WARC-Target-URI'))
    # print(record.content_stream().read().decode("utf-8", "replace"))
    # print('')

    url = record.rec_headers.get_header('WARC-Target-URI')

    entries = entries + 1

    contents = (
        record.content_stream()
        .read()
        .decode("utf-8", "replace")
    )
    soup = BeautifulSoup(contents, 'html.parser')
    flag = False
    for p in soup.find_all('p', string=True):

        m = regex.search(p.string)

        if m:
            flag = True

    for t in soup.find_all('title', string=True):
        m = regex.search(t.string)

        if flag and m:
            url = record.rec_headers.get_header('WARC-Target-URI') + "\n"
            print(m)
            print(soup.find_all('title'))
            matching_entries = matching_entries + 1
            print(url)

            result = open("result.txt", "a")
            result.write(url + "\n")
            result.close()

    print(entries, matching_entries)


