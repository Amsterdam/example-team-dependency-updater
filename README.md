# Readme

## Initiate project

Run this command to execute the following steps:
```
make init
```

**What this does:**

First clones into the dependency repo
```
git clone git@github.com:Amsterdam/dependency_updater.git
```

Then, installs `glab` and github CLI `gh`. And authenticates both
```
gh auth login
glab auth login
```

## Slack bot aanmaken

You need a Slack bot with these two scopes:
```
chat:write Send messages as @mobilab-bot
chat:write.customize Send messages as  @mobilab-bot
```
with a customized username and avatar

You can have this bot installed by a Slack admin (Timo Halbesma of Jeroen Vijverberg). 

Then you can add your bot to the channel of your choice

## Run the script 

Make sure the following environment variables are set:
```
SLACK_API_TOKEN
```

You can find the token in the Vault

Finally, run the script by other one of the following commands:

```
make run
OR
python main.py
```