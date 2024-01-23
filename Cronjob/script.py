import http.client


def make_api_request():
    api_host = "backend"
    port = 8000
    api_path = "/match/matchscript/create"
    api_method = "POST"

    # import pdb; pdb.set_trace()
    connection = http.client.HTTPConnection(api_host, port=port)

    headers = {}

    try:
        connection.request(api_method, api_path, headers=headers)
        response = connection.getresponse()
        print(f"Status Code: {response.status}")
        print("Response Data:")
        print(response.read().decode('utf-8'))
    except Exception as e:
        print(f"An error ocurred {e}")
    finally:
        connection.close()


if __name__ == "__main__":
    make_api_request()
