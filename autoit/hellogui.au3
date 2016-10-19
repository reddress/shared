#include <GUIConstantsEx.au3>

Opt("GUIOnEventMode", 1)
$mainwindow = GUICreate("Hello World",  200, 100)
GUISetOnEvent($GUI_EVENT_CLOSE, "CLOSEClicked")
$mylabel = GUICtrlCreateLabel("Hello, how are you?", 30, 10)
$okbutton = GUICtrlCreateButton("OK", 70, 50, 60)
GUICtrlSetOnEvent($okbutton, "OKButton")
GUISetState(@SW_SHOW)

While 1
   Sleep(1000)
WEnd

Func OKButton()
   ; MsgBox(0, "GUI Event", "You pressed ok")
   MouseClick("left", 210, 62)
   MouseClick("left", 210, 164)
   Sleep(200)
   Send("{RIGHT}{DOWN}{DOWN}{DOWN}{DOWN}{RIGHT}{ENTER}")
   WinWaitActive(" Ficha do Produto (PARALELO)  ")
   ; MouseClick("left", , )
   GUICtrlSetData($mylabel, "OK Clicked!")
EndFunc

Func CLOSEClicked()
   MsgBox(0, "GUI Event", "You clicked close")
   Exit
EndFunc