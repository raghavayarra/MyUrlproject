import pytest
import dblayer

class Testing():
    

    def test_1_insert_record(self):
        global dblayer
        
        try:
            my_url = 'http://www.facebook.com'
            response = dblayer.insert_record(my_url)
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False

    def test_2_update_record(self):
        
        try:
            request_url = 'http://www.youtube.com/'
            response = dblayer.update_record(1, request_url, True)
            if response == 1:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
            assert False

        finally:
            print("Updating the record")

    
    def test_3_get_record_id(self):
        
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
            
            print("Reading one record")

    def test_4_get_all_record(self):
        
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
            
            print("Reading all record")

        
    
    def test_5_teardown_row(self):
        
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




       
