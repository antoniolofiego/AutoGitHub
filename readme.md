# AutoGitHub

Automate your Git/GitHub project creation.

- Creates a GitHub repo with your project's name
- Creates a local folder with an empty README.md file
- Initializes a git repo in the folder
- Pushes the first commit to the GitHub repo


## Install

```
git clone "https://github.com/antoniolofiego/AutoGitHub"
cd AutoGitHub
pip install -r requirements.txt
```
Change the ```credentials.json``` file with your GitHub username and access token (you can learn how to create one here: https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).

It should look like:
```
{
    "YOUR-GITHUB-USERNAME": "YOUR-GITHUB-ACCESS-TOKEN" 
}
```

To use it, you can run the following code:

```
cd AutoGitHub
source create.sh; create !YOUR-GITHUB-USERNAME !PROJECT-NAME
```
or you can add it to your path and run it from anywhere.

#### Example
```
cd AutoGitHub
source create.sh; create antoniolofiego MyNewProject
```
