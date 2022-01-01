Role Name
=========

FRR 'bgp community-list', 'bgp extcommunity-list', 'bgp large-community-list' configurator

Requirements
------------

- 'frr' and 'vtysh' installed on the remote machine

Role Variables
--------------

frr_bgp_communities:
- name: <name>
  entries:
  - "<community entry>"

frr_bgp_extcommunities:
- name: <name>
  entries:
  - "<extcommunity entry>"

frr_bgp_largecommunities:
- name: <name>
  entries:
  - "<large-community entry>"

Dependencies
------------

none

License
-------

CC-BY-4.0
