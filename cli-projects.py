import click
import requests

@click.group()
def cli():
    """Simple CLI tool to interact with a fictional API."""
    pass

@click.command()
@click.argument('user_id')
def fetch_user(user_id):
    shortcut_api_token = '65e6a1cc-266a-4fa7-8ed5-67e0742b39d9'

    headers = {
    'Content-Type': 'application/json',
    'Shortcut-Token': shortcut_api_token,
}
    """Fetches and displays user information based on USER_ID."""
    api_url = f"https://api.app.shortcut.com/api/v3/projects"
    response = requests.get(api_url,headers=headers)
    
    if response.status_code == 200:
        user_info = response.json()
        click.echo(user_info)
        # click.echo(f"ID: {user_info['id']}")
        # click.echo(f"Name: {user_info['name']}")
        # click.echo(f"Color: {user_info['color']}")
        # click.echo(f"Created At: {user_info['created_at']}")
        # click.echo(f"Archived: {user_info['archived']}")
        # click.echo(f"Team ID: {user_info['team_id']}")
    else:
        click.echo("Failed to fetch user information.")




@click.command()
@click.argument('user_id')
def fetch_workflow(user_id):
    shortcut_api_token = '65e6a1cc-266a-4fa7-8ed5-67e0742b39d9'
    headers = {
        'Content-Type': 'application/json',
        'Shortcut-Token': shortcut_api_token,
    }
    data_payload = {
    "abbreviation": "foo",
    "color": "#6515dd",
    "created_at": "2016-12-31T12:30:00Z",
    "description": 'test',
    "external_id": "foo",
    "follower_ids": [],
    "iteration_length": 1,
    "name": 'My Test',
    "start_time": "2016-12-31T12:30:00Z",
    "team_id": 17523,
    "updated_at": "2016-12-31T12:30:00Z"
}

# The API URL for creating a new project
    api_url = "https://api.app.shortcut.com/api/v3/projects"

# Making the POST request
    response = requests.post(api_url, headers=headers, json=data_payload)

   
    click.echo(response.json())
    







cli.add_command(fetch_user)
cli.add_command(fetch_workflow)




if __name__ == '__main__':
    cli()


