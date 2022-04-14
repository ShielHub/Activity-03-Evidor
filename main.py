import Evidor_Script_1_stat as S1stat
import Evidor_Script_2_ev as S2ev

counter = 1
while counter == 1:
	print ("\n[1] Stat Calculator")
	print ("[2] EV Calculator")
	num = int(input("Choose Number:"))

	base = int(input("\nBase Stats:"))
	lvl = int(input("\nLevel:"))
	ev = int(input("\nEVHP:"))
	iv = int(input("\nIVHP:"))
	stat = int(input("\nDesire Increase in Stat:"))

	if num == 1:
		print ("\nHP = ", S1stat.rey.hpcal(base,iv,ev,lvl))
		print ("\nAttack = ", S1stat.rey.otherstat(base,iv,ev,lvl))
		print ("\nDef = ", S1stat.rey.otherstat(base,iv,ev,lvl))
		print ("\nSP. Attack = ", S1stat.rey.otherstat(base,iv,ev,lvl))
		print ("\nSP Def = ", S1stat.rey.otherstat(base,iv,ev,lvl))
		print ("\nSpeed = ", S1stat.rey.otherstat(base,iv,ev,lvl))
		print ("\nThe Needed Evs to Increase Stat is  ", S2ev.shiel.evneed(stat,base,iv,ev,lvl))
	
	elif num == 2:
		print ("\n[1]Single Stat")
		print ("\n[2]All Stats")
		num1 = int(input("Choose Number:"))
		
		if num1 == 1:
			print ("\n[1] Attack")
			print ("\n[2] Def")
			print ("\n[3] SP Attack")
			print ("\n[4] SP Def")
			print ("\n[5] Speed")
			print ("\n[6] HP")
			num01 = int(input("Choose Stat: "))
	
			if num01 == 1 or 2 or 3 or 4 or 5:
				print ("\nThe Stat is ", S1stat.rey.otherstat(base,iv,ev,lvl)) 
			elif num01 == 6:
				print ("\nHP = ", S1stat.rey.hpcal(base,iv,ev,lvl))
		elif num1 == 2:
			print ("\nHP = ", S1stat.rey.hpcal(base,iv,ev,lvl))
			print ("\nAttack = ", S1stat.rey.otherstat(base,iv,ev,lvl))
			print ("\nDef = ", S1stat.rey.otherstat(base,iv,ev,lvl))
			print ("\nSP. Attack = ", S1stat.rey.otherstat(base,iv,ev,lvl))
			print ("\nSP Def = ", S1stat.rey.otherstat(base,iv,ev,lvl))
			print ("\nSpeed = ", S1stat.rey.otherstat(base,iv,ev,lvl))
	print ("\n[1] Perform Another Calculation")
	print ("[2] End of the Program")
	num2 = int(input("Choose Number:"))
	if num2 == 2:
		break
	elif num2 == 1:
		continue