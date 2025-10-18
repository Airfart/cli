# Git Instructions

* Installation and Setup
* Connecting Git with Tools
* Resolving Conflicts
* Links

git config --global instructies, maarja dan gaat ie zeiken over REFS

## Resolving Conflicts

### Fixing Commit conflicts:

 1 Wanneer commiten niet lukt kun je dit proberen:
 - Je laatste commit terug draaien naar HEAD.
 - Meerdere commits bv. 8x terug gaan met 8~HEAD

 2 Branche conflicts:
 - https://stackoverflow.com/questions/13106179/error-fatal-not-possible-to-fast-forward-aborting

 Understandig - http://graphite.dev/guides/git-fast-forward-merge

 Is dit een git commando? Waarom staat dit in deze file?
Forcing Password Change:
You can force a user to change their password at their next login by expiring the password with the command 

$sudo passwd -e <username> or $sudo chage -d 0 <username>.

Check all the users with $cut -d: -f1 /etc/passwd

Delete user with $sudo deluser <username>