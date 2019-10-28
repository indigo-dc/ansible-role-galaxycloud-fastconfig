indigo-dc.galaxycloud-fastconfig
================================

Ansible role for Galaxy fast configuration on Virtual Machines with Galaxy and tools already inside, created using indigo.dc-galaxycloud role. 

The documentation on Galaxy Express services, which explotis this role, is [here](https://laniakea.readthedocs.io/en/latest/admin_documentation/indigo_paas_deploy/galaxy_vm.html).

Requirements
------------
This ansible role supports CentOS 7 and Ubuntu 16.04 Xenial

Minimum ansible version: 2.1.2.0

Role Variables
--------------

The role exploits the very same variables of [indigo-dc.galaxycloud ansible role](https://github.com/indigo-dc/ansible-role-galaxycloud).

###New variables###

``galaxy_tools_base_dir``: Galaxy flavor recipe directory. If this dir is not on the VM, the role will download the recipes (default ``/data``).

``tools_venv_dir``: Ephemeris install path (defaut: ``/tmp/tools_venv``).

``ephemeris_version``: Ephemeris version (defaults: ``0.7.0``).

``install_workflows``: install workflows (default: ``false``).

``install_data_libraries``: install libraries (default: ``false``).

``galaxy_flavors_recipes_url``: Git repository configuration for Galaxy-flavors-recipes (default: ``https://github.com/indigo-dc/Galaxy-flavors-recipes.git``).

``galaxy_flavors_recipes_dir``: Recipes directory on VM (default: ``{{ galaxy_tools_base_dir }}/Galaxy-flavors-recipes``).

``emote_tool_deps_dir_url``: tools tar.gz location (default: ``http://cloud.recas.ba.infn.it:8080/v1/AUTH_3b4918e0a982493e8c3ebcc43586a2a8/Laniakea-galaxy-tools-tar``).

Current indigo-dc.galaxycloud configuration to create valid images is:
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
