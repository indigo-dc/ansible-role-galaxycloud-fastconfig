indigo-dc.galaxycloud-fastconfig
================================

Ansible role for Galaxy fast configuration on Virtual Machines with Galaxy and tools already inside, created using indigo.dc-galaxycloud role. The role exploits the very same input of [indigo-dc.galaxycloud ansible role](https://github.com/indigo-dc/ansible-role-galaxycloud).


Requirements
------------
This ansible role supports CentOS 7 and Ubuntu 16.04 Xenial

Minimum ansible version: 2.1.2.0



Current indigo-dc.galaxycloud (and then Galaxy)  configuration is the following:
```yaml
     - hosts: servers
       roles:
         - role: indigo-dc.galaxycloud
           GALAXY_ADMIN_EMAIL: "admin@elixir-italy.org"
           GALAXY_ADMIN_USERNAME: "admin"
           GALAXY_VERSION: "release_17.05"
           galaxy_instance_key_pub: "ssh-rsa ..."
           set_pgsql_random_password: false # postgres password is fixed: galaxy
           set_proftpd_random_password: false # proftpd database password is fixed: galaxy
           galaxy_db_dir: '/home/galaxy/galaxy/database'
           tool_deps_path: '/home/galaxy/tool_deps'
           conda_prefix: '/home/galaxy/tool_deps/_conda'
```

Final Galaxy configuration, i.e. galaxycloud + galaxycloud-fastconfig is the same of galaxycloud standalone.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
    - hosts: servers
      roles:
         - role: indigo-dc.galaxycloud-fastconfig
           GALAXY_ADMIN_EMAIL: "mymail@example.com"
           GALAXY_ADMIN_USERNAME: "myuser"
           galaxy_instance_description: "mygalaxy"
           galaxy_instance_key_pub: "ssh-rsa ..."
```

License
-------

Apache Licence v2
