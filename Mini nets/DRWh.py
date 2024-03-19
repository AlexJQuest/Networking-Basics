def __init__(self):
	"Create custom topo."

	#inititialize topo
	Topo.__init__(self)

	#add h and s
	host1= self.addhost("h1")
	host2 = self.addhost("h2")
	host3 = self.addhost("h3")
	host4 = self.addhost("h4")
	switch1 = self.addSwitch("s1")
	switch2 = self.addSwitch("s2")
	switch3 = self.addSwitch("s3")
	switch4 = self.addSwitch("s4")
	control1 = self.addControl("c1")

	#add links
	self.addLink(switch1 ,switch2)
	self.addLink(switch1 ,switch3)
	self.addLink(switch1 ,switch4 )
	self.addLink(switch2 ,switch3 )	
	self.addLink(switch2 ,switch4 )
	self.addLink(switch3 ,switch4 )

topos = { 'mytopo' : (lambda: MyTopo() ) }