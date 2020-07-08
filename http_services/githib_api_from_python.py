import requests

def main():
    pass

def get_repo_info():
    user = input("What is the username? ").strip()
    repo = input("What is the repo name? ").strip()

    return user, repo

if __name__ == '__main__':
    main()