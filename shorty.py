import click
import requests
import json
import re
@click.group()
def cli():

    pass


@cli.command()
@click.option('-tm', '--team-id', 'team_id', default=17523, help='team id')
@click.option('-t', '--title', 'title', required=True, help='Project Title')
def create_project(team_id, title):

    shortcut_api_token = '65e6a1cc-266a-4fa7-8ed5-67e0742b39d9'
    headers = {
        'Content-Type': 'application/json',
        'Shortcut-Token': shortcut_api_token,
    }
    data = {
        'budget': '',
        'budget_date': '',
        'start_date': '',
        'end_date': '',
        'contract_process': '',
        'milestones': '',
        'progress': '',
        'note': '',
        'link_eoi': '',
        'link_paper': '',
        'link_original_github': '',
        'link_proposal': '',
        'link_product_github': '',
        'link_notes': '',
        'link_sharepoint': '',
        'link_shortcut': '',
        'contacts': '',
        'summary': '',
        'link_resources_folder': ''
    }

# Create the description using f-strings
    description = f"""[Budget ${data['budget']}] Matched to spent {data['budget_date']}
    [Rate Research]
    [Start {data['start_date']}]
    [End {data['end_date']}]
    [Contract Executed] Process: {data['contract_process']}
    [Milestone: {data['milestones']}]
    [Progress: {data['progress']}]
    [Note: {data['note']}]
    [Links :: [EoI]({data['link_eoi']}), [Paper]({data['link_paper']}), [Original GitHub]({data['link_original_github']}), [Proposal]({data['link_proposal']}), [Product GitHub]({data['link_product_github']}), [Notes]({data['link_notes']}), [Sharepoint]({data['link_sharepoint']}), [Shortcut]({data['link_shortcut']}) ]
    Contacts
    {data['contacts']}
Summary
{data['summary']}
Resources
[Sharepoint Folder]({data['link_resources_folder']})
    """
    data_payload = {
        "abbreviation": "foo",
        "color": "#6515dd",
        "created_at": "2016-12-31T12:30:00Z",
        "description": description,
        "external_id": "foo",
        "follower_ids": [],
        "iteration_length": 1,
        "name": title,
        "start_time": "2016-12-31T12:30:00Z",
        "team_id": team_id,
        "updated_at": "2016-12-31T12:30:00Z"
    }

    api_url = "https://api.app.shortcut.com/api/v3/projects"
    response = requests.post(api_url, headers=headers, json=data_payload)

    click.echo('Project Created: 123')

@cli.command()
@click.option('-pid', '--project-id', 'projectId', help='project id')
def get_project(projectId):
    shortcut_api_token = '65e6a1cc-266a-4fa7-8ed5-67e0742b39d9'

    headers = {
        'Content-Type': 'application/json',
        'Shortcut-Token': shortcut_api_token,
    }
    project_public_id = projectId
    """Fetches and displays user information based on USER_ID."""
    api_url = f"https://api.app.shortcut.com/api/v3/projects/{project_public_id}"
    response = requests.get(api_url, headers=headers)
    click.echo(response.json()['description'])
    return response.json()['description']


@cli.command()
@click.option('-n', '--name', 'name', help='name')
def find(name):
    shortcut_api_token = '65e6a1cc-266a-4fa7-8ed5-67e0742b39d9'
    headers = {
        'Content-Type': 'application/json',
        'Shortcut-Token': shortcut_api_token,
    }

    api_url = f"https://api.app.shortcut.com/api/v3/projects"
    response = requests.get(api_url, headers=headers)
    # click.echo(response.json())

    escaped_search_term = re.escape(name)

    pattern_string = r"\s*".join(escaped_search_term)
    pattern = re.compile(pattern_string, re.IGNORECASE)

# Filter projects that match the regex pattern
    filtered_projects = [
        project for project in response.json() if pattern.search(project['name'])]
    # click.echo(filtered_projects)
    for project in filtered_projects:
        print(
            f"Team-ID: {project['team_id']}, Name: {project['name']}, Project ID: {project['id']} ")
    # print(filtered_projects)


# def update_description(description, updates):
#     if "progress" in updates:
#         description = re.sub(
#             r'\[Progress: .+?\]', f"[Progress: {updates['progress']}]", description)
#     if "link_eoi" in updates:
#         description = re.sub(
#             r'(\[EoI\]\().+?(\))', r'\g<1>' + updates['link_eoi'] + r'\2', description)
#     return description


@cli.command()
@click.option('-pid', '--project-id', 'projectId', help='project id')
@click.option('-p', '--progress', 'progress', help='progress')
@click.option('-bdj', '--budget', 'budget', help='budget')
def update(projectId=17596, progress=34, budget=False):
    url = f"https://api.app.shortcut.com/api/v3/projects/17596"
    shortcut_api_token = '65e6a1cc-266a-4fa7-8ed5-67e0742b39d9'

    headers = {
        'Content-Type': 'application/json',
        'Shortcut-Token': shortcut_api_token
    }
    data = get_project(projectId)
    progress_pattern = r"\[Progress: (\d+)%\]"

# Replacement percentage (e.g., updating progress to 75%)
    new_progress_value = "75"

# Perform replacement
    data = re.sub(progress_pattern, f"[Progress: {new_progress_value}%]", data)


    response = requests.put(url, headers=headers, json=data)
    click.echo(response.json())







cli.add_command(create_project)
cli.add_command(update)
cli.add_command(find)
# cli.add_command(get_project)


if __name__ == '__main__':
    cli()