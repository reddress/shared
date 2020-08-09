Opt("WinWaitDelay", 50)

HotKeySet("{PAUSE}", "SummonDiz")

While 1
   Sleep(100)
WEnd
   
Func SummonDiz()
   WinActivate("(2) lo Zingarelli")
   Sleep(100)
   Send("{CTRLDOWN}r{CTRLUP}")
   Sleep(50)

   Send("{END}")
   Send("{SHIFTDOWN}{HOME}{SHIFTUP}")
   Send("{DELETE}")
EndFunc
