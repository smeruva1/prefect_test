from prefect import flow
from prefect.filesystems import GitHub

github_block = GitHub.load("github")

@flow
def my_favorite_function():
    print("What is your favortie number? ")
    
if __name__ == "main":
    my_favorite_function()