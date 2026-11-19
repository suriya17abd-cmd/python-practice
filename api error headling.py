import requests 
def get_post(post_id):
    url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    try:
        response=requests.get(url,timeout=5)
        print("status_code:",response.status_code)
        response.raise_for_status()
        data=rsponse.json()
        print("title:",data["title"]) 
    except requests.exceptions.Timeout:
        print("Error:request timeout")
    except requests.exceptions.ConnectionError:
        print("Error:check your network connection")
    except requests.exceptions.HTTPError as error:
        print("HTTP Error:",error)
    except ValueError:
        print("Error:Invaild json response")
    except requests.exceptions.RequestException as error:
        print(" requests Error:",error)
    except NameError as e:
        print("Name Error:",e)
print("Testing vaild api requests")
get_post(4)
print("Testing invaild api requests")
get_post(99999)