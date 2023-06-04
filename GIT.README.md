# The perfect commit
- Each commit will show only one topic or concept
- In case have edit multi topic in one file, we can use command ```git add -p <filename>``` to choose what part of this file will be commit first or later
- <b>The perfect commit message</b>:
    - Subject: concise <i>summary of what happened</i>
    - Body: more detail explanation
        - What is now different than before?
        - What's the reason for the change?
        - Is there anything to watch out for/ anything particularly remarkable? (Có điều gì đặc biệt đáng chú ý hay cần chú ý không?)

# Branching Strategies
- Integrating Changes & Structuring Releases
    - Mainline Development ("Always Be Integrating")
        - Long-Running Branches
            - exist through the complete lifetime of the project
            - often, they mirror "stages" in your dev life cycle
            - common convention: no direct commits!
        - few branches
        - relatively small commits
        - high-quality testing & QA standards
        - Eg: main branch, develop branch
    - State, Release, and Feature Branches: Branches Enhance Structures & Workflows
        - different types of branches
        - fullfill different types of jobs
- Two Example Branching Strategies:
    - Github Flow: very simple, very lean: only one long-running branch ("main") + feature branches
    - GitFlow
        - more structure, more rules
        - long-running: main + develop
        - short-lived: features, releases, hotfixes

# Pull requests
- Communicating About and Reviewing Code
    - without a Pull Request, you would jump right to merging your code
    - a Pull Request invites reviewers to provide feedback and approve before merging
- Contributing Code to Other Repositories

# Merge Conflicts
- How and When Conflicts Occur: When Integrating Commit from Diffrent Soures:
    - ```git merge```
    - ```git rebase```
    - ```git pull```
    - ```git cherry-pick```
    - ```git stash apply```
- After conflict, you can use ```git status``` to check status of git
- How to Undo a Conflict and Start Over
    - ```git merge --abort```
    - ```git rebase --abort```
- Can use merge tool to resolve the conflict ```git mergetool```

# Merge vs. Rebase
- Merge: merge one branch to another branch without change the commit history 
- Rebase: Same as Merge but Rebase with reconstruct the commit history 
- <b><u>Waring note</u></b>: 
    - Do NOT use Rebase on commits that you've already pushed/shared on a remote repository
    - Instead, use it for cleaning up your local commit history before merging it inti a shared team branch

# Stash
- When to use:
    - Before checking out a different branch
    - Before pulling remote changes
    - Before merging or rebasing a branch

# Interactive Rebase
- A tool for Optimizing & Cleaning Up Your Commit History
    - Change a commit's message
    - delete commits
    - reorder commits
    - combine multiple commits into one
    - edit/split an existing commit into multiple new ones
- <b><u>Waring note</u></b>: 
    - Do NOT use Rebase on commits that you've already pushed/shared on a remote repository
    - Instead, use it for cleaning up your local commit history before merging it inti a shared team branch

# Cherry-Picking
- Integrating Single, Specific Commits
- Only use in case commit wrong branch and want to change it

# Reflog
- Like a dictionary write all action in git tree
    - recover the deleted commit
    - recover the deleted branch

# Submodules
- Copy-Pasting Third-Party Code without increase size of project
- Create a shortcut for another git in own source

# Search & Find 
- Filtering your commit history
    - by date: ```--before / --after```
    - by message: ```--grep```
    - by author: ```--author```
    - by file: ```-- <filename>```
    - by branch: ```<branch-A>```