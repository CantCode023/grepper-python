import unittest
from unittest.mock import patch

from grepper_python import Grepper


class TestGrepper(unittest.TestCase):
    def setUp(self):
        self.api_key = "my_api_key"
        self.grepper = Grepper(self.api_key)

    @patch("requests.post")
    def test_update_answer_success(self, mock_post):
        # Mock successful API response (without modifying data)
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Answer updated successfully"}

        # Call the function (simulating the update)
        answer_id = 12345  # Replace with the ID of an answer you have permission to update
        new_content = "updated content"  # Replace with the desired update

        # Assertions (limited due to mocking)
        self.grepper.update_answer(answer_id, new_content)
        mock_post.assert_called_once_with(  # Verify API call with placeholders
            f"https://api.grepper.com/v1/answers/{answer_id}",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=f"answer[content]={new_content}",
            auth=(self.api_key, ""),
        )

    @patch("requests.post")
    def test_update_answer_error(self, mock_post):
        # Mock API error response
        mock_response = mock_post.return_value
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"

        # Call the function and expect an exception
        with self.assertRaises(Exception) as cm:
            self.grepper.update_answer(12345, "new answer content")

        # Assertions (limited due to mocking)
        self.assertEqual(str(cm.exception).startswith("HTTPException:"), True)


if __name__ == "__main__":
    unittest.main()