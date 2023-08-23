#!/usr/bin/pup
# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'pkill':
  command  => 'pkill -f killmenow',
  onlyif   => 'pgrep -f killmenow',
  provider => 'shell',
}
