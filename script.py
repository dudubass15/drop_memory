#!/usr/bin/python
#coding: utf-8
import os
import commands

drop = os.system("sudo sync && sudo sysctl vm.drop_caches=3")

if(drop == 0):
	print "Comando executado com sucesso"
else:
	print "Nao foi possível executar este comando"
