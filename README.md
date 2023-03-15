### Readme

First clone into the dependency repo

```git clone git@github.com:Amsterdam/dependency_updater.git```

Then, install `glab` and github CLI `gh`. And authenticate both

```
gh auth login
glab auth login
```

Make sure the following environment variables are set:

```
SLACK_API_TOKEN
```

You can find the token in the Vault

Finally, run the script

```
python main.py
```