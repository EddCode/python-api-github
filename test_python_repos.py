from unittest import TestCase, mock
from requests import Response

import python_repos

class TestMockValue(TestCase):

    @mock.patch('requests.get')
    def test_mock_value(self, mock_requests):
        call_response = {
                "total_count": 16489327,
                "incomplete_results": True,
                "items": [
                    {
                        'name': 'my repo',
                        'html_url': 'https://github.com/my-user/my-repo',
                        'description': 'A list of all Python repos on GitHub',
                        'stargazers_count': '1,000,000',
                        'owner': {
                            'login': 'jeffreybiles',
                            'html_url': '',
                            'avatar_url': ''
                        }
                    }
                ]
        }

        mock_requests.return_value.status_code.return_value = 200
        mock_requests.return_value.json.return_value = call_response

        repos = python_repos.get_repos_list('javascript')

        mock_requests.assert_called_with(
            'https://api.github.com/search/repositories?q=language:javascript&sort=stars',
            headers={'Accept': 'application/vnd.github.v3+json'}
        )

        self.assertEqual(len(repos['data']), 1)
        self.assertEqual(len(repos['data'][0]['x']), 1)
        self.assertEqual(repos['data'][0]['x'][0], '<a href="https://github.com/my-user/my-repo">my repo</a>')
        self.assertEqual(len(repos['data'][0]['y']), 1)
        self.assertEqual(repos['data'][0]['y'][0], '1,000,000')

