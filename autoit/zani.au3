Opt("WinWaitDelay", 50)

HotKeySet("{PAUSE}", "SummonDiz")

While 1
   Sleep(100)
WEnd
   
Func SummonDiz()
   WinActivate("(2) lo Zingarelli")
   Send("{CTRLDOWN}r{CTRLUP}")

   Send("{END}")
   Send("{SHIFTDOWN}{HOME}{SHIFTUP}")
   Send("{DELETE}")
EndFunc
