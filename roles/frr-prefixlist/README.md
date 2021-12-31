Role Name
=========

For config FRR prefix-lists

Requirements
------------

- frr installed on the remote machine

Role Variables
--------------

frr_prefixlists:
- name: <prefixlistname>
  address_family: (ipv4|ipv6)
  entries:
  - "<prefixlist entry>"

Dependencies
------------

- role: frr-facts

License
-------

CC-BY-4.0
