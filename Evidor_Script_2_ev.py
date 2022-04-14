class shiel():
	def evneed(stat,base,iv,ev,lvl):
		D = (2*base+iv+(ev/4))*(lvl/100)
		return ((((stat/1.0-D)*400)/lvl)/4)*4