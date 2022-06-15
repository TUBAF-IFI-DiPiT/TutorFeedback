import pandas as pd


def generateTable(localRun = False):
  url = "https://raw.githubusercontent.com/TUBAF-IFI-DiPiT/TutorFeedback/gh-pages/anonym_repos.csv"
  if localRun:
    anonym_pdRepositories = pd.read_csv(url)
  else:
    from pyodide.http import open_url
    from js import console
    url_content = open_url(url)
    anonym_pdRepositories = pd.read_csv(url_content)
  print(anonym_pdRepositories.shape)

  anonym_pdRepositories['commit_count'] = anonym_pdRepositories['commit_count'] - 2
  result = anonym_pdRepositories[(anonym_pdRepositories.year == 2022) & (anonym_pdRepositories.task == 3)][['teamKey', 'branch_count', 
                                                            'commit_count', 'release_count', 'stars']]
                                                  
  if localRun:
    print(result)
  return result

if __name__ == "__main__":
  generateTable(localRun = True)