import requests

# Replace these values with your organization name and workflow name
ORG_NAME = 'your-org-name'
WORKFLOW_NAME = 'your-workflow-name'
GITHUB_TOKEN = 'your-github-token'

def get_repos(org_name):
    url = f'https://api.github.com/orgs/{org_name}/repos'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_workflow_runs(repo_name, workflow_name):
    url = f'https://api.github.com/repos/{ORG_NAME}/{repo_name}/actions/runs'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    params = {'per_page': 100}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return [run for run in response.json()['workflow_runs'] if run['name'] == workflow_name and run['conclusion'] == 'failure']

def find_failed_workflows(org_name, workflow_name):
    repos = get_repos(org_name)
    failed_workflows = []
    
    for repo in repos:
        repo_name = repo['name']
        failed_runs = get_workflow_runs(repo_name, workflow_name)
        if failed_runs:
            failed_workflows.append((repo_name, failed_runs))
    
    return failed_workflows

if __name__ == '__main__':
    failed_workflows = find_failed_workflows(ORG_NAME, WORKFLOW_NAME)
    if failed_workflows:
        for repo_name, runs in failed_workflows:
            print(f'Repo: {repo_name}')
            for run in runs:
                print(f'  Workflow run ID: {run["id"]}, URL: {run["html_url"]}')
    else:
        print('No failed workflows found.')
