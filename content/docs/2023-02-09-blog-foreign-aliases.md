---
title: 'Blog: Foreign aliases'
date: '2023-02-09T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2023/02/09/foreign-aliases/
post_kind: link
draft: false
tldr: Foreign aliases Background Foreign aliases OWNERS and OWNERS_ALIASES in new
  repositories In an organisation with many repositories and developers that are frequently
  shifting the maintenance of OWNERS and OWNERS_ALIASES files can be tedious. In the
  passing year a couple of functionalities has been added to help with this.
summary: 'Foreign aliases Background Foreign aliases OWNERS and OWNERS_ALIASES in
  new repositories In an organisation with many repositories and developers that are
  frequently shifting the maintenance of OWNERS and OWNERS_ALIASES files can be tedious.
  In the passing year a couple of functionalities has been added to help with this.
  To avoid maintaining the OWNERS_ALIASES file in many repositories you can now refer
  to the OWNERS_ALIASES file in another repository. In the Jenkins X project we have
  the main OWNERS_ALIASES file in the jx-community repository. So in the jx repository
  the OWNERS_ALIASES file only looks like this: foreignAliases : - name : jx-community
  foreignAliases : - name : jx-community The organisation defaults to be the same
  as for the repository, but can specify as well. So in the jx-project repository
  the OWNERS_ALIASES file looks like this: foreignAliases : - name : jx-community
  org : jenkins-x foreignAliases : - name : jx-community org : jenkins-x Using the
  filed ref you can also specify a branch or tag to use instead of the default one
  of the repository. ref When creating or importing a repository using jx project
  the default content of OWNERS and OWNERS_ALIASES isn’t that useful since only the
  current user are put in the files. jx project If you create your own quickstarts
  you place the OWNERS and / or OWNERS_ALIASES files with the content of your liking
  in those. A recent new functionality is that you can put OWNERS and / or OWNERS_ALIASES
  files in the extensions directory of your cluster repository. These files will then
  be used as the default content of the files in new repositories. extensions ← Previous.'
---
Open the original post ↗ https://jenkins-x.io/blog/2023/02/09/foreign-aliases/
