import unittest
import requests


class ApiTest(unittest.TestCase):


    # To check GET request to returns the details of all urls.
    
    def test1_get_all_records(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/all"

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

        except Exception as e:
            print("Exception occured while get the table{}".format(e))

        finally:
            self.assertEqual(response.status_code,200)
            


    # To check POST request to create a new url.

    def test2_insert_record(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/add"
            create_url = "www.google.com"
            payload={'insert_url': create_url}
            files=[]
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)

        except Exception as e:
            print("Exception occured while get the table{}".format(e))

        finally:
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.text,"the insert_url is "+create_url)

    ## To check Update request to update that particular url.

    def test3_update_record(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/4"
            update_url="www.youtube.com"
            payload={'update_url': update_url}
            files=[]
            headers = {}

            response = requests.request("PUT", url, headers=headers, data=payload, files=files)

            self.assertEqual(response.status_code,200)

        except Exception as e:
            print("Exception occured while get the table{}".format(e))

        finally:
            self.assertEqual(response.status_code,200)
        


# To check GET_ID request to returns the single url.

    def test4_get_record_by_id(self):
            try:
                url = domain+":"+port+"/rest/api/v1/urlScanner/4"

                payload={}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)

            except Exception as e:
                print("Exception occured while get the table{}".format(e))

            finally:
                self.assertEqual(response.status_code,200)


    # To checking url is safe or unsafe.

    def test5_check_url(self):
        try:
            url = domain+":"+port+"/rest/api/v1/urlScanner/isSafeUrl?hostname=www.google.com&port=&originalpathquerystring="
            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

        except Exception as e:
                print("Exception occured while get the table{}".format(e))

        finally:
            self.assertEqual(response.status_code,400)


if __name__ == "__main__":
    domain = "http://192.168.55.104"
    port ="3200"
    unittest.main()
    

