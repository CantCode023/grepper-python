import unittest
from unittest.mock import patch

from grepper_python import Grepper
from grepper_python.exceptions import *


class Test(unittest.TestCase):
    def setUp(self):
        self.api_key = "my_api_key"  # Replace with your actual API key
        self.grepper = Grepper(self.api_key)

    @patch("requests.get")
    def test_fetch_answer_success(self, mock_get):
        # Mock successful API response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 12345,
            "title": "Sample answer title",
            "content": "Sample answer content",
            "author_name": "John Doe",
            "author_profile_url": "https://www.example.com/johndoe",
            "upvotes": 10,
            "downvotes": 0,
        }

        # Call the function
        answer = self.grepper.fetch_answer(12345)

        # Assertions
        self.assertEqual(answer.id, 12345)
        self.assertEqual(answer.title, "Sample answer title")
        self.assertEqual(answer.content, "Sample answer content")
        self.assertEqual(answer.author_name, "John Doe")
        self.assertEqual(answer.author_profile_url, "https://www.example.com/johndoe")
        self.assertEqual(answer.upvotes, 10)
        self.assertEqual(answer.downvotes, 0)

    @patch("requests.get")
    def test_fetch_answer_not_found(self, mock_get):
        # Mock API response with 404 status code
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.text = "Not Found"

        # Call the function and expect an exception
        with self.assertRaises(NotFound) as cm:
            self.grepper.fetch_answer(12345)

        self.assertEqual(str(cm.exception), "HTTPException: Not Found")

    @patch("requests.get")
    def test_fetch_answer_other_error(self, mock_get):
        # Mock API response with unexpected status code
        mock_response = mock_get.return_value
        mock_response.status_code = 500
        mock_response.text = "Internal Server Error"

        # Call the function and expect an exception
        with self.assertRaises(Exception) as cm:
            self.grepper.fetch_answer(12345)

        self.assertEqual(
            str(cm.exception),
            "HTTPException: Unexpected status code: 500 (Internal Server Error)",
        )


if __name__ == "__main__":
    unittest.main()