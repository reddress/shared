;HotKeySet("{NUMPADDOT}", "_d")
HotKeySet("{NUMPADADD}", "_d")
HotKeySet("{NUMPADSUB}", "SummonCodigoHistory")

While 1
   Sleep(100)
WEnd
   
Func _d()
   Send("{F3}")
EndFunc

Func SummonCodigoHistory()
   WinActivate("Codigo History")
EndFunc