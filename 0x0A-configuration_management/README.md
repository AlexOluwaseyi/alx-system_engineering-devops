# 0x0A. Configuration management
## DevOps SysAdmin Scripting CI/CD

### Introduction
As a broader subject, configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time. Even though this process was not originated in the IT industry, the term is broadly used to refer to server configuration management.

### Choosing a Configuration Management Tool
There are many CM tools available in the market, each one with a different set of features and different complexity levels. Popular choices include Chef, Ansible, and Puppet. 

## Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.
### Install puppet
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
### Install puppet-lint
```bash
$ gem install puppet-lint
```
