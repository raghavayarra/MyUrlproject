import unittest
import dblayer


class MyTestCase(unittest.TestCase):
    def test_1_SetUp_db(self):
        
        try:
            response = dblayer.truncate_table()
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False
        
        finally:
            print("Currently Executing {}".format(self._testMethodName))
            print("To clear all the records before test cases start")

    def test_2_insert_record(self):
        
        try:
            request_url = 'http://youtube.com/safe'
            response = dblayer.insert_record(request_url)
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False

        finally:
            print("Currently Executing {}".format(self._testMethodName))
            print("Inserting record")

    def test_3_update_record(self):
        
        try:
            request_url = 'http://youtube.com/notsafe'
            response = dblayer.update_record(1, request_url, True)
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False

        finally:
            print("Currently Executing {}".format(self._testMethodName))
            print("Updating the record")

    
    def test_4_get_record_id(self):
        
        try:
            response = dblayer.get_record_by_id(1)
            if len(response) > 2:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False
        
        finally:
            print("Currently Executing {}".format(self._testMethodName))
            print("Reading one record")

    def test_5_get_all_record(self):
        
        try:
            response = dblayer.get_all_records()
            if len(response) > 2:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False

        finally:
            print("Currently Executing {}".format(self._testMethodName))
            print("Reading all record")

        
    
    def test_6_teardown_row(self):
        
        try:
            response = dblayer.truncate_table()
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False

        finally:
            print("Currently Executing Cleanup")
            print("Cleaning the DB after test cases are finished")

       

if __name__ == '__main__':
    unittest.main()