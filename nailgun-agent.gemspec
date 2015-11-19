Gem::Specification.new do |s|
  s.name = 'nailgun-agent'
  s.version = '0.1'

  s.summary     = 'Discovery agent'
  s.description = 'The agent is to be run on slave nodes to gather hardware information'
  s.authors     = ["OpenStack community"]
  s.email       = 'openstack-dev@lists.openstack.org'

  s.add_dependency 'ohai', '6.14.0'
  s.add_development_dependency 'rake', '10.0.4'

  s.files = ['agent']
  s.executables = ['agent']
end
