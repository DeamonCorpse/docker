# DOCKER REPOSITORY

I have been experimenting and using Docker for a good while now but I just recently decided to take advantage of git & github to store my files in case it might benefit someone.

This repository stores both my current and archived docker run, docker compose, docker stack and docker swarm files. I have also started to re-write the stack files I am currently using with variables to facilitate re-deployment later and ensure more portability between systems.
<hr>
<br>

# REPOSITORY FOLDERS
### docker-application-stacks
- Docker stack files which contain **more than one application to be deployed**.
- **This is where the most current files are**.
<br>
<br>
> The next folders are mainly kept for historical purpose and reference
### docker-compose
- You guessed it. This is where I store my compose files
<br>

### docker-individual-stacks
- As the name suggests, there are stack files but they each **deploy only one application**.
- I tend to group applications based on their functionality so this folder is not used much and is kept *mainly for historical purpose and reference*.
<br>

### docker-run
- Although I do prefer to use stacks, I also sometimes use docker-run to have a look at an application and see if I want to use it.
<br>

### docker-swarm
- Watching all the "kings and queens of ducker" on youtube, I was convinced docker swarm was the way to go...Turned out if was not.
<br>
<hr>
Feel free to use whatever helps in your docker adventures!
