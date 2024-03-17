#!/bin/bash

# Function to show usage
export shortcut_api_token="65e6a1cc-266a-4fa7-8ed5-67e0742b39d9"

usage() {
    echo "Usage:"
    echo "  $0 create_project -t TITLE -i TEAM_ID"
    echo "  $0 get_project -p PROJECT_ID"
    echo "  $0 find_project -f NAME"
    echo "Options:"
    echo "  -t TITLE        Set the project title"
    echo "  -i TEAM_ID      Set the team ID"
    echo "  -p PROJECT_ID   Set the project ID"
    echo "  -f NAME         Find the project by name"
    exit 1
}

# Function to create a project
create_project() {
    local team_id="$1"
    local title="$2"
   
    local api_url="https://api.app.shortcut.com/api/v3/projects"

    # Define the data payload
    local description="Project Description here"  # Placeholder description

    # Make the HTTP POST request to create the project
    curl -X POST "$api_url" \
        -H "Content-Type: application/json" \
        -H "Shortcut-Token: $shortcut_api_token" \
        -d "{\"name\": \"$title\", \"team_id\": $team_id, \"description\": \"$description\"}"

    echo "Project Created"
}

# Function to get a project
get_project() {
    local project_id="$1"

    local api_url="https://api.app.shortcut.com/api/v3/projects/$project_id"

    # Make the HTTP GET request to retrieve the project
    curl -X GET "$api_url" \
        -H "Content-Type: application/json" \
        -H "Shortcut-Token: $shortcut_api_token"
}

# Function to find a project by name
find_project() {
    local name="$1"
    local api_url="https://api.app.shortcut.com/api/v3/projects"

    # Make the HTTP GET request to retrieve the projects
    local response=$(curl -s "$api_url" \
        -H "Content-Type: application/json" \
        -H "Shortcut-Token: $shortcut_api_token")
  
    # Use jq to parse JSON and search for the project name
    echo "$response" | jq -r --arg name "$name" \
        '.[] | select(.name | test($name; "i")) | "\(.team_id) \(.name) \(.id)"'
}
update_project() {
    local project_id="$1"
    local new_progress_value=98
    local url="https://api.app.shortcut.com/api/v3/projects/$project_id"

    # Get the current project data
    local project_data=$(get_project "$project_id")
    local description=$(echo "$project_data" | jq -r '.description')
   
    # Update the progress in the description
     local updated_description=$(echo "$description" | sed -r "s/(\[Progress: )[^]]*(\])/\1$new_progress_value\2/")

    echo "$updated_description"
#     # Prepare the updated data
#     local updated_data=$(echo "$project_data" | jq --arg desc "$updated_description" '.description = $desc')

#     # Make the HTTP PUT request to update the project
#     curl -X PUT "$url" \
#         -H "Content-Type: application/json" \
#         -H "Shortcut-Token: $shortcut_api_token" \
#         -d "$updated_data"
}

# Main script
if [ $# -eq 0 ]; then
    usage
    exit 1
fi

command=$1
shift

while getopts ":t:i:p:f:" opt; do
    case $opt in
        t) title="$OPTARG" ;;
        i) team_id="$OPTARG" ;;
        p) project_id="$OPTARG" ;;
        f) name_find="$OPTARG" ;;
        \?) usage ;;
    esac
done

case $command in
    create_project)
        if [ -z "$title" ] || [ -z "$team_id" ]; then
            echo "Title and team ID are required for creating a project."
            usage
        else
            create_project "$team_id" "$title"
        fi
        ;;
    get_project)
        if [ -z "$project_id" ]; then
            echo "Project ID is required for getting a project."
            usage
        else
            get_project "$project_id"
        fi
        ;;
    find_project)
        if [ -z "$name_find" ]; then
            echo "Name is required for finding a project."
            exit 1
        else
            find_project "$name_find"
        fi
        ;;
        update_project)
        if [ -z "$project_id" ]; then
            echo "Name is required for finding a project."
            exit 1
        else
            update_project "$project_id"
        fi
        ;;
    *)
        usage
        ;;
esac
