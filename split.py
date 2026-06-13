def text_split():
    url = "192.2.100.1"
    url_data = url.split(".")
    print(url_data[2])


if __name__ == "__main__":
    text_split()
