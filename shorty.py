import click
import requests

@click.group()
def cli():

    pass






@cli.command()
@click.option('-wf', '--workflowId', 'wf', default=17523, help='workflow id')
@click.option('-t', '--title', 'title', required=True, help='Project Title')
def create_project(wf, title):

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
        "team_id": wf,
        "updated_at": "2016-12-31T12:30:00Z"
    }

    api_url = "https://api.app.shortcut.com/api/v3/projects"
    response = requests.post(api_url, headers=headers, json=data_payload)

    click.echo('Project Created: 123')

@cli.command()
def find_project():
    click.echo('Dropped the database')


@cli.command()
def update_project():
    click.echo('updated Description')


cli.add_command(create_project)
cli.add_command(update_project)
cli.add_command(find_project)


if __name__ == '__main__':
    cli()