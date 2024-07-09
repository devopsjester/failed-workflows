# Failed Workflows Finder

## Overview
This script is designed to find and list all failed workflow runs for a specific workflow within an organization's repositories on GitHub. It iterates through each repository in the organization, checks for failed runs of the specified workflow, and collects this information into a list.

## How It Works
1. The script starts by fetching a list of repositories for the given organization name through the `get_repos(org_name)` function.
2. For each repository, it retrieves the name and then fetches the workflow runs that have failed for the specified workflow name using the `get_workflow_runs(repo_name, workflow_name)` function.
3. If there are any failed workflow runs, it appends a tuple containing the repository name and the failed runs to the `failed_workflows` list.
4. Finally, the script returns the list of failed workflows, where each item in the list is a tuple with the repository name and the failed workflow runs.

## How to Run
To run this script, you need to have Python installed on your system. Follow these steps:

1. Ensure you have the necessary dependencies installed. This script requires a GitHub API client library. You can install it using pip:
```
pip install requests
```
2. Define the `get_repos(org_name)` and `get_workflow_runs(repo_name, workflow_name)` functions. These functions should interact with the GitHub API to fetch repositories for an organization and workflow runs for a repository, respectively.

3. Save the script in a file, for example, `failed-workflows.py`.

4. Run the script from the terminal:
```
python failed-workflows.py
```
Note: You may need to modify the script to include your GitHub API credentials and specify the organization and workflow name you want to check.

For more detailed instructions on setting up the GitHub API client and authentication, refer to the documentation of the GitHub API client library you are using.
