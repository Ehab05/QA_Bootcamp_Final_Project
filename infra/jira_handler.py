import os
from jira import JIRA

from infra.json_file_handler import JsonFileHandler


class JiraHandler:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(base_dir, '../demo_blaze_config.json')
        self._config = JsonFileHandler().load_from_file(self._config_file_path)
        private_file_path = os.path.join(base_dir, '../private.json')
        self._secret = JsonFileHandler().load_from_file(private_file_path)
        self._jira_url = self._config["jira_url"]
        self._auth_jira = JIRA(
            basic_auth=(self._config["jira_email"], self._secret["api_token"]),
            options={'server': self._jira_url}
        )

    def create_issue(self, project_key, summary, description, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }

        return self._auth_jira.create_issue(fields=issue_dict)

    def issue_description(self, error, test_case):
        # Sanitize inputs to remove newline characters
        sanitized_error = error.replace('\n', ' ').replace('\r', '')
        sanitized_test_case = test_case.replace('\n', ' ').replace('\r', '')

        # Generate issue description for the Jira report
        return f"{sanitized_error} in Test Case: {sanitized_test_case}"
