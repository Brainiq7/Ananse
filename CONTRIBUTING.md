# CONTRIBUTING

## ISSUE CONTRIBUTIONS

When opening new issues on this repository
please make sure you use a descriptive label  


## CODE CONTRIBUTIONS

The Ananse project welcomes new contributors.  This document will guide you
through the process.


### FORK

Fork the project [on GitHub](https://github.com/Oteng/Ananse.git) and check out
your copy.

```sh
$ git clone git@github.com:username/Ananse.git
$ cd Ananse
$ git remote add upstream git://github.com/Oteng/Ananse.git
```

As a rule of thumb, every code goes into the dev branch once it has passed all the 
tests then it get merge into the master branch. As much as possible the master branch should be
a stable branch with releasable code

The rules for the dev branch are less strict;
Feel free and be yourself. All pull requests should come to this branch


### BRANCH

You can create your own branch for a new feature you want to contribute.
Once the feature is done it will be merge with the dev branch and if all goes well 
it will find it way into the master. :)

```sh
$ git checkout -b my-feature-branch -t origin/dev
```


### COMMIT

Make sure git knows your name and email address:

```sh
$ git config --global user.name "J. Random User"
$ git config --global user.email "j.random.user@example.com"
```

Writing good commit logs is important.  A commit log should describe what
changed and why.  Follow these guidelines when writing one:

1. The first line should be 50 characters or less and contain a short
   description of the change prefixed with the name of the changed
   subsystem of feature (e.g. "net: add localAddress and localPort to Socket").
2. Keep the second line blank.
3. Wrap all other lines at 72 columns.

A good commit log looks like this:

```
subsystem: explaining the commit in one line

Body of commit message is a few lines of text, explaining things
in more detail, possibly giving some background about the issue
being fixed, etc etc.

The body of the commit message can be several paragraphs, and
please do proper word-wrap and keep columns shorter than about
72 characters or so. That way `git log` will show things
nicely even when it is indented.
```

The header line should be meaningful; it is what other people see when they
run `git shortlog` or `git log --oneline`.


### REBASE

Use `git rebase` (not `git merge`) to sync your work from time to time.

```sh
$ git fetch upstream
$ git rebase upstream/dev  # or upstream/master
```


### TEST

Bug fixes and features should come with tests.  Add your tests in the
test/ directory.  Look at other tests to see how they should be
structured (license boilerplate, common includes, etc.).

To run the test, simply invoke your favorite test runner, or execute a test file directly; any of the following work:

    python -m unittest discover
    python test/test_download.py
    nosetests --verbose


### PUSH

```sh
$ git push origin my-feature-branch
```

Go to https://github.com/username/Ananse and select your feature branch.  Click
the 'Pull Request' button and fill out the form.

Pull requests are usually reviewed within a few days.  If there are comments
to address, apply your changes in a separate commit and push that to your
feature branch.  Post a comment in the pull request afterwards; GitHub does
not send out notifications when you add commits.


# Contribution Policy

Individuals making significant and valuable contributions are given
commit-access to the project. These individuals are identified by the
Technical Committee (TC) and discussed during the weekly TC meeting.

If you make a significant contribution and are not considered for
commit-access log an issue and it will be brought up in the next TC
meeting.

Internal pull-requests to solicit feedback are required for any other
non-trivial contribution but left to the discretion of the
contributor.

Pull requests may be approved by any committer with sufficient
expertise to take full responsibility for the change, according to the
"Landing Patches" protocol described below.

## Landing Patches/Features

- All bugfixes require a test case which demonstrates the defect.  The
  test should *fail* before the change, and *pass* after the change.
- Trivial changes (ie, those which fix bugs or improve performance
  without affecting API or causing other wide-reaching impact) may be
  landed immediately after review by a committer who did not write the
  code, provided that no other committers object to the change.
- If you are unsure, or if you are the author, have someone else
  review the change.
- For significant changes wait a full 48 hours (72 hours if it spans a
  weekend) before merging so that active contributors who are
  distributed throughout the world have a chance to weigh in.
- Controversial changes and **very** significant changes should not be
  merged until they have been discussed by the TC which will make any
  final decisions.
- Always include the `Reviewed-by: Your Name <your-email>` in the
  commit message.
- In commit messages also include `Fixes:` that either includes the
  **full url** (e.g.  `https://github.com/Oteng/Ananse/issues/...`),
  and/or the hash and commit message if the commit fixes a bug in a
  previous commit.
- PR's should include their full `PR-URL:` so it's easy to trace a
  commit back to the conversation that lead up to that change.
- Double check PR's to make sure the person's **full name** and email
  address are correct before merging.
- Except when updating dependencies, all commits should be self
  contained.  Meaning, every commit should pass all tests. This makes
  it much easier when bisecting to find a breaking change.

# Governance

This repository is jointly governed by a technical committee, commonly
referred to as the "TC."

The TC has final authority over this project including:

* Technical direction
* Project governance and process (including this policy)
* Contribution policy
* GitHub repository hosting
* Conduct guidelines

## Membership

Initial membership invitations to the TC were given to individuals who
had been active contributors to Ananse.  Membership is
expected to evolve over time according to the needs of the project.

There is no specific set of requirements or qualifications for TC
membership beyond these rules.

The TC may add contributors to the TC by unanimous consensus.

A TC member may be removed from the TC by voluntary resignation, or by
unanimous consensus of all other TC members.

Changes to TC membership should be posted in the agenda, and may be
suggested as any other agenda item (see "TC Meetings" below).

If an addition or removal is proposed during a meeting, and the full
TC is not in attendance to participate, then the addition or removal
is added to the agenda for the subsequent meeting.  This is to ensure
that all members are given the opportunity to participate in all
membership decisions.  If a TC member is unable to attend a meeting
where a planned membership decision is being made, then their consent
is assumed.

No more than 1/3 of the TC members may be affiliated with the same
employer.  If removal or resignation of a TC member, or a change of
employment by a TC member, creates a situation where more than 1/3 of
the TC membership shares an employer, then the situation must be
immediately remedied by the resignation or removal of one or more TC
members affiliated with the over-represented employer(s).

## TC Meetings

The TC meets monthly on a Google hangout. The meeting is run by an
appointed moderator. Each
meeting should be published to Youtube.

Items are added to the TC agenda which are considered contentious or
are modifications of governance, contribution policy, TC membership,
or release process. The intention of the agenda is not to approve or
review all patches, that should happen continuously on GitHub (see
"Contribution Policy").

Any community member or contributor can ask that something be added to
the next meeting's agenda by logging a GitHub Issue. Any TC member or
the moderator can add the item to the agenda by a simple +1. The
moderator and the TC cannot veto or remove items.

Prior to each TC meeting the moderator will email the Agenda to the
TC. TC members can add any items they like to the agenda at the
beginning of each meeting. The moderator and the TC cannot veto or
remove items.

TC may invite persons or representatives from certain projects to
participate in a non-voting capacity. 

The moderator is responsible for summarizing the discussion of each
agenda item and send it as a pull request after the meeting.

## Consensus Seeking Process

The TC follows a [Consensus
Seeking](http://en.wikipedia.org/wiki/Consensus-seeking_decision-making)
decision making model.

When an agenda item has appeared to reach a consensus the moderator
will ask "Does anyone object?" as a final call for dissent from the
consensus.

If an agenda item cannot reach a consensus a TC member can call for
either a closing vote or a vote to table the issue to the next
meeting. The call for a vote must be seconded by a majority of the TC
or else the discussion will continue. Simple majority wins.

Note that changes to TC membership require unanimous consensus.  See
"Membership" above.


**Adapted from [io.js](https://github.com/iojs/io.js/blob/v1.x/CONTRIBUTING.md)** 