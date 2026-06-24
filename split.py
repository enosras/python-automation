import webhooks_client


def text_split():
    url = "192.2.100.1"
    url_data = url.split(".")
    print(f"{url_data[2]}+{url_data[3]}")


if __name__ == "__main__":
    # text_split()
    outputest = webhooks_client.doc()
    print(outputest)
