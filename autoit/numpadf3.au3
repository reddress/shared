Opt("WinWaitDelay", 50)

;HotKeySet("{NUMPADDOT}", "_d")
HotKeySet("{NUMPADADD}", "_d")
HotKeySet("{NUMPADSUB}", "SummonCalcZero")

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