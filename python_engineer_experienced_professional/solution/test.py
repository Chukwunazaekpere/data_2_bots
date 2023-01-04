import unittest
from reader import json_reader
import os
import logging



class JSONReaderTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.json_reader_logger = logging.getLogger("JSON_reader")
        logging.basicConfig(level=logging.INFO)
        logging.info("\n\t The test setup started.......")
        self.file_index = 1
        self.file_path = os.path.join(os.path.dirname(__file__), f"../data/data_{self.file_index}.json")


    def test_logs_merry_text_on_successful_write(self):
        logging.info("\n\t testing test_logs_merry_text_on_successful_write.......")
        with self.assertLogs(self.json_reader_logger, level="INFO")as log_test:
            self.reader = json_reader(self.file_path, self.file_index)
            self.assertEqual(['INFO:JSON_reader:Operation fiinished successfully'], log_test.output)
    
    def test_raises_error_for_no_message_attribute(self):
        logging.info("\n\t testing test_raises_error_for_no_message_attribute.......")
        with self.assertRaises(AttributeError)as attr_err:
            self.reader = json_reader(self.file_path, self.file_index)
            self.assertEqual("ERROR:JSON_reader:This data file has no 'message' attribute.", str(attr_err.exception))


# run test
unittest.main()