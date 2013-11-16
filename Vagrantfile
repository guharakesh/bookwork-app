# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/centos-64-x64-vbox4210-nocm.box"
  config.vm.box = "centos-min"

  config.vm.synced_folder "provisioning/salt/roots/", "/srv/"

  config.vm.define "bookwork" do |bookwork|
    bookwork.vm.network "forwarded_port", guest: 5000, host: 5000

    bookwork.vm.provision :salt do |s|
      s.verbose = true
      s.minion_config = "provisioning/salt/bookwork-minion"
      s.run_highstate = true
    end
  end
end

