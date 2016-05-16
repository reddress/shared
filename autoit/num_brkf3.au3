Opt("WinWaitDelay", 50)

;HotKeySet("{NUMPADDOT}", "_d")
HotKeySet("{NUMPADADD}", "_d")
HotKeySet("{NUMPADSUB}", "SummonCalcZero")
HotKeySet("{NUMPADMULT}", "SummonProduto")
HotKeySet("{NUMPADDIV}", "SummonSkype")
HotKeySet("{PAUSE}", "SummonCliente")

While 1
   Sleep(100)
WEnd
   
Func _d()
   Send("{F3}")
EndFunc

Func SummonCodigoHistory()
   WinActivate("Codigo History")
EndFunc

Func SummonCalcZero()
   WinActivate("Calc ZERO")
   Send("{F3}")
EndFunc

Func SummonProduto()
   WinActivate("Produto")
   Send("{F3}")
EndFunc

Func SummonSkype()
   WinActivate("Skype")
   Send("{F3}")
EndFunc

Func SummonCliente()
   WinActivate("Cliente")
   Send("{F3}")
EndFunc
